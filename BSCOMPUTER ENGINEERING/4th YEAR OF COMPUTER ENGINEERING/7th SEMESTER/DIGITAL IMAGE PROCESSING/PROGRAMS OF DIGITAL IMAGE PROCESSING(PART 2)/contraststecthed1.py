import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
img = cv2.imread('Screenshot 2024-10-26 122930.jpg', 0)
# Calculate the 5th and 95th percentiles
p5 = np.percentile(img, 5)
p95 = np.percentile(img, 95)
# Apply contrast stretching
stretched_img = np.clip((img - p5) * (255 / (p95 - p5)), 0, 255).astype(np.uint8)
# Display the original and stretched images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(stretched_img, cmap='gray')
plt.title('Contrast Stretched Image')
plt.axis('off')
plt.tight_layout()
plt.show()