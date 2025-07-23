import cv2
import numpy as np
import os
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# --- 1. Feature Extraction Function ---
# This function is the same as before. It describes an image using numbers.
def extract_color_histogram(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None: return None
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv_image], [0], None, [16], [0, 180])
        cv2.normalize(hist, hist)
        return hist.flatten()
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

# --- 2. Updated Load Dataset Function ---
# This function is updated to work with your new folder structure.
def load_dataset(base_path, dataset_type): # dataset_type can be 'train', 'test', or 'validation'
    """Loads images and labels from the new folder structure."""
    features = []
    labels = []
    
    # The categories are the main folders: Hyperthermic, Hypothermic, Normal
    categories = ['Hyperthermic', 'Hypothermic', 'Normal']
    
    for category in categories:
        # Build the full path to the train/test/validation folder for each category
        folder_path = os.path.join(base_path, category, dataset_type)
        
        if not os.path.isdir(folder_path):
            print(f"Warning: Folder not found {folder_path}")
            continue
            
        # Process each image in that folder
        for filename in os.listdir(folder_path):
            image_path = os.path.join(folder_path, filename)
            histogram = extract_color_histogram(image_path)
            
            if histogram is not None:
                features.append(histogram)
                labels.append(category) # The label is the name of the main folder
                
    return np.array(features), np.array(labels)

# --- 3. Main Training and Evaluation ---
if __name__ == "__main__":
    base_dataset_path = '.' # This means the current directory

    print("Loading training data...")
    X_train, y_train = load_dataset(base_dataset_path, 'train')

    print("Loading testing data...")
    X_test, y_test = load_dataset(base_dataset_path, 'test')
    
    if len(X_train) == 0:
        print("Training data not found! Please check your folder structure.")
    else:
        print("\n--- Starting Model Training ---")
        model = SVC(kernel='rbf', C=1.0, probability=True, random_state=42)
        
        # This is where the magic happens: the model learns from your data
        model.fit(X_train, y_train)
        print("--- Model Training Complete! ---\n")
        
        print("--- Evaluating Model on Test Data ---")
        predictions = model.predict(X_test)
        
        # This report shows you how well your model performed
        print(classification_report(y_test, predictions, target_names=['Hyperthermic', 'Hypothermic', 'Normal']))

        print("\n--- Performing Final Check on Validation Data ---")
        X_val, y_val = load_dataset(base_dataset_path, 'validation')
        if len(X_val) > 0:
            val_accuracy = model.score(X_val, y_val)
            print(f"Final accuracy on unseen validation set: {val_accuracy * 100:.2f}%")
