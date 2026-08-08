import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load the image
image_path = "MORPHOLOGICALTRANSLATION.jpg"
image = cv2.imread(image_path, 0)  # Read as grayscale
# Define a kernel
kernel = np.ones((5, 5), np.uint8)
# Perform morphological operations
erosion = cv2.erode(image, kernel, iterations=1)
dilation = cv2.dilate(image, kernel, iterations=1)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
# Display the results
titles = ['Original Image', 'Erosion', 'Dilation', 'Opening', 'Closing']
images = [image, erosion, dilation, opening, closing]
plt.figure(figsize=(10, 10))
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()