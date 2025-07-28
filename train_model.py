import cv2
import numpy as np
import os
import joblib
from skimage.feature import local_binary_pattern
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Renamed and Final Feature Extraction Function ---
def extract_features(image_path):
    """
    Extracts a combined feature vector of HSV color histograms and LBP texture features.
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

# --- 2. Load Dataset Function ---
def load_dataset(base_path, dataset_type):
    """Loads images and labels from the structured folder."""
    features = []
    labels = []
    categories = ['Hyperthermic', 'Hypothermic', 'Normal']
    
    for category in categories:
        folder_path = os.path.join(base_path, category, dataset_type)
        if not os.path.isdir(folder_path):
            print(f"Warning: Folder not found {folder_path}")
            continue
            
        for filename in os.listdir(folder_path):
            image_path = os.path.join(folder_path, filename)
            # Use the renamed function here
            feature_vector = extract_features(image_path)
            
            if feature_vector is not None:
                features.append(feature_vector)
                labels.append(category)
                
    return np.array(features), np.array(labels)

# --- 3. Main Execution Block ---
if __name__ == "__main__":
    base_dataset_path = '.'

    print("Loading data...")
    X_train, y_train = load_dataset(base_dataset_path, 'Train')
    X_test, y_test = load_dataset(base_dataset_path, 'Test')
    X_val, y_val = load_dataset(base_dataset_path, 'Validation')
    
    if len(X_train) == 0:
        print("Training data not found! Please check your folder structure.")
    else:
        print("\n--- Starting Model Training ---")
        # Added class_weight='balanced' to help with imbalanced data
        model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
        model.fit(X_train, y_train)
        print("--- Model Training Complete! ---\n")

        print("--- Evaluating Model on Test Data ---")
        predictions = model.predict(X_test)
        target_names = ['Hyperthermic', 'Hypothermic', 'Normal']
        print(classification_report(y_test, predictions, target_names=target_names, zero_division=0))

        # Generate and save Confusion Matrix
        cm = confusion_matrix(y_test, predictions, labels=target_names)
        plt.figure(figsize=(6, 5))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=target_names, yticklabels=target_names)
        plt.title('Confusion Matrix (Test Set)')
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.tight_layout()
        plt.savefig('confusion_matrix.png')
        plt.close()

        # Generate and save Bar Plot of metrics
        precision, recall, f1, _ = precision_recall_fscore_support(y_test, predictions, labels=target_names, zero_division=0)
        metrics = {'Precision': precision, 'Recall': recall, 'F1-Score': f1}
        x = np.arange(len(target_names))
        width = 0.2
        plt.figure(figsize=(8, 5))
        for i, (metric_name, values) in enumerate(metrics.items()):
            plt.bar(x + i*width - width, values, width, label=metric_name)
        plt.xticks(x, target_names)
        plt.ylim(0, 1.05)
        plt.ylabel('Score')
        plt.title('Class-wise Metrics (Test Set)')
        plt.legend()
        plt.tight_layout()
        plt.savefig('classwise_metrics.png')
        plt.close()

        print("\n--- Performing Final Check on Validation Data ---")
        if len(X_val) > 0:
            val_accuracy = model.score(X_val, y_val)
            print(f"Final accuracy on unseen validation set: {val_accuracy * 100:.2f}%")

        # Save the final trained model
        print("\n--- Saving the trained model to a file ---")
        joblib.dump(model, 'thermo_model.joblib')
        print("Model saved as thermo_model.joblib")