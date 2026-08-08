import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image in grayscale
image = cv2.imread('download.jpeg', 0)
r_min, r_max = np.min(image), np.max(image)
contrast_stretched = (image - r_min) * (255 / (r_max - r_min))
# Normalize to [0, 255]
contrast_stretched = np.array(contrast_stretched, dtype=np.uint8)
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
# Display the result
plt.subplot(1, 2, 2)
plt.imshow(contrast_stretched, cmap='gray')
plt.title('Contrast Stretching')
plt.tight_layout()
plt.show()