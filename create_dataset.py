# Import necessary libraries for image processing and file operations
import cv2                      # OpenCV for image reading and processing
import matplotlib.pyplot as plt # For color mapping (thermal visualization)
import os                       # For file and directory operations
import numpy as np              # For numerical operations on image arrays

# Configuration: Define input and output directories
# INPUT_FOLDER: Contains the original source images to be processed
INPUT_FOLDER = 'New_Source_Images' 

# OUTPUT_FOLDER: Where all generated thermal images will be saved
OUTPUT_FOLDER = 'Generated_Images' 

# COLOR_MAP: Defines the thermal color scheme (jet colormap - blue=cold, red=hot)
COLOR_MAP = plt.cm.jet

# Start the dataset generation process
print(f"Starting dataset generation from '{INPUT_FOLDER}'...")

# Create the main output directory if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Find all image files in the input folder (supports .png, .jpg, .jpeg)
image_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Check if any images were found
if not image_files:
    print(f"Error: No images found in '{INPUT_FOLDER}'. Please check the folder.")
else:
    # Process each source image to create 9 thermal variations (3 per class)
    for i, filename in enumerate(image_files):
        img_path = os.path.join(INPUT_FOLDER, filename)
        
        # Read image in grayscale mode (thermal images are typically grayscale)
        # Grayscale values represent temperature intensity
        gray_image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        # Skip if image couldn't be loaded
        if gray_image is None:
            continue

        # ====================================================================
        # SECTION 1: CREATE NORMAL THERMAL IMAGES (3 versions)
        # ====================================================================
        # Normal thermal images represent healthy body temperature
        # We create slight variations to increase dataset diversity
        
        # Version 1: Use original grayscale as baseline normal temperature
        normal_v1 = np.clip(gray_image, 0, 255).astype(np.uint8)
        
        # Version 2: Slightly brighter (simulate minor temperature variation)
        normal_v2 = np.clip(gray_image * 1.1, 0, 255).astype(np.uint8)
        
        # Version 3: Slightly darker (simulate another temperature variation)
        normal_v3 = np.clip(gray_image * 0.9, 0, 255).astype(np.uint8)
        
        # Create directory for normal class images
        normal_folder = os.path.join(OUTPUT_FOLDER, 'Normal')
        if not os.path.exists(normal_folder):
            os.makedirs(normal_folder)
            
        # Save all 3 normal variations to the Normal folder
        cv2.imwrite(os.path.join(normal_folder, f'normal_{i}_v1.jpg'), normal_v1)
        cv2.imwrite(os.path.join(normal_folder, f'normal_{i}_v2.jpg'), normal_v2)
        cv2.imwrite(os.path.join(normal_folder, f'normal_{i}_v3.jpg'), normal_v3)

        # ====================================================================
        # SECTION 2: CREATE HYPOTHERMIC IMAGES (3 versions)
        # ====================================================================
        # Hypothermia = abnormally low body temperature
        # Simulate this by darkening peripheral areas (extremities cool first)
        
        # Start with a copy of the original image for manipulation
        hypo_base = gray_image.copy().astype(float)
        rows, cols = hypo_base.shape
        
        # Version 1: Strong peripheral cooling effect
        # Darken the outer 20% borders of the image (hands, feet, edges)
        # This simulates how extremities lose heat first in hypothermia
        hypo_base[0:int(rows*0.2), :] *= 0.4          # Top 20% darker
        hypo_base[int(rows*0.8):rows, :] *= 0.4       # Bottom 20% darker  
        hypo_base[:, 0:int(cols*0.2)] *= 0.4          # Left 20% darker
        hypo_base[:, int(cols*0.8):cols] *= 0.4       # Right 20% darker
        hypo_v1 = np.clip(hypo_base, 0, 255).astype(np.uint8)
        
        # Version 2: Moderate cooling (less intense than v1)
        hypo_v2 = np.clip(hypo_base * 1.1, 0, 255).astype(np.uint8)
        
        # Version 3: Mild cooling with slight brightness boost
        # Add 20 to simulate some areas retaining heat
        hypo_v3 = np.clip(hypo_base * 0.9 + 20, 0, 255).astype(np.uint8)
        
        # Create directory for hypothermic class images
        hypo_folder = os.path.join(OUTPUT_FOLDER, 'Hypothermic')
        if not os.path.exists(hypo_folder):
            os.makedirs(hypo_folder)
            
        # Save all 3 hypothermic variations
        cv2.imwrite(os.path.join(hypo_folder, f'hypothermic_{i}_v1.jpg'), hypo_v1)
        cv2.imwrite(os.path.join(hypo_folder, f'hypothermic_{i}_v2.jpg'), hypo_v2)
        cv2.imwrite(os.path.join(hypo_folder, f'hypothermic_{i}_v3.jpg'), hypo_v3)

        # ====================================================================
        # SECTION 3: CREATE HYPERTHERMIC IMAGES (3 versions)
        # ====================================================================
        # Hyperthermia = abnormally high body temperature (fever)
        # Simulate this by increasing brightness and contrast
        
        # Version 1: High heat - multiply by 1.5 for overall brightness increase
        # This simulates elevated body temperature across the entire body
        hyper_v1 = np.clip(gray_image * 1.5, 0, 255).astype(np.uint8)
        
        # Version 2: Moderate heat - add constant value to increase brightness
        # Adding 50 to all pixels simulates general temperature elevation
        hyper_v2 = np.clip(gray_image + 50, 0, 255).astype(np.uint8)
        
        # Version 3: High contrast heat pattern
        # Histogram equalization redistributes intensity values for high contrast
        # This simulates uneven heat distribution typical in fever
        hyper_v3 = cv2.equalizeHist(gray_image)
        
        # Create directory for hyperthermic class images
        hyper_folder = os.path.join(OUTPUT_FOLDER, 'Hyperthermic')
        if not os.path.exists(hyper_folder):
            os.makedirs(hyper_folder)
            
        # Save all 3 hyperthermic variations
        cv2.imwrite(os.path.join(hyper_folder, f'hyperthermic_{i}_v1.jpg'), hyper_v1)
        cv2.imwrite(os.path.join(hyper_folder, f'hyperthermic_{i}_v2.jpg'), hyper_v2)
        cv2.imwrite(os.path.join(hyper_folder, f'hyperthermic_{i}_v3.jpg'), hyper_v3)
        
        # Progress update: Show which file was processed
        print(f"Processed {filename}: Created 9 new images (3 normal, 3 hypothermic, 3 hyperthermic)")
    # Summary of image generation process
    print(f"Success! Generated {len(image_files) * 9} new images in the '{OUTPUT_FOLDER}' folder.")

    # ====================================================================
    # SECTION 4: AUTOMATIC DATASET SPLITTING
    # ====================================================================
    # After generating all images, automatically split them into train/test/validation sets
    # This ensures proper machine learning workflow without manual file organization
    
    print("\nSplitting images into train/test/validation sets...")
    random.seed(42)  # Set seed for reproducible random splits
    
    # Process each class folder (Normal, Hypothermic, Hyperthermic)
    for cls in ['Normal', 'Hypothermic', 'Hyperthermic']:
        class_folder = os.path.join(OUTPUT_FOLDER, cls)
        if os.path.isdir(class_folder):
            split_dataset(class_folder, class_folder)
        else:
            print(f"Class folder not found: {class_folder}")

# ====================================================================
# UTILITY FUNCTIONS FOR DATASET SPLITTING
# ====================================================================
import shutil  # For copying files
import random  # For random shuffling of images

def split_dataset(class_folder, output_base, train_ratio=0.8, test_ratio=0.1, val_ratio=0.1):
    """
    Split images in a class folder into Train/Test/Validation subsets
    
    Parameters:
    - class_folder: Path to folder containing images for one class
    - output_base: Base path where Train/Test/Validation folders will be created
    - train_ratio: Percentage of images for training (default: 80%)
    - test_ratio: Percentage of images for testing (default: 10%) 
    - val_ratio: Percentage of images for validation (default: 10%)
    
    Process:
    1. Find all image files in the class folder
    2. Randomly shuffle them to ensure random distribution
    3. Split based on the specified ratios
    4. Copy files to appropriate Train/Test/Validation subfolders
    """
    
    # Find all image files in the class folder
    images = [f for f in os.listdir(class_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    # Randomly shuffle the list to ensure random distribution across splits
    random.shuffle(images)
    
    # Calculate exact numbers for each split
    n = len(images)                          # Total number of images
    n_train = int(n * train_ratio)           # Number for training (80%)
    n_test = int(n * test_ratio)             # Number for testing (10%)
    n_val = n - n_train - n_test             # Remaining for validation (10%)
    
    # Create splits dictionary with appropriate image lists
    splits = {
        'Train': images[:n_train],                           # First 80% for training
        'Test': images[n_train:n_train+n_test],             # Next 10% for testing
        'Validation': images[n_train+n_test:]                # Final 10% for validation
    }
    
    # Create subfolders and copy files for each split
    for split, files in splits.items():
        # Create subdirectory (e.g., Normal/Train, Normal/Test, Normal/Validation)
        split_dir = os.path.join(output_base, split)
        if not os.path.exists(split_dir):
            os.makedirs(split_dir)
        
        # Copy each file to the appropriate subdirectory
        for fname in files:
            src = os.path.join(class_folder, fname)    # Source file path
            dst = os.path.join(split_dir, fname)       # Destination file path
            shutil.copy2(src, dst)                     # Copy file with metadata
    
    # Print summary of the splitting process
    print(f"{os.path.basename(class_folder)}: {n} images split into {n_train} train, {n_test} test, {n_val} validation.")
      