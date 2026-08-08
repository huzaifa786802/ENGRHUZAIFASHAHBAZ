import cv2
import numpy as np
import matplotlib.pyplot as plt
# Read the RGB image and normalize it to [0, 1]
Img = cv2.imread('import cv2')
import numpy as np
import matplotlib.pyplot as plt
# Read the RGB image and normalize it to [0, 1]
Img = cv2.imread('The HSI Model.jpg')
Img = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB) # Convert BGR to RGB
Img = Img.astype(np.float32) / 255.0 # Normalize to range [0, 1]
# Display the original image
plt.figure()
plt.imshow(Img)
plt.title("Original RGB Image")
plt.axis('off')
Img = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB) # Convert BGR to RGB
Img = Img.astype(np.float32) / 255.0 # Normalize to range [0, 1]
# Display the original image
plt.figure()
plt.imshow(Img)
plt.title("Original RGB Image")
plt.axis('off')
# Extract R, G, B channels
R = Img[:, :, 0]
G = Img[:, :, 1]
B = Img[:, :, 2]
# Hue calculation
numerator = 0.5 * (R - G + R - B)
denominator = np.sqrt((R - G) ** 2 + (R - B) * (G - B)) + 1e-7 # Avoid division by zero
H = np.arccos(numerator / denominator)
# Adjust H where B > G
H[B > G] = 2 * np.pi - H[B > G]
H = H / (2 * np.pi) # Normalize to range [0, 1]
# Intensity calculation
I = (R + G + B) / 3
# Saturation calculation
minRGB = np.minimum(np.minimum(R, G), B)
S = 1 - 3 * minRGB / (R + G + B + 1e-7) # Avoid division by zero
# Combine H, S, and I into one visualization
HSI = np.stack((H, S, I), axis=-1)
# Display H, S, and I components
plt.figure(figsize=(12, 4))
# Hue
plt.subplot(1, 3, 1)
plt.imshow(H, cmap='hsv')
plt.title("Hue")
plt.axis('off')
# Saturation
plt.subplot(1, 3, 2)
plt.imshow(S, cmap='gray')
plt.title("Saturation")
plt.axis('off')
# Intensity
plt.subplot(1, 3, 3)
plt.imshow(I, cmap='gray')
plt.title("Intensity")
plt.axis('off') 
plt.tight_layout()
plt.show()