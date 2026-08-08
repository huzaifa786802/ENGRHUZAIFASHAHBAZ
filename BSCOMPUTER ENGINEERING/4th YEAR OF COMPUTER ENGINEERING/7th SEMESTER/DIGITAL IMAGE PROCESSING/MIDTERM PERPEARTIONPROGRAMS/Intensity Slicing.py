import numpy as np
import cv2
import matplotlib.pyplot as plt
# Step 1: Load the grayscale image
image = cv2.imread('Intensity Slicing.jpg',cv2.IMREAD_GRAYSCALE) # Load as grayscale
plt.figure()
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')
# Step 2: Create an RGB image initialized with zeros
I_rgb = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
# Step 3: Perform intensity slicing
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        intensity = image[i, j] 
        if 0 <= intensity < 32: 
            I_rgb[i, j, 0] = 64 # Red channel 
            I_rgb[i, j, 2] = 64 # Blue channel 
        elif 32 <= intensity < 64: 
            I_rgb[i, j, 1] = 64 # Green channel 
            I_rgb[i, j, 2] = 64 # Blue channel 
        elif 64 <= intensity < 96: 
            I_rgb[i, j, 0] = 96 # Red channel 
            I_rgb[i, j, 2] = 96 # Blue channel
        elif 96 <= intensity < 128: 
            I_rgb[i, j, 1] = 96 # Green channel 
            I_rgb[i, j, 2] = 96 # Blue channel 
        elif 128 <= intensity < 160: 
            I_rgb[i, j, 0] = 128 # Red channel 
            I_rgb[i, j, 2] = 128 # Blue channel 
        elif 160 <= intensity < 192: 
            I_rgb[i, j, 0] = 255 # Red channel 
        elif 192 <= intensity < 224: 
            I_rgb[i, j, 1] = 255 # Green channel 
        elif 224 <= intensity < 256: 
            I_rgb[i, j, 2] = 255 # Blue channel
# Step 4: Display the color-mapped image
plt.figure()
plt.imshow(I_rgb)
plt.title("Intensity Sliced Image")
plt.axis('off')
plt.show()