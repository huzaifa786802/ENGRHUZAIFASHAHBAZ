# Import necessary libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load the image uploaded by the user
image_path = 'MORPHOLOGICALreflection.jpg'
image = cv2.imread(image_path, cv2.IMREAD_COLOR)
# Convert the image to grayscale for morphological operations
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Define a structuring element for morphological reflection
structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# Apply morphological reflection (dilation followed by erosion)
dilated_image = cv2.dilate(gray_image, structuring_element)
eroded_image = cv2.erode(dilated_image, structuring_element)
# Display the original and processed images
plt.figure(figsize=(10, 8))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.subplot(1, 2, 2)
plt.title("Morphological Reflection")
plt.imshow(eroded_image, cmap="gray")
plt.axis("off")
plt.tight_layout()
plt.show()