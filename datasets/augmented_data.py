import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define dataset folder
dataset_folder = "dataset"  # Folder containing original images

# Image augmentation setup
datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest",
)

# Load images
image_files = [f for f in os.listdir(dataset_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

for image_file in image_files:
    image_path = os.path.join(dataset_folder, image_file)
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB

    # Reshape for ImageDataGenerator
    image = np.expand_dims(image, axis=0)

    # Generate augmented images
    aug_iter = datagen.flow(image, batch_size=1)

    # Save a few augmented images per original image
    for i in range(3):  # Generate 3 augmented versions per image
        aug_image = next(aug_iter)[0].astype(np.uint8)
        aug_filename = f"{os.path.splitext(image_file)[0]}_aug_{i}.jpg"
        aug_path = os.path.join(dataset_folder, aug_filename)
        cv2.imwrite(aug_path, cv2.cvtColor(aug_image, cv2.COLOR_RGB2BGR))

print("Augmentation complete! Augmented images saved in the same folder.")
