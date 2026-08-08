import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = ('Screenshot 2024-10-30 124752.jpg' ) # Replace with your image path if different
image = cv2.imread(image_path, 0)
laplacian_filter = cv2.Laplacian(image, cv2.CV_64F)
laplacian_filter = cv2.convertScaleAbs(laplacian_filter)  # Convert to 8-bit
gaussian_blur = cv2.GaussianBlur(image, (5, 5), sigmaX=1)
unsharp_image = cv2.addWeighted(image, 1.5, gaussian_blur, -0.5, 0)
plt.figure(figsize=(12, 5))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(laplacian_filter, cmap='gray')
plt.title('Laplacian Filter')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(unsharp_image, cmap='gray')
plt.title('Unsharp Masking')
plt.axis('off')
plt.tight_layout()
plt.show()