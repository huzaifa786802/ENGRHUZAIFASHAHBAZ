import cv2
import numpy as np
# Load the image in grayscale
image = cv2.imread('contrast_image.jpg', cv2.IMREAD_GRAYSCALE)
# Calculate the mean pixel value of the image
mean_val = np.mean(image)
# Transformation (a): Less than mean -> 0, Greater than mean -> 255
transformation_a = np.where(image < mean_val, 0, 255).astype(np.uint8)
# Transformation (b): Less than mean -> 255, Greater than mean -> 0
transformation_b = np.where(image < mean_val, 255, 0).astype(np.uint8)
# Transformation (c): Within ±20 of mean -> 0, Otherwise -> 255
tolerance = 20
transformation_c = np.where((image >= mean_val - tolerance) & (image <= mean_val + tolerance), 0, 255).astype(np.uint8)
# Save the transformed images
cv2.imwrite('transformation_a.jpg', transformation_a)
cv2.imwrite('transformation_b.jpg', transformation_b)
cv2.imwrite('transformation_c.jpg', transformation_c)
# Display the transformed images
cv2.imshow('Transformation A', transformation_a)
cv2.imshow('Transformation B', transformation_b)
cv2.imshow('Transformation C', transformation_c)
cv2.waitKey(0)
cv2.destroyAllWindows()
