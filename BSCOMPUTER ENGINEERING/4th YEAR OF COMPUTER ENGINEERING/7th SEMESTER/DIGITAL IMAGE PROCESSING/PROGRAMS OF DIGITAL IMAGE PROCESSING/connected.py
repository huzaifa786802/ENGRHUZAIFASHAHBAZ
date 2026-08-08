import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
image_path = '/mnt/data/Screenshot 2024-10-10 211625.jpg'
image = cv2.imread(image_path)
# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply thresholding to create a binary image
_, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
# Apply connected component analysis
num_labels, labels = cv2.connectedComponents(binary)
# Display the result
plt.figure(figsize=(10,10))
plt.imshow(labels, cmap='nipy_spectral')
plt.title(f'Total Colored Objects: {num_labels - 1}')  # Subtract 1 to exclude the background
plt.show()
# Print the total number of objects
print(f'Total number of colored objects: {num_labels - 1}')  # Exclude background