import cv2
import numpy as np
import matplotlib.pyplot as plt
def perform_morphological_operations(image_path):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Create a 3x3 kernel
    kernel = np.ones((3,3), np.uint8)
    # Perform dilation
    dilation = cv2.dilate(img, kernel, iterations=1)
    # Perform erosion
    erosion = cv2.erode(img, kernel, iterations=1)
    # Morphological gradient (dilation - erosion)
    morph_gradient = cv2.subtract(dilation, erosion)
    # Top-hat operation (original - opening)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    tophat = cv2.subtract(img, opening)
    # Create subplots to display results
    plt.figure(figsize=(15, 10))
    plt.subplot(2, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    plt.subplot(2, 3, 2)
    plt.imshow(dilation, cmap='gray')
    plt.title('Dilation')
    plt.axis('off')
    plt.subplot(2, 3, 3)
    plt.imshow(erosion, cmap='gray')
    plt.title('Erosion')
    plt.axis('off')
    plt.subplot(2, 3, 4)
    plt.imshow(morph_gradient, cmap='gray')
    plt.title('Morphological Gradient')
    plt.axis('off')
    plt.subplot(2, 3, 5)
    plt.imshow(tophat, cmap='gray')
    plt.title('Top-hat')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    return dilation, erosion, morph_gradient, tophat
# To use this function:
image_path = 'Grayscale Morphological Operations.jpg'
dilation, erosion, gradient, tophat = perform_morphological_operations(image_path)