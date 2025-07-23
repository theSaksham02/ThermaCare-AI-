import cv2
import numpy as np
import os
from skimage.feature import local_binary_pattern
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support
import matplotlib.pyplot as plt
import seaborn as sns


# This function is the same as before. It describes an image using numbers.
def extract_color_histogram(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None: return None
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # Calculate histograms for H, S, and V channels
        h_hist = cv2.calcHist([hsv_image], [0], None, [16], [0, 180])
        s_hist = cv2.calcHist([hsv_image], [1], None, [16], [0, 256])
        v_hist = cv2.calcHist([hsv_image], [2], None, [16], [0, 256])
        # Normalize each histogram
        cv2.normalize(h_hist, h_hist)
        cv2.normalize(s_hist, s_hist)
        cv2.normalize(v_hist, v_hist)
        # LBP texture feature extraction (on grayscale)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        lbp = local_binary_pattern(gray_image, P=8, R=1, method="uniform")
        # Compute LBP histogram
        (lbp_hist, _) = np.histogram(lbp.ravel(), bins=np.arange(0, 11), range=(0, 10))
        lbp_hist = lbp_hist.astype("float")
        lbp_hist /= (lbp_hist.sum() + 1e-6)
        # Concatenate all histograms into a single feature vector
        return np.concatenate([
            h_hist.flatten(),
            s_hist.flatten(),
            v_hist.flatten(),
            lbp_hist
        ])
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None


# This function is updated to work with your new folder structure.
def load_dataset(base_path, dataset_type): # dataset_type can be 'Train', 'Test', or 'Validation'
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


if __name__ == "__main__":
    base_dataset_path = '.' # This means the current directory

    print("Loading training data...")
    X_train, y_train = load_dataset(base_dataset_path, 'Train')

    print("Loading testing data...")
    X_test, y_test = load_dataset(base_dataset_path, 'Test')
    
    if len(X_train) == 0:
        print("Training data not found! Please check your folder structure.")
    else:
        print("\n--- Starting Model Training ---")
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        print("--- Model Training Complete! ---\n")

        print("--- Evaluating Model on Test Data ---")
        predictions = model.predict(X_test)
        target_names = ['Hyperthermic', 'Hypothermic', 'Normal']
        print(classification_report(y_test, predictions, target_names=target_names))

        # 1. Confusion Matrix
        cm = confusion_matrix(y_test, predictions, labels=target_names)
        plt.figure(figsize=(6, 5))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=target_names, yticklabels=target_names)
        plt.title('Confusion Matrix (Test Set)')
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.tight_layout()
        plt.savefig('confusion_matrix.png')
        plt.close()

        # 2. Bar Plot of Precision, Recall, F1-Score
        precision, recall, f1, _ = precision_recall_fscore_support(y_test, predictions, labels=target_names, zero_division=0)
        metrics = {'Precision': precision, 'Recall': recall, 'F1-Score': f1}
        x = np.arange(len(target_names))
        width = 0.2
        plt.figure(figsize=(8, 5))
        for i, (metric, values) in enumerate(metrics.items()):
            plt.bar(x + i*width, values, width, label=metric)
        plt.xticks(x + width, target_names)
        plt.ylim(0, 1)
        plt.ylabel('Score')
        plt.title('Class-wise Precision, Recall, F1-Score (Test Set)')
        plt.legend()
        plt.tight_layout()
        plt.savefig('classwise_metrics.png')
        plt.close()

        # 3. Feature Importance Plot
        importances = model.feature_importances_
        plt.figure(figsize=(10, 4))
        plt.bar(range(len(importances)), importances)
        plt.title('Feature Importances (Random Forest)')
        plt.xlabel('Feature Index')
        plt.ylabel('Importance')
        plt.tight_layout()
        plt.savefig('feature_importance.png')
        plt.close()

        print("\n--- Performing Final Check on Validation Data ---")
        X_val, y_val = load_dataset(base_dataset_path, 'Validation')
        if len(X_val) > 0:
            val_accuracy = model.score(X_val, y_val)
            print(f"Final accuracy on unseen validation set: {val_accuracy * 100:.2f}%")
