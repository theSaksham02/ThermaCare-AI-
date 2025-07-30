    # ====================================================================
# THERMACARE AI - THERMAL IMAGE CLASSIFICATION MODEL
# ====================================================================
# This script trains a machine learning model to classify thermal images into:
# - Hyperthermic (fever/high temperature)
# - Hypothermic (low temperature/cooling)
# - Normal (healthy temperature)
#
# The model uses a combination of color and texture features extracted from images.
# ====================================================================

# Import necessary libraries for image processing and machine learning
import cv2                                    # OpenCV for image reading and processing
import numpy as np                            # Numerical operations on arrays
import os                                     # File and directory operations
import joblib                                 # For saving/loading trained models
from skimage.feature import local_binary_pattern  # Texture feature extraction
from sklearn.ensemble import RandomForestClassifier  # Machine learning classifier
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support, roc_curve, auc # Model evaluation
from sklearn.preprocessing import label_binarize # For ROC curve
from itertools import cycle                   # For plotting colors
import matplotlib.pyplot as plt               # Plotting and visualization
import seaborn as sns                         # Enhanced statistical plotting
import pandas as pd                            # Data manipulation and analysis

# ====================================================================
# FEATURE EXTRACTION FUNCTION
# ====================================================================
def extract_features(image_path):
    """
    Extracts a combined feature vector from thermal images using:
    1. HSV Color Histograms (for color/temperature information)
    2. Local Binary Pattern (LBP) features (for texture information)
    """
    try:
        image = cv2.imread(image_path)
        if image is None: return None
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h_hist = cv2.calcHist([hsv_image], [0], None, [16], [0, 180])
        s_hist = cv2.calcHist([hsv_image], [1], None, [16], [0, 256])
        v_hist = cv2.calcHist([hsv_image], [2], None, [16], [0, 256])
        cv2.normalize(h_hist, h_hist)
        cv2.normalize(s_hist, s_hist)
        cv2.normalize(v_hist, v_hist)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        lbp = local_binary_pattern(gray_image, P=8, R=1, method="uniform")
        (lbp_hist, _) = np.histogram(lbp.ravel(), bins=np.arange(0, 11), range=(0, 10))
        lbp_hist = lbp_hist.astype("float")
        lbp_hist /= (lbp_hist.sum() + 1e-6)
        return np.concatenate([
            h_hist.flatten(), s_hist.flatten(), v_hist.flatten(), lbp_hist
        ])
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

# ====================================================================
# DATASET LOADING FUNCTION
# ====================================================================
def load_dataset(base_path, dataset_type):
    """
    Loads images and their corresponding labels from the structured folder system.
    """
    features = []
    labels = []
    categories = ['Hyperthermic', 'Hypothermic', 'Normal']
    for category in categories:
        folder_path = os.path.join(base_path, category, dataset_type)
        if not os.path.isdir(folder_path):
            print(f"Warning: Folder not found {folder_path}")
            continue
        print(f"Processing {category} {dataset_type} images from {folder_path}")
        for filename in os.listdir(folder_path):
            image_path = os.path.join(folder_path, filename)
            feature_vector = extract_features(image_path)
            if feature_vector is not None:
                features.append(feature_vector)
                labels.append(category)
    print(f"Loaded {len(features)} images from {dataset_type} set")
    return np.array(features), np.array(labels)

# ====================================================================
# MAIN EXECUTION BLOCK
# ====================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("THERMACARE AI - THERMAL IMAGE CLASSIFICATION")
    print("=" * 60)
    
    base_dataset_path = '.'
    
    print("Loading datasets...")
    print("-" * 40)
    X_train, y_train = load_dataset(base_dataset_path, 'Train')
    X_test, y_test = load_dataset(base_dataset_path, 'Test')
    X_val, y_val = load_dataset(base_dataset_path, 'Validation')
    
    if len(X_train) == 0:
        print("❌ ERROR: No training data found!")
        exit(1)
    
    print(f"\n📊 Dataset Statistics:")
    print(f"   Training images: {len(X_train)}")
    print(f"   Testing images: {len(X_test)}")
    print(f"   Validation images: {len(X_val)}")
    print(f"   Features per image: {X_train.shape[1] if len(X_train) > 0 else 0}")
    
    print("\n" + "=" * 50)
    print("🚀 STARTING MODEL TRAINING")
    print("=" * 50)
    
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight='balanced'
    )
    
    print("🔄 Training Random Forest model...")
    model.fit(X_train, y_train)
    print("✅ Model training complete!")
    
    print("\n" + "=" * 50)
    print("📈 EVALUATING MODEL PERFORMANCE")
    print("=" * 50)
    
    print("🔍 Testing model on test dataset...")
    predictions = model.predict(X_test)
    target_names = ['Hyperthermic', 'Hypothermic', 'Normal']
    
    print("\n📋 Detailed Classification Report:")
    print(classification_report(y_test, predictions, target_names=target_names, zero_division=0))

    # ================================================================
    # STEP 4: GENERATE VISUALIZATION PLOTS
    # ================================================================
    print("\n" + "=" * 50)
    print("📊 GENERATING 5 VISUALIZATION PLOTS")
    print("=" * 50)
    
    # --- PLOT 1: CONFUSION MATRIX ---
    print("🎨 Creating plot 1/5: Confusion Matrix...")
    cm = confusion_matrix(y_test, predictions, labels=target_names)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=target_names, yticklabels=target_names)
    plt.title('Confusion Matrix - Performance on Test Set', fontsize=14, fontweight='bold')
    plt.xlabel('Predicted Class', fontsize=12)
    plt.ylabel('True Class', fontsize=12)
    plt.tight_layout()
    plt.savefig('1_confusion_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Saved '1_confusion_matrix.png'")
    
    # --- PLOT 2: CLASS-WISE METRICS BAR CHART ---
    print("📊 Creating plot 2/5: Class-wise Metrics Chart...")
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, predictions, labels=target_names, zero_division=0)
    metrics = {'Precision': precision, 'Recall': recall, 'F1-Score': f1}
    x = np.arange(len(target_names))
    width = 0.25
    plt.figure(figsize=(10, 6))
    for i, (metric_name, values) in enumerate(metrics.items()):
        offset = (i - 1) * width
        plt.bar(x + offset, values, width, label=metric_name, alpha=0.8)
    plt.xlabel('Thermal Condition Classes', fontsize=12)
    plt.ylabel('Performance Score (0-1)', fontsize=12)
    plt.title('Model Performance Metrics by Class', fontsize=14, fontweight='bold')
    plt.xticks(x, target_names)
    plt.ylim(0, 1.05)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('2_classwise_metrics.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Saved '2_classwise_metrics.png'")
    
    # --- PLOT 3: ROC CURVES ---
    print("📈 Creating plot 3/5: ROC Curves...")
    y_train_bin = label_binarize(y_train, classes=target_names)
    y_test_bin = label_binarize(y_test, classes=target_names)
    n_classes = y_train_bin.shape[1]
    y_score = model.predict_proba(X_test)
    fpr, tpr, roc_auc = dict(), dict(), dict()
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test_bin[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    plt.figure(figsize=(8, 6))
    colors = cycle(['red', 'blue', 'green'])
    for i, color in zip(range(n_classes), colors):
        plt.plot(fpr[i], tpr[i], color=color, lw=2, label=f'ROC curve for {target_names[i]} (area = {roc_auc[i]:0.2f})')
    plt.plot([0, 1], [0, 1], 'k--', lw=2)
    plt.xlim([0.0, 1.0]); plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=12)
    plt.ylabel('True Positive Rate', fontsize=12)
    plt.title('Receiver Operating Characteristic (ROC) Curves', fontsize=14, fontweight='bold')
    plt.legend(loc="lower right")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('3_roc_curves.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Saved '3_roc_curves.png'")

    # --- PLOT 4: FEATURE IMPORTANCE ---
    print("💡 Creating plot 4/5: Top 20 Feature Importances...")
    importances = model.feature_importances_
    feature_names = [f'H_{i}' for i in range(16)] + [f'S_{i}' for i in range(16)] + [f'V_{i}' for i in range(16)] + [f'LBP_{i}' for i in range(10)]
    forest_importances = pd.Series(importances, index=feature_names).sort_values(ascending=False)
    top_20_importances = forest_importances.head(20)
    plt.figure(figsize=(10, 7))
    sns.barplot(x=top_20_importances, y=top_20_importances.index, palette='viridis')
    plt.xlabel('Importance Score', fontsize=12)
    plt.ylabel('Features', fontsize=12)
    plt.title('Top 20 Most Important Features', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('4_feature_importance.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Saved '4_feature_importance.png'")

    # --- PLOT 5: CLASS DISTRIBUTION PIE CHART ---
    print("🍰 Creating plot 5/5: Training Data Distribution...")
    unique, counts = np.unique(y_train, return_counts=True)
    class_distribution = dict(zip(unique, counts))
    plt.figure(figsize=(8, 6))
    plt.pie(class_distribution.values(), labels=class_distribution.keys(), autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Training Set Class Distribution', fontsize=14, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('5_class_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Saved '5_class_distribution.png'")
    
    print("\n" + "=" * 50)
    print("🔬 FINAL MODEL VALIDATION")
    print("=" * 50)
    if len(X_val) > 0:
        print("🧪 Testing on validation set...")
        val_accuracy = model.score(X_val, y_val)
        print(f"🎯 Final validation accuracy: {val_accuracy * 100:.2f}%")
    else:
        print("⚠️  No validation data available")
    
    print("\n" + "=" * 50)
    print("💾 SAVING TRAINED MODEL")
    print("=" * 50)
    model_filename = 'thermo_model.joblib'
    joblib.dump(model, model_filename)
    print(f"✅ Model saved as '{model_filename}'")
    
    print("\n" + "=" * 60)
    print("🎉 TRAINING COMPLETE - SUMMARY")
    print("=" * 60)
    print(f"📁 Files generated:")
    print(f"   • {model_filename}\n   • 1_confusion_matrix.png\n   • 2_classwise_metrics.png\n   • 3_roc_curves.png\n   • 4_feature_importance.png\n   • 5_class_distribution.png")
    print(f"\n🧠 Model details:")
    print(f"   • Algorithm: Random Forest Classifier")
    print(f"   • Features: {X_train.shape[1]} per image (HSV + LBP)")
    print(f"\n🚀 Ready for deployment!")
    print("=" * 60)
