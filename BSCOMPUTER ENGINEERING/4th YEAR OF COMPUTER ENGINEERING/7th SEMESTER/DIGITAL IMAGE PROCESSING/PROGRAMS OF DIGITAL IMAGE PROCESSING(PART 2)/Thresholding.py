import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image in grayscale
image = cv2.imread('Screenshot 2024-10-26 122352.jpeg', 0)
# Apply simple thresholding
# Threshold at 127, values above 127 are set to 255, below are set to 0
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# Apply inverse binary thresholding
_, binary_inv_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
# Display original and thresholded images
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(binary_image, cmap='gray')
plt.title('Binary Thresholding')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(binary_inv_image, cmap='gray')
plt.title('Inverse Binary Thresholding')
plt.axis('off')
plt.tight_layout()
plt.show()