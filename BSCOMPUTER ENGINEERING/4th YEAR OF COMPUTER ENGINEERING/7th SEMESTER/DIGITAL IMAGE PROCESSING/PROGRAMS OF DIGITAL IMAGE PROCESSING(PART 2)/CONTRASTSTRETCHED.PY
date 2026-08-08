import cv2
import numpy as np
# Load the image
image = cv2.imread('Screenshot 2024-10-26 200104.jpg', cv2.IMREAD_GRAYSCALE)
# Enhance contrast
enhanced_image = cv2.equalizeHist(image)
# Calculate the mean pixel value
mean = np.mean(enhanced_image)
# Apply the transformation
# Option a)
transformed_image_a = np.where(enhanced_image < mean, 0, 255).astype(np.uint8)
# Option b)
transformed_image_b = np.where(enhanced_image < mean, 255, 0).astype(np.uint8)
# Option c)
transformed_image_c = np.where(np.abs(enhanced_image - mean) <= 20, 0, 255).astype(np.uint8)
# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Enhanced Image', enhanced_image)
cv2.imshow('Transformed Image (Option a)', transformed_image_a)
cv2.imshow('Transformed Image (Option b)', transformed_image_b)
cv2.imshow('Transformed Image (Option c)', transformed_image_c)
cv2.waitKey(0)
cv2.destroyAllWindows()