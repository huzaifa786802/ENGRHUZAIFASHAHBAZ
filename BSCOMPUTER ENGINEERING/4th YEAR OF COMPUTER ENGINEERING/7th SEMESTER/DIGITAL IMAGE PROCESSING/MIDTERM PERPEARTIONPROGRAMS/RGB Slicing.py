import cv2
import numpy as np
import matplotlib.pyplot as plt
# Read the RGB image
image = cv2.imread('RGB Slicing.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert BGR to RGB
plt.figure()
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')
w = 140
a = np.array([30, 30, 30])
# Create a copy of the image for modification
sliced_image = image.copy()
# Vectorized approach for RGB slicing
diff = np.abs(image - a) # Calculate absolute differences for all pixels
mask = np.any(diff > w / 2, axis=-1) # Check if any channel exceeds w/2
sliced_image[mask] = 128 # Set gray value for pixels that match the condition
# Display the result
plt.figure()
plt.imshow(sliced_image)
plt.title("RGB Sliced Image (Optimized)")
plt.axis('off')
plt.show()