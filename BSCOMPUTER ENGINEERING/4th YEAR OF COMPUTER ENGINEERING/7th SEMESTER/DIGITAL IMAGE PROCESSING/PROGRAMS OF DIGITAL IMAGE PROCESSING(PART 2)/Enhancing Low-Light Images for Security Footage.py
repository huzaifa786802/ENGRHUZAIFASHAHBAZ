import cv2
import numpy as np
import matplotlib.pyplot as plt
def zoom_image(img, zoom_factor): 
    # img: Input image matrix (grayscale or RGB) 
    # # zoom_factor: Factor by which the image is zoomed 
    # # Get the size of the original image 
    rows, cols, channels = img.shape 
    # Initialize the zoomed image matrix 
    zoomed_image = np.zeros((zoom_factor * rows, zoom_factor * cols, channels), dtype=np.uint8) 
    # Apply pixel replication  
    for i in range(rows): 
       for j in range(cols): 
         zoomed_image[i * zoom_factor:(i + 1) * zoom_factor, j * zoom_factor:(j + 1) * zoom_factor, :] = img[i, j, :] 
         return zoomed_image
# Load the image
img = cv2.imread('Dahua-IPC-HDW5231R-Z-with-internal-IR-off-and-no-extra-light.jpg')
# Zoom factor (e.g., zoom by a factor of 2, you can change this to 3, 4,etc.)
zoom_factor = 2
# Zoom the image
zoomed_img = zoom_image(img, zoom_factor)
# Display the original and zoomed image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(zoomed_img, cv2.COLOR_BGR2RGB))
plt.title(f'Zoomed Image by factor of {zoom_factor}')
plt.axis('off')
plt.show()