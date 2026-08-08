import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from collections import Counter
import math
class DifferenceCoding:
    def __init__(self):
        self.original_entropy = None
        self.encoded_entropy = None
    def encode(self, image_array):
        """Apply difference coding to the image."""
        height, width = image_array.shape
        encoded = np.zeros_like(image_array, dtype=np.int16)
        # First pixel remains unchanged
        encoded[0, 0] = image_array[0, 0]
        # Encode first row
        for j in range(1, width):
            encoded[0, j] = int(image_array[0, j]) - int(image_array[0, j-1])
        # Encode first column
        for i in range(1, height):
            encoded[i, 0] = int(image_array[i, 0]) - int(image_array[i-1, 0])
        # Encode rest of the image
        # Using average of left and top pixels as predictor
        for i in range(1, height):
            for j in range(1, width):
                predictor = (int(image_array[i-1, j]) + int(image_array[i, j-1])) // 2
                encoded[i, j] = int(image_array[i, j]) - predictor
        return encoded
    def decode(self, encoded_array):
        """Decode the difference coded image."""
        height, width = encoded_array.shape
        decoded = np.zeros_like(encoded_array, dtype=np.uint8)
        # First pixel remains unchanged
        decoded[0, 0] = encoded_array[0, 0]
        # Decode first row
        for j in range(1, width):
            decoded[0, j] = encoded_array[0, j] + decoded[0, j-1]
        # Decode first column
        for i in range(1, height):
            decoded[i, 0] = encoded_array[i, 0] + decoded[i-1, 0]
        # Decode rest of the image
        for i in range(1, height):
            for j in range(1, width):
                predictor = (int(decoded[i-1, j]) + int(decoded[i, j-1])) // 2
                decoded[i, j] = encoded_array[i, j] + predictor
        return decoded
    def calculate_entropy(self, array):
        """Calculate entropy of the array."""
        counter = Counter(array.flatten())
        total_pixels = array.size
        entropy = 0
        for count in counter.values():
            probability = count / total_pixels
            entropy -= probability * math.log2(probability)
        return entropy
    def analyze_redundancy(self, image_path):
        """Analyze redundancy reduction after difference coding."""
        # Read and convert image to grayscale
        image = Image.open(image_path).convert('L')
        image_array = np.array(image)
        # Apply difference coding
        encoded_array = self.encode(image_array)
        # Calculate entropies
        self.original_entropy = self.calculate_entropy(image_array)
        self.encoded_entropy = self.calculate_entropy(encoded_array)
        # Calculate redundancy reduction
        redundancy_reduction = ((self.original_entropy - self.encoded_entropy) / 
                              self.original_entropy * 100)
        # Create visualization
        plt.figure(figsize=(15, 5))
        # Original image histogram
        plt.subplot(131)
        plt.hist(image_array.flatten(), bins=256, range=(0, 256), density=True)
        plt.title('Original Image Histogram')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
        # Difference coded histogram
        plt.subplot(132)
        plt.hist(encoded_array.flatten(), bins=256, density=True)
        plt.title('Difference Coded Histogram')
        plt.xlabel('Difference Value')
        plt.ylabel('Frequency')
        # Decoded image
        decoded_array = self.decode(encoded_array)
        plt.subplot(133)
        plt.imshow(decoded_array, cmap='gray')
        plt.title('Decoded Image')
        plt.axis('off')
        plt.tight_layout()
        # Print analysis results
        print("\nRedundancy Analysis:")
        print(f"Original Entropy: {self.original_entropy:.2f} bits/pixel")
        print(f"Encoded Entropy: {self.encoded_entropy:.2f} bits/pixel")
        print(f"Redundancy Reduction: {redundancy_reduction:.2f}%")
        # Calculate value range statistics
        original_range = np.ptp(image_array)
        encoded_range = np.ptp(encoded_array)
        print(f"\nValue Range Analysis:")
        print(f"Original Range: {original_range}")
        print(f"Encoded Range: {encoded_range}")
        # Calculate standard deviations
        original_std = np.std(image_array)
        encoded_std = np.std(encoded_array)
        print(f"\nStandard Deviation Analysis:")
        print(f"Original Std Dev: {original_std:.2f}")
        print(f"Encoded Std Dev: {encoded_std:.2f}")
        return {
            'original_entropy': self.original_entropy,
            'encoded_entropy': self.encoded_entropy,
            'redundancy_reduction': redundancy_reduction,
            'original_array': image_array,
            'encoded_array': encoded_array,
            'decoded_array': decoded_array
        }
# Example usage
if __name__ == "__main__":
    # Replace with your image path
    image_path = "differencecoding.jpg"
    difference_coder = DifferenceCoding()
    results = difference_coder.analyze_redundancy(image_path)
    plt.show()