import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load the images
img_hist = cv2.imread('/mnt/data/hist2.jpg', cv2.IMREAD_GRAYSCALE)
img_contrast = cv2.imread('/mnt/data/high_contrast.png', cv2.IMREAD_GRAYSCALE)
# Function for histogram equalization
def histogram_equalization(image):
    equalized_img = cv2.equalizeHist(image)
    return equalized_img
# Function for contrast adjustment using CLAHE (Contrast Limited Adaptive Histogram Equalization)
def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    cl_img = clahe.apply(image)
    return cl_img
# Apply transformations
hist_equalized_img = histogram_equalization(img_hist)
clahe_img = apply_clahe(img_contrast)
# Save the transformed images
cv2.imwrite('/mnt/data/histogram_equalized_output.jpg', hist_equalized_img)
cv2.imwrite('/mnt/data/clahe_output.png', clahe_img)
# Display the original and transformed images using matplotlib
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.title('Original Histogram Image')
plt.imshow(img_hist, cmap='gray')
plt.subplot(2, 2, 2)
plt.title('Histogram Equalized Image')
plt.imshow(hist_equalized_img, cmap='gray')
plt.subplot(2, 2, 3)
plt.title('Original High Contrast Image')
plt.imshow(img_contrast, cmap='gray')
plt.subplot(2, 2, 4)
plt.title('CLAHE Adjusted Image')
plt.imshow(clahe_img, cmap='gray')
plt.show()