import numpy as np
import matplotlib.pyplot as plt
# Function to generate the image with sine wave pattern
def generate_sine_image(frequency, size=256):
    image = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            image[i, j] = np.sin(2 * np.pi * frequency * (i + j))
    return image
# Function to display the images with different frequencies
def plot_images(frequencies, size=256):
    plt.figure(figsize=(15, 5))
    for idx, freq in enumerate(frequencies):
        plt.subplot(1, len(frequencies), idx + 1)
        image = generate_sine_image(freq, size)
        plt.imshow(image, cmap='gray', extent=(0, size, 0, size))
        plt.title(f"Frequency = {freq}")
        plt.axis('off')
    plt.show()
# Ask user for frequencies
frequencies = [float(x) for x in input("Enter frequencies separated by spaces: ").split()]
# Generate and display the images
plot_images(frequencies)