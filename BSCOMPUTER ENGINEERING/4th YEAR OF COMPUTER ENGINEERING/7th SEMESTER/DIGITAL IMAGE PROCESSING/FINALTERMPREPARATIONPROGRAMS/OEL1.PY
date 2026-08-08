from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
# Load the uploaded image
image_path = "OEL-Image-1.jpg"
image = Image.open(image_path)
# Display the original image
plt.figure(figsize=(6, 6))
plt.title("Original Image")
plt.imshow(image)
plt.axis("off")
plt.show()
# Convert the image to grayscale for processing
gray_image = image.convert("L")
# Display the grayscale image
plt.figure(figsize=(6, 6))
plt.title("Grayscale Image")
plt.imshow(gray_image, cmap="gray")
plt.axis("off")
plt.show()
# Convert the grayscale image to a NumPy array for further processing
gray_array = np.array(gray_image)
gray_array.shape