from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np
# Load the uploaded image
image_path = 'OEL-Image-4.jpg'
image = cv2.imread(image_path)
# Convert to grayscale for edge detection
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply Sobel Edge Detection
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
sobel_edge = cv2.magnitude(sobel_x, sobel_y)
# Apply Canny Edge Detection
canny_edges = cv2.Canny(gray_image, 100, 200)
# Display the results
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
# Original Image
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')
axs[0].axis('off')
# Sobel Edge Detection
axs[1].imshow(sobel_edge, cmap='gray')
axs[1].set_title('Sobel Edge Detection')
axs[1].axis('off')
# Canny Edge Detection
axs[2].imshow(canny_edges, cmap='gray')
axs[2].set_title('Canny Edge Detection')
axs[2].axis('off')
plt.tight_layout()
plt.show()