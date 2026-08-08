import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.util import random_noise
image = io.imread('Screenshot 2024-11-01 094346.jpg')
noisy_image = random_noise(image, mode='gaussian', var=0.01)  # var controls the amount of noise
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Image with Gaussian Noise')
plt.imshow(noisy_image)
plt.axis('off')
plt.show()