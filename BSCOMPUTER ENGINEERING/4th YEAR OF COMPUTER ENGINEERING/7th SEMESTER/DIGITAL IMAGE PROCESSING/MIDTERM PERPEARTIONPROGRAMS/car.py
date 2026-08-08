import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
image = cv2.imread('car.jpg', cv2.IMREAD_GRAYSCALE)#Gaussian Blur filtering image
# Apply Gaussian Blur
smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)
# Display the original and smoothed images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Smoothed Image')
plt.imshow(smoothed_image, cmap='gray')
plt.axis('off')
plt.show()