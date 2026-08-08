import cv2
import numpy as np
import matplotlib.pyplot as plt
# Import the image
img = plt.imread("The CMY Model.jpg")
# Normalize the BGR image to range [0, 1]
bgr = img.astype(float) / 255.0
# Calculate CMYK channels
with np.errstate(invalid='ignore', divide='ignore'):
    K = 1 - np.max(bgr, axis=2)
    C = (1 - bgr[..., 2] - K) / (1 - K + 1e-10)  # Add a small value to avoid division by zero
    M = (1 - bgr[..., 1] - K) / (1 - K + 1e-10)
    Y = (1 - bgr[..., 0] - K) / (1 - K + 1e-10)
# Stack the channels and scale to [0, 255]
CMYK = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)
# Split CMYK channels
C, M, Y, K = cv2.split(CMYK)
# Save each CMYK channel as a separate image
cv2.imwrite('C_Channel.jpg', C)
cv2.imwrite('M_Channel.jpg', M)
cv2.imwrite('Y_Channel.jpg', Y)
cv2.imwrite('K_Channel.jpg', K)
# Function to convert CMY to RGB
def cmy_to_rgb(c, m, y, key):
    r = (1 - c) * (1 - key)
    g = (1 - m) * (1 - key)
    b = (1 - y) * (1 - key)
    return r, g, b
# Example usage of the CMY to RGB conversion function
c = 1 - 0.412
m = 1 - 0.412
y = 1 - 0.412
key = 0.412
r, g, b = cmy_to_rgb(c, m, y, key)
# Print the RGB values
print(f"R: {r:.3f}")
print(f"G: {g:.3f}")
print(f"B: {b:.3f}")