import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image in grayscale
image = cv2.imread('Screenshot 2024-10-30 124752.jpeg', 0)
# Perform Histogram Equalization
equalized_image = cv2.equalizeHist(image)
# Calculate the histogram of the equalized image
equalized_histogram = cv2.calcHist([equalized_image], [0], None, [256], [0,256])
# Display the original and equalized image side by side
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(2, 2, 2)
plt.plot('histogram')
plt.title('Original Histogram')
plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.subplot(2, 2, 4)
plt.plot(equalized_histogram)
plt.title('Equalized Histogram')
plt.show()
