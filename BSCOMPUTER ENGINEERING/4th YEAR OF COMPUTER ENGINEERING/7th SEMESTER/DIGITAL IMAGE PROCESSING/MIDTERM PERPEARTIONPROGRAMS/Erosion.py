import cv2
import numpy as np
import matplotlib.pyplot as plt
def load_and_process_image(image_path):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Convert to binary (if not already)
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return binary
def perform_erosion(image, kernel_size=3, iterations=1):
    # Create kernel for erosion
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    # Perform erosion
    eroded = cv2.erode(image, kernel, iterations=iterations)
    return eroded
def display_results(original, eroded):
    # Create figure with two subplots
    plt.figure(figsize=(10, 5))    
    # Display original image
    plt.subplot(121)
    plt.imshow(original, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    # Display eroded image
    plt.subplot(122)
    plt.imshow(eroded, cmap='gray')
    plt.title('Eroded Image')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
# Main execution
def main():
    # Load and process the image
    image_path = 'Erosion.jpg'  # Replace with your image path
    original = load_and_process_image(image_path)
    # Perform erosion
    # Using kernel_size=5 and iterations=2 to ensure separation
    eroded = perform_erosion(original, kernel_size=5, iterations=2)
    # Display results
    display_results(original, eroded)
if __name__ == "__main__":
    main()