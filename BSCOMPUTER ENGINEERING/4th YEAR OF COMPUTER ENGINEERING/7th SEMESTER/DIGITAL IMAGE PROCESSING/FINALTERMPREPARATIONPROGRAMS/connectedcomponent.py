import cv2
import numpy as np
# Load the uploaded image
image_path = '/mnt/data/Screenshot 2024-10-10 211014.jpg'
image = cv2.imread(image_path)
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply a binary threshold to the image (convert to black & white)
ret, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
# Find contours (connected components)
contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Create a blank image with the same shape as the original to draw contours with random colors
image_with_colored_contours = np.zeros_like(image)
# Loop through each contour and draw it with a random color
for contour in contours:
    color = np.random.randint(0, 255, size=3).tolist()  # Generate a random color
    cv2.drawContours(image_with_colored_contours, [contour], -1, color, 3)  # Draw contour with random color
# Total number of detected objects (contours)
total_objects = len(contours)
# Display the results
cv2.imshow('Image with Colored Contours', image_with_colored_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Print the total number of objects detected
print(f"Total number of objects detected: {total_objects}")