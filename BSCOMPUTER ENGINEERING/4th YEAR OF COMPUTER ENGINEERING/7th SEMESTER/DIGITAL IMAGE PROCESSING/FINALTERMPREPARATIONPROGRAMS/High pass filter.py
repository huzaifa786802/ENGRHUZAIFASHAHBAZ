from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
# Load the image
image_path = "High pass filter.jpg"
image = Image.open(image_path).convert("L")  # Convert to grayscale
# Convert the image to a NumPy array
image_array = np.array(image)
# Apply Fourier Transform to the image
f = np.fft.fft2(image_array)
fshift = np.fft.fftshift(f)
# Create a High-Pass Filter (HPF)
rows, cols = image_array.shape
crow, ccol = rows // 2, cols // 2
# Create a mask with a centered square of zeros (low-pass block)
mask = np.ones((rows, cols), np.uint8)
size = 30  # Define the size of the low-pass block
mask[crow - size:crow + size, ccol - size:ccol + size] = 0
# Apply the mask to the frequency domain
fshift_filtered = fshift * mask
# Inverse Fourier Transform to get the filtered image
f_ishift = np.fft.ifftshift(fshift_filtered)
image_filtered = np.abs(np.fft.ifft2(f_ishift))
# Plot the original and high-pass filtered images
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_array, cmap="gray")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.title("High-Pass Filtered Image")
plt.imshow(image_filtered, cmap="gray")
plt.axis("off")
plt.tight_layout()
plt.show()