import cv2
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
# Load a grayscale image
image = cv2.imread("Huffman Coding.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("Image not found. Please check the file path.")
# Calculate pixel intensity frequencies
unique, counts = np.unique(image, return_counts=True)
frequency = dict(zip(unique, counts))
# Create a Huffman Tree
def huffman_tree(frequency):
    # Create a heap with frequency and symbol pairs
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    while len(heap) > 1:
        heap.sort()  # Sort by frequency
        lo = heap.pop(0)  # Remove the two smallest nodes
        hi = heap.pop(0)
        for pair in lo[1:]:
            pair[1] = "0" + pair[1]  # Append '0' to the left node
        for pair in hi[1:]:
            pair[1] = "1" + pair[1]  # Append '1' to the right node
        # Merge the two nodes and push back to the heap
        heap.append([lo[0] + hi[0]] + lo[1:] + hi[1:])
    # Return sorted Huffman codes
    return sorted(heap[0][1:], key=lambda p: (len(p[1]), p))
# Generate Huffman codes
huffman_codes = huffman_tree(frequency)
huffman_dict = {symbol: code for symbol, code in huffman_codes}
# Encode the image
encoded_image = "".join([huffman_dict[pixel] for pixel in image.flatten()])
# Calculate the size of the Huffman encoded image
original_size = image.size * 8  # Original image size in bits (8 bits per pixel)
encoded_size = len(encoded_image)  # Encoded image size in bits
# Print results
print(f"Original Image Size: {original_size} bits")
print(f"Huffman Encoded Image Size: {encoded_size} bits")
# Save Huffman codes to a file (optional)
with open("huffman_codes.txt", "w") as f:
    for symbol, code in huffman_codes:
        f.write(f"{symbol}: {code}\\n")
# Save the encoded image (optional)
with open("encoded_image.txt", "w") as f:
    f.write(encoded_image)
# Display the original image
plt.figure(figsize=(8, 6))
plt.imshow(image, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis("off")
plt.show()