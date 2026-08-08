#convert a grayscale fingerprint imaage into pesudo-color using intensity slicing
import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = ("fingerprint1.jpg")
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
def pseudoColor(img):
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    color_map = [
        (0, (255, 0, 0)),      
        (68, (0, 255, 0)),     
        (148, (0, 255, 255)),  
        (190, (0, 0, 255)),    
        (255, (255, 255, 255)) 
    ]
    pseudo_color_img = np.zeros((*img.shape, 3), dtype=np.uint8)
    for i in range(len(color_map) - 1):
        lower, color1 = color_map[i]
        upper, color2 = color_map[i + 1]
        mask = (img >= lower) & (img < upper)
        pseudo_color_img[mask] = color1
    return pseudo_color_img
pseudo_color_img = pseudoColor(gray_img)
plt.figure(figsize=(12,6))
plt.subplot(1,3,1)
plt.title("Grayscale Image")
plt.imshow(gray_img, cmap='gray')
plt.axis('off')
plt.subplot(1,2,2)
plt.title("Pseudo-colored Image")
plt.imshow(cv2.cvtColor(pseudo_color_img, cv2.COLOR_BGR2RGB))  
plt.axis('off')
plt.show()