#perform morphological operations to refine fingerprint pattrns
# use eroison to thin the rideges
# apply dilation to enhance broken or faint rideges
#use opening to remove noise and isolate continious pattern or textures
import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = ("fingerprint1.jpg")
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)  # 3x3 kernel
eroded_img = cv2.erode(gray_img, kernel, iterations=1)
dilated_img = cv2.dilate(gray_img, kernel, iterations=1)
opened_img = cv2.morphologyEx(gray_img, cv2.MORPH_OPEN, kernel)
plt.figure(figsize=(14, 7))
plt.subplot(2, 5, 2)
plt.title("Original")
plt.imshow(gray_img, cmap='gray')
plt.axis('off')
plt.subplot(2, 5, 3)
plt.title("Erosion (Thinning Ridges)")
plt.imshow(eroded_img, cmap='gray')
plt.axis('off')
plt.subplot(2, 5, 4)
plt.title("Dilation (Enhancing Ridges)")
plt.imshow(dilated_img, cmap='gray')
plt.axis('off')
plt.subplot(2, 5, 5)
plt.title("Opening (Noise Removal)")
plt.imshow(opened_img, cmap='gray')
plt.axis('off')
plt.show()