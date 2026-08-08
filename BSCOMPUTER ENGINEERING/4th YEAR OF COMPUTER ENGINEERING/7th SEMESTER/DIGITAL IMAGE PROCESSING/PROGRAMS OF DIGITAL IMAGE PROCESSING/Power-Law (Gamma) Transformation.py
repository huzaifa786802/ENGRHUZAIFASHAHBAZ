import cv2
import numpy as np
import matplotlib.pyplot as plt
def gamma_correction(image, gamma):
# Normalize the image to range [0, 1]
normalized_image = image / 255.0
# Apply the gamma correction
gamma_corrected = np.power(normalized_image, gamma)
# Scale back to [0, 255]
gamma_corrected = np.uint8(gamma_corrected * 255)
return gamma_corrected
# Load the image in grayscale
image = cv2.imread('download.jpeg', 0)
# Define different gamma values for experimentation
gamma_values = [0.5, 1.0, 1.5, 2.0]
# Plot original and gamma corrected images
plt.figure(figsize=(12, 8))
# Display original image
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
# Apply Gamma Transformations for each gamma value
for i, gamma in enumerate(gamma_values):
gamma_image = gamma_correction(image, gamma)
# Display the gamma corrected image
plt.subplot(2, 3, i + 2)
plt.imshow(gamma_image, cmap='gray')
plt.title(f'Gamma = {gamma}')
plt.axis('off')
plt.tight_layout()
plt.show()