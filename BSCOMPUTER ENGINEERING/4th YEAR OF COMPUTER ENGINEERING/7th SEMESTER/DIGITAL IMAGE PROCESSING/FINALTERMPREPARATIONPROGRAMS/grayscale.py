import cv2
import matplotlib.pyplot as plt
import numpy as np
# Load the grayscale image
image_path = 'grayscale.jpg'  # Replace with the path to your image
grayscale_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# Apply HSV and RAINBOW colormaps
hsv_colormap = cv2.applyColorMap(grayscale_image, cv2.COLORMAP_HSV)
rainbow_colormap = cv2.applyColorMap(grayscale_image, cv2.COLORMAP_RAINBOW)
# Display the results
plt.figure(figsize=(15, 5))
# Original grayscale image
plt.subplot(1, 3, 1)
plt.title("Grayscale Image")
plt.imshow(grayscale_image, cmap='gray')
plt.axis('off')
# HSV colormap
plt.subplot(1, 3, 2)
plt.title("HSV Colormap")
plt.imshow(cv2.cvtColor(hsv_colormap, cv2.COLOR_BGR2RGB))
plt.axis('off')
# RAINBOW colormap
plt.subplot(1, 3, 3)
plt.title("RAINBOW Colormap")
plt.imshow(cv2.cvtColor(rainbow_colormap, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.tight_layout()
plt.show()