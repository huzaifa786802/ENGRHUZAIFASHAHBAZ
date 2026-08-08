import numpy as np
import cv2
import matplotlib.pyplot as plt
def standard_quantization(image, bits):
    levels = 2 ** bits
    quantized_image = np.floor(image / (256 / levels)) * (256 / levels)
    return quantized_image.astype(np.uint8)
def igs_quantization(image, bits):
    levels = 2 ** bits
    quantized_image = np.zeros_like(image, dtype=np.uint8)
    error = 0
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            pixel_value = image[row, col]
            new_value = (pixel_value + error) // (256 // levels) * (256 // levels)
            error = pixel_value + error - new_value
            quantized_image[row, col] = new_value
    return quantized_image
def plot_images(original, quantized_images, title_prefix):
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 3, 1)
    plt.imshow(original, cmap='gray')
    plt.title("Original")
    plt.axis('off')
    for i, (bits, q_image) in enumerate(quantized_images):
        plt.subplot(2, 3, i + 2)
        plt.imshow(q_image, cmap='gray')
        plt.title(f"{title_prefix} {bits}-bit")
        plt.axis('off')
    plt.tight_layout()
    plt.show()
# Load the grayscale image
image_path = ('APPLEANDTREE.jpg')
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    raise ValueError("Image not found or not readable.")
# Perform quantization
bit_depths = [4, 6, 8, 16]
standard_quantized_images = [(bits, standard_quantization(image, bits)) for bits in bit_depths]
igs_quantized_images = [(bits, igs_quantization(image, bits)) for bits in bit_depths]
# Plot results
plot_images(image, standard_quantized_images, "Standard Quantization")
plot_images(image, igs_quantized_images, "IGS Quantization")