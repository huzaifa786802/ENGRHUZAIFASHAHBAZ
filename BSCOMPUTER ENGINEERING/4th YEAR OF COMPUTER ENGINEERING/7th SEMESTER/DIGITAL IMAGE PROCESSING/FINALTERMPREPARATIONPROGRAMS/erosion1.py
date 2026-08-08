import cv2
import numpy as np
import matplotlib.pyplot as plt
def process_fingerprint(image):
    """
    Process fingerprint image using erosion followed by dilation
    Returns original, eroded and final processed images
    """
    # Convert to grayscale if the image has multiple channels
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Create kernel for morphological operations
    kernel = np.ones((3,3), np.uint8)
    # Perform erosion
    eroded = cv2.erode(image, kernel, iterations=1)
    # Perform dilation on the eroded image
    processed = cv2.dilate(eroded, kernel, iterations=1)
    return image, eroded, processed
def display_results(original, eroded, processed):
    """
    Display the original, eroded, and final processed images side by side
    """
    plt.figure(figsize=(15,5))
    plt.subplot(131)
    plt.imshow(original, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    plt.subplot(132)
    plt.imshow(eroded, cmap='gray')
    plt.title('After Erosion')
    plt.axis('off')
    plt.subplot(133)
    plt.imshow(processed, cmap='gray')
    plt.title('After Dilation (Final)')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
# Main execution
if __name__ == "__main__":
    # Read the image
    image = cv2.imread('fingerprint.jpg')
    # Process the image
    original, eroded, processed = process_fingerprint(image)
    # Display results
    display_results(original, eroded, processed)
    # Save the processed image
    cv2.imwrite('processed_fingerprint.jpg', processed)