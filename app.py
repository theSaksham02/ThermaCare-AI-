import os
import joblib
import cv2
import numpy as np
from flask import Flask, request, render_template_string, url_for # Import url_for
import google.generativeai as genai
from skimage.feature import local_binary_pattern
import json # Ensure json is imported for parsing

# --- CONFIGURATION ---
GEMMA_API_KEY = 'AIzaSyDMU1Pw-sYSu-FIZbOQTcGlK5hgCZljf7s' # Paste your actual Gemma API key

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
    Optimized for speed while maintaining accuracy.
    """
    try:
        # Load image with optimized settings
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if image is None: return None

        # Resize image for faster processing (maintain aspect ratio)
        height, width = image.shape[:2]
        if width > 512 or height > 512:
            scale = min(512/width, 512/height)
            new_width = int(width * scale)
            new_height = int(height * scale)
            image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

        # Convert to HSV for color features (optimized)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # Calculate histograms with optimized parameters
        h_hist = cv2.calcHist([hsv_image], [0], None, [16], [0, 180])
        s_hist = cv2.calcHist([hsv_image], [1], None, [16], [0, 256])
        v_hist = cv2.calcHist([hsv_image], [2], None, [16], [0, 256])

        # Fast normalization
        h_hist = h_hist.flatten() / (h_hist.sum() + 1e-6)
        s_hist = s_hist.flatten() / (s_hist.sum() + 1e-6)
        v_hist = v_hist.flatten() / (v_hist.sum() + 1e-6)

        # Convert to grayscale for LBP texture features
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Optimized LBP calculation
        lbp = local_binary_pattern(gray_image, P=8, R=1, method="uniform")
        lbp_hist, _ = np.histogram(lbp.ravel(), bins=10, range=(0, 10))
        lbp_hist = lbp_hist.astype("float") / (lbp_hist.sum() + 1e-6)

        # Combine all features into one vector
        return np.concatenate([h_hist, s_hist, v_hist, lbp_hist])
        
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def get_gemma_response(diagnosis):
    # Fast fallback responses for immediate results
    fallback_responses = {
        'Normal': {
            'nurse_plan': '1. Monitor infant temperature every 2-3 hours. 2. Ensure proper feeding and hydration. 3. Maintain comfortable room temperature (22-24°C).',
            'parent_message_hindi': 'आपके बच्चे का तापमान सामान्य है। कोई चिंता की बात नहीं है। नियमित रूप से खिलाते रहें और सामान्य देखभाल जारी रखें।',
            'video_id': '3yS-x98Z_eU'
        },
        'Hypothermic': {
            'nurse_plan': '1. Immediately warm the infant using skin-to-skin contact or warm blankets. 2. Monitor temperature every 30 minutes. 3. Ensure frequent feeding and check for signs of infection.',
            'parent_message_hindi': 'बच्चे का तापमान कम है। तुरंत गर्म कपड़े पहनाएं और स्तनपान कराएं। डॉक्टर से संपर्क करें।',
            'video_id': 'Z42K_t-v8MY'
        },
        'Hyperthermic': {
            'nurse_plan': '1. Remove excess clothing and blankets immediately. 2. Cool the environment and ensure proper ventilation. 3. Monitor temperature and hydration status closely.',
            'parent_message_hindi': 'बच्चे का तापमान अधिक है। अतिरिक्त कपड़े हटा दें और ठंडी जगह में रखें। तरल पदार्थ दें।',
            'video_id': 'NpRZ-p-vgoY'
        }
    }
    
    # Return immediate fallback response for speed
    if diagnosis in fallback_responses:
        return json.dumps(fallback_responses[diagnosis])
    
    # Fallback for unknown diagnosis
    return json.dumps({
        'nurse_plan': '1. Monitor the infant closely. 2. Check temperature regularly. 3. Contact healthcare provider if concerned.',
        'parent_message_hindi': 'बच्चे की निगरानी करें और डॉक्टर से सलाह लें।',
        'video_id': '3yS-x98Z_eU'
    })

# --- HTML TEMPLATE FOR THE PREMIUM DASHBOARD ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ThermoVision AI - Premium Nurse Dashboard</title>
    <link rel="icon" type="image/x-icon" href="{{ url_for('static', filename='favicon.ico') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <meta name="description" content="Advanced thermal imaging analysis for infant care. AI-powered diagnosis and clinical guidance.">
    <meta name="keywords" content="thermal imaging, infant care, AI diagnosis, healthcare, temperature monitoring">
</head>
<body>
    <div class="container">
        <!-- Header Section -->
        <div class="header fade-in-up">
            <h1>ThermoVision AI</h1>
            <p>Advanced thermal imaging analysis for infant care. Upload thermal images for instant AI-powered diagnosis and clinical guidance.</p>
        </div>

        <!-- Main Content Grid -->
        <div class="main-content">
            <!-- Upload Section -->
            <div class="upload-section fade-in-left">
                <h2>Upload Thermal Image</h2>
                <form method="post" enctype="multipart/form-data">
                    <div class="file-upload-area" onclick="document.getElementById('file-input').click()">
                        <input type="file" id="file-input" name="file" accept="image/*" required class="file-input">
                        <div class="upload-icon">📷</div>
                        <div class="upload-text">Click to select or drag & drop thermal image</div>
                        <div class="upload-button">Choose File</div>
                    </div>
                    <button type="submit" class="upload-button" style="margin-top: 1rem; width: 100%;">
                        Analyze Image
                    </button>
                </form>
            </div>

            <!-- Results Section -->
            <div class="results-section {% if diagnosis %}show{% endif %} fade-in-right">
                <h2>Analysis Results</h2>
                
                <!-- Diagnosis Card -->
                <div class="result-card diagnosis">
                    <h3>Diagnosis</h3>
                    <div class="diagnosis-badge {{ diagnosis_class if diagnosis else 'normal' }}">
                        {{ diagnosis if diagnosis else 'No analysis yet' }}
                    </div>
                </div>

                <!-- Nurse Plan Card -->
                <div class="result-card nurse-plan">
                    <h3>Action Plan for Nurse</h3>
                    <div>{{ nurse_plan | safe if nurse_plan else 'Upload an image to get clinical guidance' }}</div>
                </div>

                <!-- Parent Message Card -->
                <div class="result-card parent-message">
                    <h3>Message for Parents (Hindi)</h3>
                    <div>{{ parent_message if parent_message else 'Upload an image to get parent guidance' }}</div>
                </div>

                <!-- Specific Condition Information -->
                {% if diagnosis == 'Hypothermic' %}
                <div class="condition-info">
                    <h3>Hypothermia Risk - Important Considerations</h3>
                    <ul>
                        <li>Ensure infant is warm and dry immediately</li>
                        <li>Utilize skin-to-skin contact (Kangaroo Mother Care if applicable)</li>
                        <li>Cover with warm blankets or use radiant warmer</li>
                        <li>Monitor temperature closely and re-evaluate frequently</li>
                        <li>Feed frequently (breastfeeding encouraged)</li>
                    </ul>
                </div>
                {% elif diagnosis == 'Hyperthermic' %}
                <div class="condition-info">
                    <h3>Hyperthermia Risk - Important Considerations</h3>
                    <ul>
                        <li>Remove excess clothing/blankets</li>
                        <li>Encourage frequent fluids (breastfeeding/formula)</li>
                        <li>Cool environment (ensure good ventilation, avoid direct sun)</li>
                        <li>Monitor temperature closely; avoid rapid cooling</li>
                        <li>Look for signs of dehydration</li>
                    </ul>
                </div>
                {% endif %}
            </div>
        </div>

        <!-- Video Section -->
        {% if video_id %}
        <div class="video-section fade-in-up">
            <h2>Instructional Video</h2>
            <div class="video-container">
                <iframe src="https://www.youtube.com/embed/{{ video_id }}" 
                        title="YouTube video player" 
                        frameborder="0" 
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                        allowfullscreen>
                </iframe>
            </div>
        </div>
        {% endif %}

        <!-- Loading Animation -->
        <div class="loading">
            <div class="spinner"></div>
            <p>Analyzing thermal image...</p>
        </div>
    </div>

    <!-- JavaScript -->
    <script src="{{ url_for('static', filename='js/app.js') }}"></script>
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

            # 1. Get diagnosis from your model (optimized)
            features = extract_features(filepath)
            if features is not None:
                prediction = model.predict([features])
                diagnosis = prediction[0]
            else:
                diagnosis = "Error: Could not process image"

            # 2. Get fast response (no API delay)
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