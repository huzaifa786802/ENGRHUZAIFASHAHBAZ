# Import necessary libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image_path = 'Fitting and Hitting.jpg'
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create binary thresholded image for morphological operations
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Define a small structuring element
structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Perform morphological fitting (erosion to check full fit)
fitting_result = cv2.erode(binary_image, structuring_element)

# Perform morphological hitting (dilation to check partial overlap)
hitting_result = cv2.dilate(binary_image, structuring_element)

# Display the original, fitting, and hitting results
plt.figure(figsize=(15, 6))
plt.subplot(1, 3, 1)
plt.title("Original Binary Image")
plt.imshow(binary_image, cmap="gray")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Fitting Result (Erosion)")
plt.imshow(fitting_result, cmap="gray")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Hitting Result (Dilation)")
plt.imshow(hitting_result, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()
