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
        plt.imsave(os.path.join(OUTPUT_FOLDER, f'normal_{i}_v1.jpg'), COLOR_MAP(gray_image))
        # Add slight variations for more data
        normal_v2 = np.clip(gray_image * 1.1, 0, 255).astype(np.uint8)
        plt.imsave(os.path.join(OUTPUT_FOLDER, f'normal_{i}_v2.jpg'), COLOR_MAP(normal_v2))
        normal_v3 = np.clip(gray_image * 0.9, 0, 255).astype(np.uint8)
        plt.imsave(os.path.join(OUTPUT_FOLDER, f'normal_{i}_v3.jpg'), COLOR_MAP(normal_v3))

        # --- 2. Create HYPOTHERMIC images (3 versions) ---
        # Simulate cooling by darkening parts of the image
        hypo_base = gray_image.copy().astype(float)
        rows, cols = hypo_base.shape
        # Version 1: Strong peripheral cooling
        hypo_base[0:int(rows*0.2), :] *= 0.4
        hypo_base[int(rows*0.8):rows, :] *= 0.4
        hypo_base[:, 0:int(cols*0.2)] *= 0.4
        hypo_base[:, int(cols*0.8):cols] *= 0.4
        plt.imsave(os.path.join(OUTPUT_FOLDER, f'hypothermic_{i}_v1.jpg'), COLOR_MAP(np.clip(hypo_base, 0, 255).astype(np.uint8)))
        # Version 2: Moderate cooling
        hypo_v2 = np.clip(hypo_base * 1.1, 0, 255).astype(np.uint8)
        plt.imsave(os.path.join(OUTPUT_FOLDER, f'hypothermic_{i}_v2.jpg'), COLOR_MAP(hypo_v2))
        # Version 3: Less intense cooling
        hypo_v3 = np.clip(hypo_base * 0.9 + 20, 0, 255).astype(np.uint8)
        plt.imsave(os.path.join(OUTPUT_FOLDER, f'hypothermic_{i}_v3.jpg'), COLOR_MAP(hypo_v3))


        # --- 3. Create HYPERTHERMIC images (3 versions) ---
        # Simulate fever by increasing brightness and reducing contrast
        hyper_v1 = np.clip(gray_image * 1.5, 0, 255).astype(np.uint8)
        plt.imsave(os.path.join(OUTPUT_FOLDER, f'hyperthermic_{i}_v1.jpg'), COLOR_MAP(hyper_v1))
        hyper_v2 = np.clip(gray_image + 50, 0, 255).astype(np.uint8)
        plt.imsave(os.path.join(OUTPUT_FOLDER, f'hyperthermic_{i}_v2.jpg'), COLOR_MAP(hyper_v2))
        hyper_v3 = cv2.equalizeHist(gray_image) # High contrast heat
        plt.imsave(os.path.join(OUTPUT_FOLDER, f'hyperthermic_{i}_v3.jpg'), COLOR_MAP(hyper_v3))


    print(f"Success! Generated {len(image_files) * 9} new images in the '{OUTPUT_FOLDER}' folder.")