import numpy as np
import matplotlib.pyplot as plt

# Define a square structuring element
def square_structuring_element(size):
    return np.ones((size, size), dtype=np.uint8)

# Define a disk structuring element
def disk_structuring_element(radius):
    diameter = 2 * radius + 1
    y, x = np.ogrid[-radius:radius+1, -radius:radius+1]
    mask = x**2 + y**2 <= radius**2
    return mask.astype(np.uint8)

# Create structuring elements
square_element = square_structuring_element(5)
disk_element = disk_structuring_element(3)

# Display the structuring elements
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title('Square Structuring Element')
plt.imshow(square_element, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Disk Structuring Element')
plt.imshow(disk_element, cmap='gray')
plt.axis('off')

plt.show()