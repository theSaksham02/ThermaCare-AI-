import os
import joblib
import cv2
import numpy as np
from flask import Flask, request, render_template_string, url_for
import google.generativeai as genai
from skimage.feature import local_binary_pattern
import json

# --- CONFIGURATION ---
GEMMA_API_KEY = 'AIzaSyDMU1Pw-sYSu-FIZbOQTcGlK5hgCZljf7s'

# --- INITIALIZE APP & MODELS ---
app = Flask(__name__)

# Load your saved model
model = joblib.load('thermo_model.joblib')
# Configure Gemma
genai.configure(api_key=GEMMA_API_KEY)
gemma_model = genai.GenerativeModel('gemini-1.5-flash')

# --- HELPER FUNCTIONS ---
def extract_features(image_path):
    """
    Extracts a combined feature vector of HSV color histograms and LBP texture features.
    This must be IDENTICAL to the function used in Train.py.
    """
    try:
        image = cv2.imread(image_path)
        if image is None: return None

        # Convert to HSV for color features
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h_hist = cv2.calcHist([hsv_image], [0], None, [16], [0, 180])
        s_hist = cv2.calcHist([hsv_image], [1], None, [16], [0, 256])
        v_hist = cv2.calcHist([hsv_image], [2], None, [16], [0, 256])

        # Normalize histograms
        cv2.normalize(h_hist, h_hist)
        cv2.normalize(s_hist, s_hist)
        cv2.normalize(v_hist, v_hist)

        # Convert to grayscale for LBP texture features
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        lbp = local_binary_pattern(gray_image, P=8, R=1, method="uniform")
        (lbp_hist, _) = np.histogram(lbp.ravel(), bins=np.arange(0, 11), range=(0, 10))
        lbp_hist = lbp_hist.astype("float")
        lbp_hist /= (lbp_hist.sum() + 1e-6) # Normalize

        # Combine all features into one powerful vector
        return np.concatenate([
            h_hist.flatten(),
            s_hist.flatten(),
            v_hist.flatten(),
            lbp_hist
        ])
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def get_gemma_response(diagnosis):
    # This function triggers Gemma to get all the required info
    prompt = f"""
    An infant's thermal scan resulted in a diagnosis of '{diagnosis}'.
    You are a clinical assistant AI. Generate a JSON object with the following three keys:
    1. "nurse_plan": A concise, 3-step action plan for a nurse in a low-resource clinic. Each step should be a separate point.
    2. "parent_message_hindi": A simple, reassuring explanation for a parent in Hindi.
    3. "video_id": Provide only the YouTube video ID for a relevant instructional video. For 'Hypothermia Risk', use 'Z42K_t-v8MY'. For 'Hyperthermia Risk', use 'NpRZ-p-vgoY'. For 'Normal', use '3yS-x98Z_eU'.
    Ensure the output is a valid JSON string.
    """
    if gemma_model is None:
        return '{"nurse_plan": "Error communicating with AI assistant.", "parent_message_hindi": "त्रुटि", "video_id": "3yS-x98Z_eU"}'
    try:
        response = gemma_model.generate_content(prompt)
        # Clean up the response to be valid JSON
        clean_json_string = response.text.strip().replace('```json', '').replace('```', '')
        return clean_json_string
    except Exception as e:
        print(f"Gemma API Error: {e}")
        # Return a fallback JSON so the app doesn't crash
        return '{"nurse_plan": "Error communicating with AI assistant.", "parent_message_hindi": "त्रुटि", "video_id": "3yS-x98Z_eU"}'

# --- HTML TEMPLATE FOR THE DASHBOARD ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ThermoVision AI - Nurse Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            background: linear-gradient(-45deg, #98d8c8, #7fb069, #a8d5ba, #6b8e23);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            color: #2d3748;
            line-height: 1.6;
            min-height: 100vh;
            padding: 40px 20px;
        }
        
        @keyframes gradientShift {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        h1 {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #10a37f, #1a73e8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 10px;
        }
        
        h2 {
            color: #10a37f;
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 20px;
        }
        
        .upload-section {
            text-align: center;
            padding: 40px;
            border: 3px dashed #e2e8f0;
            border-radius: 15px;
            margin-bottom: 40px;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
            transition: all 0.3s ease;
        }
        
        .upload-section:hover {
            border-color: #10a37f;
            background: rgba(16, 163, 127, 0.05);
            transform: translateY(-2px);
        }
        
        .upload-section input[type="file"] {
            margin-bottom: 20px;
            padding: 15px;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            background: white;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        
        .upload-section input[type="file"]:focus {
            outline: none;
            border-color: #10a37f;
            box-shadow: 0 0 0 3px rgba(16, 163, 127, 0.1);
        }
        
        .results-section {
            display: {% if diagnosis %}block{% else %}none{% endif %};
            animation: fadeInUp 0.6s ease-out;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .result-box {
            background: white;
            border-left: 5px solid #10a37f;
            padding: 25px;
            margin-bottom: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        
        .result-box:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        }
        
        .result-box.hyperthermic {
            background: linear-gradient(135deg, #fff5f5, #fed7d7);
            border-left-color: #f56565;
        }
        
        .result-box.hypothermic {
            background: linear-gradient(135deg, #f0fff4, #c6f6d5);
            border-left-color: #48bb78;
        }
        
        .result-box strong {
            color: #2d3748;
            font-size: 1.1rem;
            font-weight: 600;
        }
        
        .video-container {
            position: relative;
            padding-bottom: 56.25%;
            height: 0;
            overflow: hidden;
            max-width: 100%;
            background: #000;
            margin-top: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        }
        
        .video-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border-radius: 15px;
        }
        
        button {
            background: linear-gradient(135deg, #10a37f, #0d8a6f);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(16, 163, 127, 0.3);
        }
        
        button:hover {
            background: linear-gradient(135deg, #0d8a6f, #0a6b5a);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(16, 163, 127, 0.4);
        }
        
        .specific-condition-info {
            background: linear-gradient(135deg, #fffaf0, #feebc8);
            border-left: 5px solid #ed8936;
            padding: 25px;
            margin-top: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        }
        
        .specific-condition-info h3 {
            color: #c05621;
            margin-bottom: 15px;
            font-size: 1.3rem;
        }
        
        .specific-condition-info ul {
            list-style: none;
            padding: 0;
        }
        
        .specific-condition-info li {
            padding: 8px 0;
            border-bottom: 1px solid rgba(237, 137, 54, 0.1);
            position: relative;
            padding-left: 25px;
        }
        
        .specific-condition-info li::before {
            content: '•';
            color: #ed8936;
            font-weight: bold;
            font-size: 1.2rem;
            position: absolute;
            left: 0;
        }
        
        .specific-condition-info li:last-child {
            border-bottom: none;
        }
        
        @media (max-width: 768px) {
            body {
                padding: 20px 10px;
            }
            
            .container {
                padding: 30px 20px;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            .upload-section {
                padding: 30px 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>ThermoVision AI Dashboard</h1>

        <div class="upload-section">
            <h2>Upload Infant Thermal Image</h2>
            <form method="post" enctype="multipart/form-data">
                <input type="file" name="file" required>
                <button type="submit">Analyze</button>
            </form>
        </div>

        <div class="results-section">
            <h2>Analysis Results</h2>
            <div class="result-box {{ diagnosis_class }}">
                <strong>Diagnosis:</strong> {{ diagnosis }}
            </div>

            <div class="result-box">
                <strong>Action Plan for Nurse:</strong>
                <p>{{ nurse_plan | safe }}</p>
            </div>

            <div class="result-box">
                <strong>Message for Parents (Hindi):</strong>
                <p>{{ parent_message }}</p>
            </div>

            {% if diagnosis == 'Hypothermic' %}
            <div class="specific-condition-info hypothermic">
                <h3>Hypothermia Risk - Important Considerations:</h3>
                <ul>
                    <li>Ensure infant is warm and dry immediately.</li>
                    <li>Utilize skin-to-skin contact (Kangaroo Mother Care if applicable).</li>
                    <li>Cover with warm blankets or use radiant warmer.</li>
                    <li>Monitor temperature closely and re-evaluate frequently.</li>
                    <li>Feed frequently (breastfeeding encouraged).</li>
                </ul>
            </div>
            {% elif diagnosis == 'Hyperthermic' %}
            <div class="specific-condition-info hyperthermic">
                <h3>Hyperthermia Risk - Important Considerations:</h3>
                <ul>
                    <li>Remove excess clothing/blankets.</li>
                    <li>Encourage frequent fluids (breastfeeding/formula).</li>
                    <li>Cool environment (ensure good ventilation, avoid direct sun).</li>
                    <li>Monitor temperature closely; avoid rapid cooling.</li>
                    <li>Look for signs of dehydration.</li>
                </ul>
            </div>
            {% endif %}

            <h2>Instructional Video</h2>
            <div class="video-container">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/{{ video_id }}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
        </div>
    </div>
</body>
</html>
"""

# --- FLASK ROUTES ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400

        if file:
            # Save the uploaded file temporarily
            filepath = os.path.join('uploads', file.filename)
            if not os.path.exists('uploads'):
                os.makedirs('uploads')
            file.save(filepath)

            # 1. Get diagnosis from your model
            features = extract_features(filepath)
            if features is not None:
                prediction = model.predict([features])
                diagnosis = prediction[0]
            else:
                diagnosis = "Error: Could not process image"

            # 2. Trigger Gemma
            gemma_data_str = get_gemma_response(diagnosis)
            gemma_data = json.loads(gemma_data_str)

            nurse_plan_raw = gemma_data.get('nurse_plan', 'N/A')

            # --- START OF FIX FOR 'AttributeError: 'list' object has no attribute 'split'' ---
            nurse_plan_html = ""
            if isinstance(nurse_plan_raw, list):
                # If Gemma returns a list, format it as an unordered list directly
                nurse_plan_html = "<ul>" + "".join([f"<li>{item.strip()}</li>" for item in nurse_plan_raw if item.strip()]) + "</ul>"
            elif isinstance(nurse_plan_raw, str):
                # If Gemma returns a string (as expected), process it to split by periods
                if diagnosis != "Error: Could not process image":
                    # Only apply numbered list if there's an actual diagnosis
                    nurse_plan_html = "<ul>" + "".join([f"<li>{step.strip()}</li>" for step in nurse_plan_raw.split('.') if step.strip()]) + "</ul>"
                else:
                    nurse_plan_html = nurse_plan_raw.replace('\n', '<br>') # Fallback for error or non-list format
            else:
                # Fallback for unexpected data types
                nurse_plan_html = str(nurse_plan_raw).replace('\n', '<br>')
            # --- END OF FIX ---

            # Pass all data to the dashboard
            return render_template_string(HTML_TEMPLATE,
                                          diagnosis=diagnosis,
                                          diagnosis_class=diagnosis.lower(),
                                          nurse_plan=nurse_plan_html,
                                          parent_message=gemma_data.get('parent_message_hindi', 'N/A'),
                                          video_id=gemma_data.get('video_id', '3yS-x98Z_eU'))

    # Render the initial page with the upload form
    return render_template_string(HTML_TEMPLATE, diagnosis=None)

# --- RUN THE APP ---
if __name__ == '__main__':
    port = int(os.getenv('PORT', '5050'))
    # Use 127.0.0.1 for local only. Change to '0.0.0.0' when deploying.
    app.run(host='127.0.0.1', port=port, debug=True)