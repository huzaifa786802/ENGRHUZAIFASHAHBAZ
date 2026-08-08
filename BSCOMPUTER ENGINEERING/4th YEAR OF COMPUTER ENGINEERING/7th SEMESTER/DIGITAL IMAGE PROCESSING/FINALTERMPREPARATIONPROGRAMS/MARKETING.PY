import cv2
import numpy as np
# Load the image
image = cv2.imread('marketing.jpg')
# Convert the image from BGR to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Define the lower and upper bounds for the blue color in HSV
lower_blue = np.array([100, 0, 0])
upper_blue = np.array([130, 255, 255])
# Create a mask using the defined color range
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
# Bitwise-AND mask and original image to extract blue areas
extracted_blue = cv2.bitwise_and(image, image, mask=mask)
# Display the original image and the extracted blue areas
cv2.imshow('Original Image', image)
cv2.imshow('Extracted Blue Letters', extracted_blue)
# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()