import numpy as np
from collections import defaultdict
import heapq
from PIL import Image
import os
class HuffmanNode:
    def __init__(self, pixel=None, freq=None):
        self.pixel = pixel
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
class HuffmanImageCompression:
    def __init__(self):
        self.codes = {}
        self.reverse_codes = {}
    def calculate_frequency(self, image_array):
        """Calculate frequency of each pixel value in the image."""
        frequency = defaultdict(int)
        for pixel in image_array.flatten():
            frequency[pixel] += 1
        return frequency
    def build_huffman_tree(self, frequency):
        """Build Huffman tree using priority queue."""
        priority_queue = []
        # Create leaf nodes for each pixel value
        for pixel, freq in frequency.items():
            node = HuffmanNode(pixel, freq)
            heapq.heappush(priority_queue, node)
        # Build the tree
        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            internal_node = HuffmanNode()
            internal_node.freq = left.freq + right.freq
            internal_node.left = left
            internal_node.right = right
            heapq.heappush(priority_queue, internal_node)
        return priority_queue[0]
    def generate_codes(self, root, code=""):
        """Generate Huffman codes for each pixel value."""
        if root is None:
            return
        if root.pixel is not None:
            self.codes[root.pixel] = code
            self.reverse_codes[code] = root.pixel
            return
        self.generate_codes(root.left, code + "0")
        self.generate_codes(root.right, code + "1")
    def compress(self, image_path):
        """Compress the image using Huffman coding."""
        # Read image
        image = Image.open(image_path).convert('L')  # Convert to grayscale
        image_array = np.array(image)
        # Calculate frequencies
        frequency = self.calculate_frequency(image_array)
        # Build Huffman tree and generate codes
        root = self.build_huffman_tree(frequency)
        self.generate_codes(root)
        # Encode image
        encoded_image = ""
        for pixel in image_array.flatten():
            encoded_image += self.codes[pixel]
        # Calculate compression statistics
        original_size = image_array.size * 8  # 8 bits per pixel
        compressed_size = len(encoded_image)
        compression_ratio = original_size / compressed_size
        return {
            'encoded_data': encoded_image,
            'codes': self.codes,
            'original_size': original_size,
            'compressed_size': compressed_size,
            'compression_ratio': compression_ratio
        }
    def decompress(self, encoded_data, shape):
        """Decompress the encoded image data."""
        current_code = ""
        decoded_pixels = []
        for bit in encoded_data:
            current_code += bit
            if current_code in self.reverse_codes:
                decoded_pixels.append(self.reverse_codes[current_code])
                current_code = ""
        # Reshape back to original image dimensions
        decoded_array = np.array(decoded_pixels, dtype=np.uint8).reshape(shape)
        return decoded_array
# Example usage and analysis
def analyze_compression(image_path):
    """Analyze the compression efficiency for a given image."""
    compressor = HuffmanImageCompression()
    # Compress the image
    compression_results = compressor.compress(image_path)
    # Calculate compression statistics
    original_size_kb = compression_results['original_size'] / 8000  # Convert bits to KB
    compressed_size_kb = compression_results['compressed_size'] / 8000
    compression_ratio = compression_results['compression_ratio']
    space_saving = (1 - 1/compression_ratio) * 100
    # Print analysis
    print(f"\nCompression Analysis for {os.path.basename(image_path)}:")
    print(f"Original Size: {original_size_kb:.2f} KB")
    print(f"Compressed Size: {compressed_size_kb:.2f} KB")
    print(f"Compression Ratio: {compression_ratio:.2f}:1")
    print(f"Space Saving: {space_saving:.2f}%")
    return compression_results
# Usage example:
if __name__ == "__main__":
    # Replace with your image path
    image_path = "huffmancoding.jpg"
    results = analyze_compression(image_path)