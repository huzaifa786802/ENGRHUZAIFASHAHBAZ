import cv2
import numpy as np
# Load the image
image = cv2.imread("OEL-Image-3.jpg")
# Convert the image to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply Otsu's thresholding
_, thresholded_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# Define a kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)  # You can change the size of the kernel based on requirements
# Perform Erosion
erosion = cv2.erode(thresholded_image, kernel, iterations=1)
# Perform Dilation
dilation = cv2.dilate(thresholded_image, kernel, iterations=1)
# Perform Opening (Erosion followed by Dilation)
opening = cv2.morphologyEx(thresholded_image, cv2.MORPH_OPEN, kernel)
# Perform Closing (Dilation followed by Erosion)
closing = cv2.morphologyEx(thresholded_image, cv2.MORPH_CLOSE, kernel)
# Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", grayscale_image)
cv2.imshow("Thresholded Image", thresholded_image)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()