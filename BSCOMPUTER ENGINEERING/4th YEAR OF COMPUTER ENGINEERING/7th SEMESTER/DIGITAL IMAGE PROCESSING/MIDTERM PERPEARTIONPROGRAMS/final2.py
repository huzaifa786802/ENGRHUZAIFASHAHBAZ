# compress a fingerprint image using Run-length coding
import cv2
import numpy as np
def rle_encode(img):
    pixels = img.flatten()  
    rle = []
    prev_pixel = pixels[0]
    count = 1
    for pixel in pixels[1:]:
        if pixel == prev_pixel:
            count += 1
        else:
            rle.append((prev_pixel, count)) 
            prev_pixel=pixel
            count=1 
    rle.append((prev_pixel, count))  
    return rle
image_path = ("fingerprint1.jpg")
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
compressed_data = rle_encode(gray_img)
print("Compressed Data (First 25 runs):", compressed_data[:20])
original_size = gray_img.size  
compressed_size = len(compressed_data) * 2  
compression_ratio = original_size/compressed_size
print("Original Size: "+str(original_size)+" pixels")
print("Compressed Size: "+str(compressed_size)+" values")
print("Compression Ratio: %.2f" %compression_ratio)