import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('image.jpg', 0)

# Calculate the mean of the image
mean = np.mean(img)

# Apply the transformation
# a) Less than mean - 0, Greater than mean - 255
img_a = np.where(img < mean, 0, 255)

# b) Less than mean - 255, Greater than mean - 0
img_b = np.where(img < mean, 255, 0)

# c) ±20 mean - 0, Otherwise - 255
img_c = np.where(np.abs(img - mean) <= 20, 0, 255)

# Display the original and transformed images
plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.imshow(img_a, cmap='gray')
plt.title('Transformation a)')

plt.subplot(2, 2, 3)
plt.imshow(img_b, cmap='gray')
plt.title('Transformation b)')

plt.subplot(2, 2, 4)
plt.imshow(img_c, cmap='gray')
plt.title('Transformation c)')

plt.show()