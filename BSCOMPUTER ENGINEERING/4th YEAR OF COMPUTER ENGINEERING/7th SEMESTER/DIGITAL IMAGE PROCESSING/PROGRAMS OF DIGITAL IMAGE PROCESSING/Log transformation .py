import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image in grayscale
image = cv2.imread('download.jpeg', 0)
c = 255 / np.log(1 + np.max(image))
log_transformed = c * (np.log(1 + image))
# Normalize to [0, 255]
log_transformed = np.array(log_transformed, dtype=np.uint8)
# Display the result
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(log_transformed, cmap='gray')
plt.title('Log Transformation')
plt.tight_layout()
plt.show()