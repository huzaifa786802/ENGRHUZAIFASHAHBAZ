import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = ('Screenshot 2024-10-30 124752.jpg')  # Replace with your image path if different
image = cv2.imread(image_path, 0)
average_blur = cv2.blur(image, (5, 5))  # 5x5 kernel size
gaussian_blur = cv2.GaussianBlur(image, (5, 5), sigmaX=1)  # 5x5 kernel, sigmaX=1
plt.figure(figsize=(12, 5))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(average_blur, cmap='gray')
plt.title('Averaging Filter')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(gaussian_blur, cmap='gray')
plt.title('Gaussian Filter')
plt.axis('off')
plt.tight_layout()
plt.show()