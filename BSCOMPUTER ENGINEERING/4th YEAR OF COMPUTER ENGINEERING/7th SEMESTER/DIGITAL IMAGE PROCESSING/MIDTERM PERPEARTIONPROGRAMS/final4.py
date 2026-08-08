# applying frequency domain filtering to emphasize unique patterns or textures
# use FFT to analyze the fingerprint in the frequency domain.
#apply a band-pass filter to focus on specific frequency ranges that emphaisze fingerprnt ridges
#use a high-pass filter to remove low-frequency noise and improve ridge patterns.
# reconstruct the image from the filtered frequency domain.
import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = ("fingerprint1.jpg")
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
fft_image = np.fft.fft2(gray_img)
fft_shift = np.fft.fftshift(fft_image)  
rows, cols = gray_img.shape
crow, ccol = rows // 2 , cols // 2  
def band_pass_filter(shape, d_low, d_high):
    mask = np.zeros(shape, np.uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            d = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)  
            if d_low <= d <= d_high:
                mask[i, j] = 1
    return mask
def high_pass_filter(shape, cutoff):
    mask = np.ones(shape, np.uint8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            d = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)  
            if d < cutoff:
                mask[i, j] = 0
    return mask
bpf_mask = band_pass_filter(gray_img.shape, 10, 60)  
bpf_filtered = fft_shift * bpf_mask  
hpf_mask = high_pass_filter(gray_img.shape, 30)  
hpf_filtered = fft_shift * hpf_mask  
bpf_reconstructed = np.abs(np.fft.ifft2(np.fft.ifftshift(bpf_filtered)))
hpf_reconstructed = np.abs(np.fft.ifft2(np.fft.ifftshift(hpf_filtered)))
plt.figure(figsize=(12, 6))
plt.subplot(2, 4, 1)
plt.title("Original Image")
plt.imshow(gray_img, cmap='gray')
plt.axis('off')
plt.subplot(2, 4, 2)
plt.title("Band-Pass Filtered")
plt.imshow(bpf_reconstructed, cmap='gray')
plt.axis('off')
plt.subplot(2, 4, 3)
plt.title("High-Pass Filtered")
plt.imshow(hpf_reconstructed, cmap='gray')
plt.axis('off')
plt.subplot(2, 4, 4)
plt.title("FFT Magnitude Spectrum")
plt.imshow(np.log(1 + np.abs(fft_shift)), cmap='gray')
plt.axis('off')
plt.show()