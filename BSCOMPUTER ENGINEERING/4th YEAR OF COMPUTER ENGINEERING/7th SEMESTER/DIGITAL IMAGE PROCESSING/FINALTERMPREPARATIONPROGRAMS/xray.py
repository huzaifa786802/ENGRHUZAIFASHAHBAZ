import cv2
import matplotlib.pyplot as plt
import numpy as np
# Load the image
image = cv2.imread('x-ray.jpg', cv2.IMREAD_GRAYSCALE)
# Apply histogram equalization
equalized_image = cv2.equalizeHist(image)
# Calculate histograms using numpy
hist_original, bin_edges_original = np.histogram(image.flatten(),
bins=256, range=[0, 256])
hist_equalized, bin_edges_equalized =np.histogram(equalized_image.flatten(), bins=256, range=[0, 256])
# Display the original and equalized images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')
plt.show()
# Plot the histograms
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(bin_edges_original[1:], hist_original, color='black')
plt.title('Original Image Histogram')
plt.subplot(1, 2, 2)
plt.plot(bin_edges_equalized[1:], hist_equalized, color='black')
plt.title('Equalized Image Histogram')
plt.show()