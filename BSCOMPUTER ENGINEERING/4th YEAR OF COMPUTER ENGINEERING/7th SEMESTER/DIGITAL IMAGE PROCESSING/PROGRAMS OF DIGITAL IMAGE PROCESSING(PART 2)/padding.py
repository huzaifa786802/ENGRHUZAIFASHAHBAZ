import cv2
import numpy as np
from matplotlib import pyplot as plt
def create_mask():
    rows = int(input("Enter the number of rows for the mask: "))
    cols = int(input("Enter the number of columns for the mask: "))
    values = []
    print("Enter the values for the mask:")
    for _ in range(rows * cols):
        value = int(input())
        values.append(value)
    mask = np.array(values).reshape((rows, cols))
    return mask
def add_padding(image, padding_size, padding_type='zero'):
    if padding_type == 'zero':
        padded_image = cv2.copyMakeBorder(image, padding_size, padding_size, padding_size, padding_size, cv2.BORDER_CONSTANT, value=0)
    elif padding_type == 'replicate':
        padded_image = cv2.copyMakeBorder(image, padding_size, padding_size, padding_size, padding_size, cv2.BORDER_REPLICATE)
    return padded_image
def apply_filter(image, mask):
    filtered_image = cv2.filter2D(image, -1, mask)
    return filtered_image
def normalize_image(image):
    normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    return normalized_image.astype(np.uint8)
image = cv2.imread('Screenshot 2024-11-01 093850.jpg', cv2.IMREAD_GRAYSCALE)
mask = np.ones((3, 3), np.float32) / 9  
padding_size = 1  
padded_image = add_padding(image, padding_size, padding_type='zero')
filtered_image = apply_filter(padded_image, mask)
normalized_image = normalize_image(filtered_image)
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 3, 2), plt.imshow(filtered_image, cmap='gray'), plt.title('Filtered Image')
plt.subplot(1, 3, 3), plt.imshow(normalized_image, cmap='gray'), plt.title('Normalized Image')
plt.show()