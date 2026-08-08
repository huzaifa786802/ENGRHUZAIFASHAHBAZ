import cv2
import numpy as np
import matplotlib.pyplot as plt
# Read the RGB image
I = cv2.imread('The CMY Model.jpg')
I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB) # Convert BGR to RGB for proper color display
# Display the original RGB image
plt.figure()
plt.imshow(I)
plt.title("Original RGB Image")
plt.axis('off')
# Create a CMY image by subtracting each channel from 255
CMY = np.zeros_like(I) # Initialize CMY array with the same shape as I
R = I[:, :, 0] # Red channel
G = I[:, :, 1] # Green channel
B = I[:, :, 2] # Blue channel
# Compute CMY channels
CMY[:, :, 0] = 255 - R # Cyan (complement of red)
CMY[:, :, 1] = 255 - G # Magenta (complement of green)
CMY[:, :, 2] = 255 - B # Yellow (complement of blue)
# Display the CMY image
plt.figure()
plt.imshow(CMY)
plt.title("CMY Image")
plt.axis('off')
plt.show()