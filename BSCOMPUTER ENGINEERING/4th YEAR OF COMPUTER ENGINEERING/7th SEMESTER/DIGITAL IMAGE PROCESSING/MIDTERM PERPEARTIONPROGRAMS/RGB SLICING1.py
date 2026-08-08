import cv2
import numpy as np
import matplotlib.pyplot as plt
# Read the RGB image
image = cv2.imread('RGB Slicing.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert BGR to RGB for correct visualization
# Display the original image
plt.figure()
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')
# Create a copy of the image for modification
modified_image = image.copy()
# Vectorized approach
mask = (image[:, :, 1] > 40) & (image[:, :, 2] > 40) # Condition for green and blue channels
modified_image[mask] = 58 # Apply the gray value to pixels that satisfy the condition
# Display the modified image
plt.figure()
plt.imshow(modified_image)
plt.title("Modified Image (Optimized)")
plt.axis('off')
plt.show()