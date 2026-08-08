import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image in grayscale
image = cv2.imread('Screenshot 2024-10-30 124752.jpg', 0)
# Calculate the histogram using numpy.histogram()
# 'bins=256' means we want 256 intensity levels (for grayscale images, 0 to 255)
# 'range=(0, 256)' means we are considering pixel intensities in this range
hist, bin_edges = np.histogram(image, bins=256, range=(0, 256))
#histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
# Plot the histogram
plt.plot(bin_edges[0:-1], hist)
plt.title('Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()