import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
image = cv2.imread('COLORSCALING.jpg')  # Replace 'image.jpg' with your image path
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
# Function to perform image quantization
def quantize_image(image, levels):
    step = 256 // levels
    quantized = (image // step) * step + step // 2
    return np.clip(quantized, 0, 255).astype(np.uint8)
# Quantize the image with a given number of levels
quantized_image_4 = quantize_image(image, levels=4)
quantized_image_8 = quantize_image(image, levels=8)
quantized_image_6 = quantize_image(image, levels=6)
quantized_image_16 = quantize_image(image, levels=16)
# Function to perform intensity slicing
def intensity_slice(channel, min_val, max_val):
    sliced = np.zeros_like(channel)
    sliced[(channel >= min_val) & (channel <= max_val)] = channel[(channel >= min_val) & (channel <= max_val)]
    return sliced
# Slice intensity ranges for each channel
red_channel, green_channel, blue_channel = image[:, :, 0], image[:, :, 1], image[:, :, 2]
red_sliced = intensity_slice(red_channel, 100, 200)
green_sliced = intensity_slice(green_channel, 50, 150)
blue_sliced = intensity_slice(blue_channel, 0, 100)
# Quantize the sliced channels
red_quantized_4 = quantize_image(red_sliced, levels=4)
green_quantized_4 = quantize_image(green_sliced, levels=4)
blue_quantized_4 = quantize_image(blue_sliced, levels=4)
red_quantized_8 = quantize_image(red_sliced, levels=8)
green_quantized_8 = quantize_image(green_sliced, levels=8)
blue_quantized_8 = quantize_image(blue_sliced, levels=8)
red_quantized_6 = quantize_image(red_sliced, levels=6)
green_quantized_6 = quantize_image(green_sliced, levels=6)
blue_quantized_6 = quantize_image(blue_sliced, levels=6)
red_quantized_16 = quantize_image(red_sliced, levels=16)
green_quantized_16 = quantize_image(green_sliced, levels=16)
blue_quantized_16 = quantize_image(blue_sliced, levels=16)
# Display the results
fig, axs = plt.subplots(5, 4, figsize=(20, 20))
# Original image and quantized images
axs[0, 0].imshow(image)
axs[0, 0].set_title("Original Image")
axs[0, 0].axis('off')
axs[0, 1].imshow(quantized_image_4)
axs[0, 1].set_title("Quantized (4 levels)")
axs[0, 1].axis('off')
axs[0, 2].imshow(quantized_image_8)
axs[0, 2].set_title("Quantized (8 levels)")
axs[0, 2].axis('off')
axs[0, 3].imshow(quantized_image_6)
axs[0, 3].set_title("Quantized (6 levels)")
axs[0, 3].axis('off')
axs[1, 0].imshow(quantized_image_16)
axs[1, 0].set_title("Quantized (16 levels)")
axs[1, 0].axis('off')
# Red channel slicing and quantization
axs[1, 1].imshow(red_sliced, cmap='Reds')
axs[1, 1].set_title("Red Channel Sliced")
axs[1, 1].axis('off')
axs[1, 2].imshow(red_quantized_4, cmap='Reds')
axs[1, 2].set_title("Red Channel Quantized (4 levels)")
axs[1, 2].axis('off')
axs[1, 3].imshow(red_quantized_8, cmap='Reds')
axs[1, 3].set_title("Red Channel Quantized (8 levels)")
axs[1, 3].axis('off')
axs[2, 0].imshow(red_quantized_6, cmap='Reds')
axs[2, 0].set_title("Red Channel Quantized (6 levels)")
axs[2, 0].axis('off')
axs[2, 1].imshow(red_quantized_16, cmap='Reds')
axs[2, 1].set_title("Red Channel Quantized (16 levels)")
axs[2, 1].axis('off')
# Green channel slicing and quantization
axs[2, 2].imshow(green_sliced, cmap='Greens')
axs[2, 2].set_title("Green Channel Sliced")
axs[2, 2].axis('off')
axs[2, 3].imshow(green_quantized_4, cmap='Greens')
axs[2, 3].set_title("Green Channel Quantized (4 levels)")
axs[2, 3].axis('off')
axs[3, 0].imshow(green_quantized_8, cmap='Greens')
axs[3, 0].set_title("Green Channel Quantized (8 levels)")
axs[3, 0].axis('off')
axs[3, 1].imshow(green_quantized_6, cmap='Greens')
axs[3, 1].set_title("Green Channel Quantized (6 levels)")
axs[3, 1].axis('off')
axs[3, 2].imshow(green_quantized_16, cmap='Greens')
axs[3, 2].set_title("Green Channel Quantized (16 levels)")
axs[3, 2].axis('off')
# Blue channel slicing and quantization
axs[3, 3].imshow(blue_sliced, cmap='Blues')
axs[3, 3].set_title("Blue Channel Sliced")
axs[3, 3].axis('off')
axs[4, 0].imshow(blue_quantized_4, cmap='Blues')
axs[4, 0].set_title("Blue Channel Quantized (4 levels)")
axs[4, 0].axis('off')
axs[4, 1].imshow(blue_quantized_8, cmap='Blues')
axs[4, 1].set_title("Blue Channel Quantized (8 levels)")
axs[4, 1].axis('off')
axs[4, 2].imshow(blue_quantized_6, cmap='Blues')
axs[4, 2].set_title("Blue Channel Quantized (6 levels)")
axs[4, 2].axis('off')
axs[4, 3].imshow(blue_quantized_16, cmap='Blues')
axs[4, 3].set_title("Blue Channel Quantized (16 levels)")
axs[4, 3].axis('off')
plt.tight_layout()
plt.show()
import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
image = cv2.imread('COLORSCALING.jpg')  # Replace 'image.jpg' with your image path
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
# Function to perform image quantization
def quantize_image(image, levels):
    step = 256 // levels
    quantized = (image // step) * step + step // 2
    return np.clip(quantized, 0, 255).astype(np.uint8)
# Quantize the image with a given number of levels
quantized_image_4 = quantize_image(image, levels=4)
quantized_image_8 = quantize_image(image, levels=8)
quantized_image_6 = quantize_image(image, levels=6)
quantized_image_16 = quantize_image(image, levels=16)
# Function to perform intensity slicing
def intensity_slice(channel, min_val, max_val):
    sliced = np.zeros_like(channel)
    sliced[(channel >= min_val) & (channel <= max_val)] = channel[(channel >= min_val) & (channel <= max_val)]
    return sliced
# Slice intensity ranges for each channel
red_channel, green_channel, blue_channel = image[:, :, 0], image[:, :, 1], image[:, :, 2]
red_sliced = intensity_slice(red_channel, 100, 200)
green_sliced = intensity_slice(green_channel, 50, 150)
blue_sliced = intensity_slice(blue_channel, 0, 100)
# Quantize the sliced channels
red_quantized_4 = quantize_image(red_sliced, levels=4)
green_quantized_4 = quantize_image(green_sliced, levels=4)
blue_quantized_4 = quantize_image(blue_sliced, levels=4)
red_quantized_8 = quantize_image(red_sliced, levels=8)
green_quantized_8 = quantize_image(green_sliced, levels=8)
blue_quantized_8 = quantize_image(blue_sliced, levels=8)
red_quantized_6 = quantize_image(red_sliced, levels=6)
green_quantized_6 = quantize_image(green_sliced, levels=6)
blue_quantized_6 = quantize_image(blue_sliced, levels=6)
red_quantized_16 = quantize_image(red_sliced, levels=16)
green_quantized_16 = quantize_image(green_sliced, levels=16)
blue_quantized_16 = quantize_image(blue_sliced, levels=16)
# Display the results
fig, axs = plt.subplots(5, 4, figsize=(20, 20))
# Original image and quantized images
axs[0, 0].imshow(image)
axs[0, 0].set_title("Original Image")
axs[0, 0].axis('off')
axs[0, 1].imshow(quantized_image_4)
axs[0, 1].set_title("Quantized (4 levels)")
axs[0, 1].axis('off')
axs[0, 2].imshow(quantized_image_8)
axs[0, 2].set_title("Quantized (8 levels)")
axs[0, 2].axis('off')
axs[0, 3].imshow(quantized_image_6)
axs[0, 3].set_title("Quantized (6 levels)")
axs[0, 3].axis('off')
axs[1, 0].imshow(quantized_image_16)
axs[1, 0].set_title("Quantized (16 levels)")
axs[1, 0].axis('off')
# Red channel slicing and quantization
axs[1, 1].imshow(red_sliced, cmap='Reds')
axs[1, 1].set_title("Red Channel Sliced")
axs[1, 1].axis('off')
axs[1, 2].imshow(red_quantized_4, cmap='Reds')
axs[1, 2].set_title("Red Channel Quantized (4 levels)")
axs[1, 2].axis('off')
axs[1, 3].imshow(red_quantized_8, cmap='Reds')
axs[1, 3].set_title("Red Channel Quantized (8 levels)")
axs[1, 3].axis('off')
axs[2, 0].imshow(red_quantized_6, cmap='Reds')
axs[2, 0].set_title("Red Channel Quantized (6 levels)")
axs[2, 0].axis('off')
axs[2, 1].imshow(red_quantized_16, cmap='Reds')
axs[2, 1].set_title("Red Channel Quantized (16 levels)")
axs[2, 1].axis('off')
# Green channel slicing and quantization
axs[2, 2].imshow(green_sliced, cmap='Greens')
axs[2, 2].set_title("Green Channel Sliced")
axs[2, 2].axis('off')
axs[2, 3].imshow(green_quantized_4, cmap='Greens')
axs[2, 3].set_title("Green Channel Quantized (4 levels)")
axs[2, 3].axis('off')
axs[3, 0].imshow(green_quantized_8, cmap='Greens')
axs[3, 0].set_title("Green Channel Quantized (8 levels)")
axs[3, 0].axis('off')
axs[3, 1].imshow(green_quantized_6, cmap='Greens')
axs[3, 1].set_title("Green Channel Quantized (6 levels)")
axs[3, 1].axis('off')
axs[3, 2].imshow(green_quantized_16, cmap='Greens')
axs[3, 2].set_title("Green Channel Quantized (16 levels)")
axs[3, 2].axis('off')
# Blue channel slicing and quantization
axs[3, 3].imshow(blue_sliced, cmap='Blues')
axs[3, 3].set_title("Blue Channel Sliced")
axs[3, 3].axis('off')
axs[4, 0].imshow(blue_quantized_4, cmap='Blues')
axs[4, 0].set_title("Blue Channel Quantized (4 levels)")
axs[4, 0].axis('off')
axs[4, 1].imshow(blue_quantized_8, cmap='Blues')
axs[4, 1].set_title("Blue Channel Quantized (8 levels)")
axs[4, 1].axis('off')
axs[4, 2].imshow(blue_quantized_6, cmap='Blues')
axs[4, 2].set_title("Blue Channel Quantized (6 levels)")
axs[4, 2].axis('off')
axs[4, 3].imshow(blue_quantized_16, cmap='Blues')
axs[4, 3].set_title("Blue Channel Quantized (16 levels)")
axs[4, 3].axis('off')
plt.tight_layout()
plt.show()