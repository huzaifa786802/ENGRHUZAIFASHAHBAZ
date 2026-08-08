import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
image_path = 'OEL-Image-2.jpg'  # Path to your uploaded image
image = cv2.imread(image_path)
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply Histogram Equalization
hist_eq_image = cv2.equalizeHist(gray_image)
# Apply Gaussian Blur for smoothing
smoothed_image = cv2.GaussianBlur(hist_eq_image, (5, 5), 0)
# Apply a sharpening filter
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
sharpened_image = cv2.filter2D(smoothed_image, -1, kernel)
# Plot the results
plt.figure(figsize=(12, 8))
plt.subplot(1, 4, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.subplot(1, 4, 2)
plt.title('Histogram Equalized')
plt.imshow(hist_eq_image, cmap='gray')
plt.axis('off')
plt.subplot(1, 4, 3)
plt.title('Smoothed Image')
plt.imshow(smoothed_image, cmap='gray')
plt.axis('off')
plt.subplot(1, 4, 4)
plt.title('Sharpened Image')
plt.imshow(sharpened_image, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()
# Save the processed images
cv2.imwrite('/mnt/data/histogram_equalized.png', hist_eq_image)
cv2.imwrite('/mnt/data/smoothed_image.png', smoothed_image)
cv2.imwrite('/mnt/data/sharpened_image.png', sharpened_image)