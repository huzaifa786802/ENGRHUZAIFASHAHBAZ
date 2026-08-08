# Import necessary libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load the grayscale image
image_path = 'Erosion.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# Check if the image is loaded properly
if image is None:
    print("Error: Could not load the image. Check the file path.")
else:
    # Convert the grayscale image to binary
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    # Define the structuring element (e.g., a 3x3 rectangular kernel)
    structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # Perform erosion on the binary image
    eroded_image = cv2.erode(binary_image, structuring_element, iterations=1)
    # Display the original binary image and the eroded image
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original  Image")
    plt.imshow(binary_image, cmap="gray")
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.title("Eroded Image")
    plt.imshow(eroded_image, cmap="gray")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
