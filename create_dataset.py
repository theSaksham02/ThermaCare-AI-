import cv2
import matplotlib.pyplot as plt
import os
import numpy as np


# Folder with your 11 new source images
INPUT_FOLDER = 'New_Source_Images' 

# Folder where the new images will be saved
OUTPUT_FOLDER = 'Generated_Images' 

# The thermal color map we'll use
COLOR_MAP = plt.cm.jet


print(f"Starting dataset generation from '{INPUT_FOLDER}'...")

# Create output folder if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

image_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg'))]

if not image_files:
    print(f"Error: No images found in '{INPUT_FOLDER}'. Please check the folder.")
else:
    for i, filename in enumerate(image_files):
        img_path = os.path.join(INPUT_FOLDER, filename)
        # Read image in grayscale for thermal mapping
        gray_image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if gray_image is None:
            continue

        # --- 1. Create NORMAL images (3 versions) ---
        # Add slight variations for more data
        normal_v2 = np.clip(gray_image * 1.1, 0, 255).astype(np.uint8)
        normal_v3 = np.clip(gray_image * 0.9, 0, 255).astype(np.uint8)
        # Make a folder for normal images
        normal_folder = os.path.join(OUTPUT_FOLDER, 'Normal')
        if not os.path.exists(normal_folder):
            os.makedirs(normal_folder)
        # Save normal images in the normal folder
        cv2.imwrite(os.path.join(normal_folder, f'normal_{i}_v1.jpg'), np.clip(gray_image, 0, 255).astype(np.uint8))
        cv2.imwrite(os.path.join(normal_folder, f'normal_{i}_v2.jpg'), normal_v2)
        cv2.imwrite(os.path.join(normal_folder, f'normal_{i}_v3.jpg'), normal_v3)

        # --- 2. Create HYPOTHERMIC images (3 versions) ---
        # Simulate cooling by darkening parts of the image
        hypo_base = gray_image.copy().astype(float)
        rows, cols = hypo_base.shape
        # Version 1: Strong peripheral cooling
        hypo_base[0:int(rows*0.2), :] *= 0.4
        hypo_base[int(rows*0.8):rows, :] *= 0.4
        hypo_base[:, 0:int(cols*0.2)] *= 0.4
        hypo_base[:, int(cols*0.8):cols] *= 0.4
        # Version 2: Moderate cooling
        hypo_v2 = np.clip(hypo_base * 1.1, 0, 255).astype(np.uint8)
        # Version 3: Less intense cooling
        hypo_v3 = np.clip(hypo_base * 0.9 + 20, 0, 255).astype(np.uint8)
        #Make a folder for hypothermic images
        hypo_folder = os.path.join(OUTPUT_FOLDER, 'Hypothermic')
        if not os.path.exists(hypo_folder):
            os.makedirs(hypo_folder)
        # Save hypothermic images in the hypothermic folder
        cv2.imwrite(os.path.join(hypo_folder, f'hypothermic_{i}_v1.jpg'), np.clip(hypo_base, 0, 255).astype(np.uint8))
        cv2.imwrite(os.path.join(hypo_folder, f'hypothermic_{i}_v2.jpg'), hypo_v2)
        cv2.imwrite(os.path.join(hypo_folder, f'hypothermic_{i}_v3.jpg'), hypo_v3)

        # --- 3. Create HYPERTHERMIC images (3 versions) ---
        # Simulate fever by increasing brightness and reducing contrast
        hyper_v1 = np.clip(gray_image * 1.5, 0, 255).astype(np.uint8)
        hyper_v2 = np.clip(gray_image + 50, 0, 255).astype(np.uint8)
        hyper_v3 = cv2.equalizeHist(gray_image) # High contrast heat
        # Make a folder for hyperthermic images
        hyper_folder = os.path.join(OUTPUT_FOLDER, 'Hyperthermic')
        if not os.path.exists(hyper_folder):
            os.makedirs(hyper_folder)
        # Save hyperthermic images in the hyperthermic folder
        cv2.imwrite(os.path.join(hyper_folder, f'hyperthermic_{i}_v1.jpg'), hyper_v1)
        cv2.imwrite(os.path.join(hyper_folder, f'hyperthermic_{i}_v2.jpg'), hyper_v2)
        cv2.imwrite(os.path.join(hyper_folder, f'hyperthermic_{i}_v3.jpg'), hyper_v3)
        print(f"Processed {filename}: Created 9 new images (3 normal, 3 hypothermic, 3 hyperthermic)")
    print(f"Success! Generated {len(image_files) * 9} new images in the '{OUTPUT_FOLDER}' folder.")

    # Now split the generated images into train/test/validation sets
   

import shutil
import random

def split_dataset(class_folder, output_base, train_ratio=0.8, test_ratio=0.1, val_ratio=0.1):
    images = [f for f in os.listdir(class_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    random.shuffle(images)
    n = len(images)
    n_train = int(n * train_ratio)
    n_test = int(n * test_ratio)
    n_val = n - n_train - n_test
    splits = {
        'Train': images[:n_train],
        'Test': images[n_train:n_train+n_test],
        'Validation': images[n_train+n_test:]
    }
    print(f"\nSplitting images into train/test/validation sets for {os.path.basename(class_folder)}...")
    random.seed(42)
    for split, files in splits.items():
        split_dir = os.path.join(output_base, split)
        if not os.path.exists(split_dir):
            os.makedirs(split_dir)
        for fname in files:
            src = os.path.join(class_folder, fname)
            dst = os.path.join(split_dir, fname)
            shutil.copy2(src, dst)
    print(f"{os.path.basename(class_folder)}: {n} images split into {n_train} train, {n_test} test, {n_val} validation.")
    print(f"Splitting images into train/test/validation sets...")
    random.seed(42)
    for cls in ['Normal', 'Hypothermic', 'Hyperthermic']:       
        class_folder = os.path.join(OUTPUT_FOLDER, cls)
        if os.path.isdir(class_folder):
            split_dataset(class_folder, class_folder)
        else:
            print(f"Class folder not found: {class_folder}")
    print("\nSplitting images into train/test/validation sets...")
    random.seed(42)
    for cls in ['Normal', 'Hypothermic', 'Hyperthermic']:
        class_folder = os.path.join(OUTPUT_FOLDER, cls)
        if os.path.isdir(class_folder):
            split_dataset(class_folder, class_folder)
        else:
            print(f"Class folder not found: {class_folder}")
    for split, files in splits.items():
        split_dir = os.path.join(output_base, split)
        if not os.path.exists(split_dir):
            os.makedirs(split_dir)
        for fname in files:
            src = os.path.join(class_folder, fname)
            dst = os.path.join(split_dir, fname)
            shutil.copy2(src, dst)
    print(f"{os.path.basename(class_folder)}: {n} images split into {n_train} train, {n_test} test, {n_val} validation.")
      