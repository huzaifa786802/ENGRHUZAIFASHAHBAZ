import cv2
import numpy as np

def run_length_encode(data):
    encoding = []
    prev_pixel = data[0]
    count = 1
    # Iterate through the array starting from the second element
    for pixel in data[1:]:
        if pixel == prev_pixel:
            count += 1
        else:
            encoding.append((prev_pixel, count))
            prev_pixel = pixel
            count = 1
    # Append the last sequence
    encoding.append((prev_pixel, count))
    return encoding

def main():
    # Read the image
    image = cv2.imread('Run-Length Coding.jpg', cv2.IMREAD_GRAYSCALE)  # Read as grayscale
    # Flatten the image into a 1D array
    flat_image = image.flatten()
    # Perform RLE
    encoded_rlc = run_length_encode(flat_image)
    # Print some statistics
    print(f"Original image size: {image.shape}")
    print(f"Original number of pixels: {len(flat_image)}")
    print(f"Number of RLE sequences: {len(encoded_rlc)}")
    # Print first few encoded sequences
    print("\nFirst 10 RLE sequences:")
    for i, (pixel, count) in enumerate(encoded_rlc[:10]):
        print(f"Sequence {i+1}: Pixel value {pixel}, Count {count}")
    # Calculate compression ratio
    original_size = len(flat_image)
    compressed_size = len(encoded_rlc) * 2  # Each tuple has 2 numbers (pixel_value, count)
    compression_ratio = original_size / compressed_size
    print(f"\nCompression ratio: {compression_ratio:.2f}:1")
if __name__ == "__main__":
    main()