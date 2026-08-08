import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image_path = '/mnt/data/image.png'  # Path to the image you uploaded
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply contrast stretching by setting 5th and 95th percentiles
min_val, max_val = np.percentile(image, (5, 95))

# Contrast stretching
stretched_image = np.clip((image - min_val) * 255.0 / (max_val - min_val), 0, 255).astype(np.uint8)

# Display original and contrast-stretched images
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Contrast-stretched image
plt.subplot(1, 2, 2)
plt.imshow(stretched_image, cmap='gray')
plt.title('Contrast Stretched Image')
plt.axis('off')

plt.tight_layout()
plt.show()
