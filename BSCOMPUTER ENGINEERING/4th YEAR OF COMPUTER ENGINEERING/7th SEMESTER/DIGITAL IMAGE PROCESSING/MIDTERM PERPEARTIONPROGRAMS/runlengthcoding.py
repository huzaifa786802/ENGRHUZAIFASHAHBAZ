import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from typing import List, Tuple
import time
class BinaryRLC:
    def __init__(self, threshold: int = 127):
        self.threshold = threshold
    def convert_to_binary(self, image_path: str) -> np.ndarray:
        """Convert grayscale image to binary."""
        # Read image and convert to grayscale
        image = Image.open(image_path).convert('L')
        # Convert to numpy array and threshold
        return (np.array(image) > self.threshold).astype(np.uint8)
    def run_length_encode(self, binary_image: np.ndarray) -> List[int]:
        """Perform run-length coding on binary image."""
        # Flatten the image
        flat_image = binary_image.flatten()
        # Initialize variables
        encoded = []
        count = 1
        current = flat_image[0]
        # Count runs
        for pixel in flat_image[1:]:
            if pixel == current:
                count += 1
            else:
                encoded.append(count)
                current = pixel
                count = 1
        # Append the last run
        encoded.append(count)
        return encoded
    def run_length_decode(self, encoded: List[int], shape: Tuple[int, int], 
                         first_value: int = 0) -> np.ndarray:
        """Decode RLC data back to binary image."""
        # Initialize output array
        decoded = np.zeros(shape[0] * shape[1], dtype=np.uint8)
        # Track position and current value
        pos = 0
        value = first_value
        # Reconstruct the image
        for run_length in encoded:
            decoded[pos:pos + run_length] = value
            pos += run_length
            value = 1 - value  # Toggle between 0 and 1
        return decoded.reshape(shape)
    def analyze_compression(self, image_path: str) -> dict:
        """Perform compression analysis with visualizations."""
        # Start timing
        start_time = time.time()
        # Convert to binary
        binary_image = self.convert_to_binary(image_path)
        # Encode the image
        encoded_data = self.run_length_encode(binary_image)
        # Calculate first value for decoding
        first_value = binary_image.flatten()[0]
        # Decode the image
        decoded_image = self.run_length_decode(encoded_data, binary_image.shape, first_value)
        # End timing
        process_time = time.time() - start_time
        # Calculate compression metrics
        original_size = binary_image.size // 8  # Size in bytes (8 bits per byte)
        encoded_size = len(encoded_data) * 4  # Size in bytes (32-bit integers)
        compression_ratio = original_size / encoded_size
        # Create visualization
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        # Original grayscale image
        original_image = Image.open(image_path).convert('L')
        axes[0, 0].imshow(original_image, cmap='gray')
        axes[0, 0].set_title('Original Grayscale')
        axes[0, 0].axis('off')
        # Binary image
        axes[0, 1].imshow(binary_image, cmap='binary')
        axes[0, 1].set_title('Binary Image')
        axes[0, 1].axis('off')
        # Decoded image
        axes[1, 0].imshow(decoded_image, cmap='binary')
        axes[1, 0].set_title('Decoded Image')
        axes[1, 0].axis('off')
        # Run length distribution
        axes[1, 1].hist(encoded_data, bins=50, color='blue', alpha=0.7)
        axes[1, 1].set_title('Run Length Distribution')
        axes[1, 1].set_xlabel('Run Length')
        axes[1, 1].set_ylabel('Frequency')
        plt.tight_layout()
        # Print analysis
        print("\nRun-Length Coding Analysis:")
        print("-" * 30)
        print(f"Original Size: {original_size:,} bytes")
        print(f"Encoded Size: {encoded_size:,} bytes")
        print(f"Compression Ratio: {compression_ratio:.2f}:1")
        print(f"Space Saving: {(1 - 1/compression_ratio) * 100:.2f}%")
        print(f"Processing Time: {process_time:.3f} seconds")
        # Run length statistics
        print("\nRun Length Statistics:")
        print("-" * 30)
        print(f"Number of Runs: {len(encoded_data):,}")
        print(f"Average Run Length: {np.mean(encoded_data):.2f}")
        print(f"Maximum Run Length: {np.max(encoded_data):,}")
        print(f"Minimum Run Length: {np.min(encoded_data):,}")
        # Verify compression accuracy
        compression_accurate = np.array_equal(binary_image, decoded_image)
        print("\nCompression Verification:")
        print("-" * 30)
        print(f"Lossless Compression: {'Yes' if compression_accurate else 'No'}")
        return {
            'binary_image': binary_image,
            'encoded_data': encoded_data,
            'decoded_image': decoded_image,
            'compression_ratio': compression_ratio,
            'original_size': original_size,
            'encoded_size': encoded_size,
            'process_time': process_time,
            'is_lossless': compression_accurate
        }
    def save_compressed(self, encoded_data: List[int], shape: Tuple[int, int], 
                       first_value: int, output_path: str):
        """Save compressed data to file."""
        # Save shape, first value, and encoded data
        data = {
            'shape': shape,
            'first_value': first_value,
            'encoded_data': encoded_data
        }
        np.save(output_path, data)
    def load_compressed(self, input_path: str) -> Tuple[np.ndarray, dict]:
        """Load and decode compressed data from file."""
        # Load data
        data = np.load(input_path, allow_pickle=True).item()
        # Decode image
        decoded_image = self.run_length_decode(
            data['encoded_data'], 
            data['shape'], 
            data['first_value']
        )
        return decoded_image, data
# Example usage
if __name__ == "__main__":
    # Replace with your image path
    image_path = "Run-Length Coding.jpg"
    # Create compressor instance
    rlc = BinaryRLC(threshold=127)
    # Analyze compression
    results = rlc.analyze_compression(image_path)
    # Save compressed data
    binary_image = rlc.convert_to_binary(image_path)
    encoded_data = rlc.run_length_encode(binary_image)
    first_value = binary_image.flatten()[0]
    # Save and load example
    rlc.save_compressed(encoded_data, binary_image.shape, first_value, "compressed.npy")
    decoded_image, saved_data = rlc.load_compressed("compressed.npy")
    plt.show()