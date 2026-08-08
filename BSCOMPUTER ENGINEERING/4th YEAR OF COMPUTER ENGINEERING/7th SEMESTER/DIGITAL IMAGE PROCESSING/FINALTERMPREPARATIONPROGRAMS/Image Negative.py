import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image in grayscale
image = cv2.imread('download.jpeg', 0)
# Perform negative transformation
negative_image1 = 255 - image
# Perform negative operation using cv2.bitwise_not()
negative_image2 = cv2.bitwise_not(image)
# Display original and negative image
plt.subplot(3, 1, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.subplot(3, 1, 2)
plt.title('Negative Image After subtracting from L=255')
plt.imshow(negative_image1, cmap='gray')
plt.subplot(3, 1, 3)
plt.title('Negative Image using cv2.bitwise_not()')
plt.imshow(negative_image2, cmap='gray')
plt.tight_layout()
plt.show()