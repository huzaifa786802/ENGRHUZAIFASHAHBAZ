#convert a grayscale fingerprint imaage into pesudo-color using intensity slicing
# compress a fingerprint image using Run-length coding
#perform morphological operations to refine fingerprint pattrns
# use eroison to thin the rideges
# apply dilation to enhance broken or faint rideges
#use opening to remove noise and isolate continious pattern or textures
# applying frequency domain filtering to emphasize unique patterns or textures
# use FFT to analyze the fingerprint in the frequency domain.
#apply a band-pass filter to focus on specific frequency ranges that emphaisze fingerprnt ridges
#use a high-pass filter to remove low-frequency noise and improve ridge patterns.
# reconstruct the image from the filtered frequency domain.
import cv2
import numpy as np
import matplotlib.pyplot as plt
def pseudoColor(img):
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    color_map = [
        (0, (255, 0, 0)),      
        (64, (0, 255, 0)),     
        (128, (0, 255, 255)),  
        (192, (0, 0, 255)),    
        (255, (255, 255, 255)) 
    ]
    pseudo_color_img = np.zeros((*img.shape, 3), dtype=np.uint8)
    for i in range(len(color_map) - 1):
        lower, color1 = color_map[i]
        upper, color2 = color_map[i + 1]
        mask = (img >= lower) & (img < upper)
        pseudo_color_img[mask] = color1
    return pseudo_color_img
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
            prev_pixel = pixel
            count = 1 
    rle.append((prev_pixel, count))  
    return rle
def morphological_operations(img):
    kernel = np.ones((5,5), np.uint8)
    eroded = cv2.erode(img, kernel, iterations=1)
    dilated = cv2.dilate(img, kernel, iterations=1)
    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return eroded, dilated, opened
def band_pass_filter(shape, d_low, d_high, crow, ccol):
    mask = np.zeros(shape, np.uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            d = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            if d_low <= d <= d_high:
                mask[i, j] = 1
    return mask
def high_pass_filter(shape, cutoff, crow, ccol):
    mask = np.ones(shape, np.uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            d = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            if d < cutoff:
                mask[i, j] = 0
    return mask
def frequency_domain_filtering(img):
    fft_image = np.fft.fft2(img)
    fft_shift = np.fft.fftshift(fft_image)
    rows, cols = img.shape
    crow, ccol = rows // 2 , cols // 2
    bpf_mask = band_pass_filter(img.shape, 10, 60, crow, ccol)
    hpf_mask = high_pass_filter(img.shape, 30, crow, ccol)
    bpf_filtered = fft_shift * bpf_mask
    hpf_filtered = fft_shift * hpf_mask
    bpf_reconstructed = np.abs(np.fft.ifft2(np.fft.ifftshift(bpf_filtered)))
    hpf_reconstructed = np.abs(np.fft.ifft2(np.fft.ifftshift(hpf_filtered)))
    return bpf_reconstructed, hpf_reconstructed, np.log(1 + np.abs(fft_shift))
gray_img = cv2.imread("fingerprint1.jpg", cv2.IMREAD_GRAYSCALE)
pseudo_color_img = pseudoColor(gray_img)
compressed_data = rle_encode(gray_img)
original_size = gray_img.size
compressed_size = len(compressed_data) * 2
compression_ratio = original_size / compressed_size
eroded_img, dilated_img, opened_img = morphological_operations(gray_img)
bpf_reconstructed, hpf_reconstructed, fft_spectrum = frequency_domain_filtering(gray_img)
plt.figure(figsize=(16, 10))
plt.subplot(2, 4, 1)
plt.title("Original Image")
plt.imshow(gray_img, cmap='gray')
plt.axis('off')
plt.subplot(2, 4, 2)
plt.title("Pseudo-colored Image")
plt.imshow(cv2.cvtColor(pseudo_color_img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.subplot(2, 4, 3)
plt.title("Erosion")
plt.imshow(eroded_img, cmap='gray')
plt.axis('off')
plt.subplot(2, 4, 4)
plt.title("Dilation")
plt.imshow(dilated_img, cmap='gray')
plt.axis('off')
plt.subplot(2, 4, 5)
plt.title("Opening (Noise Removal)")
plt.imshow(opened_img, cmap='gray')
plt.axis('off')
plt.subplot(2, 4, 6)
plt.title("Band-Pass Filtered")
plt.imshow(bpf_reconstructed, cmap='gray')
plt.axis('off')
plt.subplot(2, 4, 7)
plt.title("High-Pass Filtered")
plt.imshow(hpf_reconstructed, cmap='gray')
plt.axis('off')
plt.subplot(2, 4, 8)
plt.title("FFT Spectrum")
plt.imshow(fft_spectrum, cmap='gray')
plt.axis('off')
plt.show()
print("Compressed Data (First 25 runs):", compressed_data[:25])
print(f"Original Size: {original_size} pixels")
print(f"Compressed Size: {compressed_size} values")
print(f"Compression Ratio: {compression_ratio:.2f}")