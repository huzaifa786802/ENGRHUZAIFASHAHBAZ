import cv2
import matplotlib.pyplot as plt
import numpy as np
def bit_plane_slicing(image):
    # Get image dimensions
    rows, cols = image.shape
    # Initialize list to store bit planes
    bit_planes = []
    # Extract each bit plane
    for bit in range(8):
        # Use bitwise AND with 1 shifted left by 'bit' positions
        # Then shift right by 'bit' positions to get binary image
        bit_plane = (image & (1 << bit)) >> bit
        bit_planes.append(bit_plane)
    return bit_planes
def display_bit_planes(image_path):
    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Check if image was successfully loaded
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return
    # Get bit planes
    bit_planes = bit_plane_slicing(image)
    # Create figure for displaying results
    plt.figure(figsize=(15, 8))
    # Display original image
    plt.subplot(2, 5, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    # Display each bit plane
    for i, plane in enumerate(bit_planes):
        plt.subplot(2, 5, i + 3)
        plt.imshow(plane, cmap='gray')
        plt.title(f'Bit Plane {i}')
        plt.axis('off')
    # Adjust layout and display
    plt.tight_layout()
    plt.show()
# Example usage
if __name__ == "__main__":
    # Replace with your image path
    image_path = "Bit Plane Coding.jpg"
    display_bit_planes(image_path)