import cv2
import matplotlib.pyplot as plt
# Load the image
image = cv2.imread('input_image.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert to RGB for display
# Split the image into R, G, B channels
r_channel, g_channel, b_channel = cv2.split(image_rgb)
# Display the original image and each channel
plt.figure(figsize=(12, 6))
# Original Image
plt.subplot(1, 4, 1)
plt.imshow(image_rgb)
plt.title("Original RGB Image")
plt.axis('off')
# Red Channel
plt.subplot(1, 4, 2)
plt.imshow(r_channel, cmap='Reds')
plt.title("Red Channel")
plt.axis('off')
# Green Channel
plt.subplot(1, 4, 3)
plt.imshow(g_channel, cmap='Greens')
plt.title("Green Channel")
plt.axis('off')
# Blue Channel
plt.subplot(1, 4, 4)
plt.imshow(b_channel, cmap='Blues')
plt.title("Blue Channel")
plt.axis('off')
plt.tight_layout()
plt.show()