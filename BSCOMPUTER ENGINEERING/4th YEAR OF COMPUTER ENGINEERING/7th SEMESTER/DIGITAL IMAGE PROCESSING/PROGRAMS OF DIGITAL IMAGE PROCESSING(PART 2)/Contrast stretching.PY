import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image_path = '/mnt/data/Screenshot 2024-10-26 114803.jpg'
image = cv2.imread(image_path, 0)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image. Check the file path or file integrity.")
else:
    # Calculate minimum and maximum pixel values
    r_min, r_max = np.min(image), np.max(image)

    # Perform contrast stretching
    contrast_stretched = (image - r_min) * (255 / (r_max - r_min))
    contrast_stretched = np.array(contrast_stretched, dtype=np.uint8)

    # Display the results
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.imshow(contrast_stretched, cmap='gray')
    plt.title('Contrast Stretching')
    plt.tight_layout()
    plt.show()
