def gray_level_slicing(image, min_val, max_val, slice_value):
# Create an output image filled with zeros (black)
output_image = np.zeros_like(image)
# Set the pixel values within the specified range to the slice_value
output_image[(image >= min_val) & (image <= max_val)] = slice_value
return output_image
# Apply gray-level slicing to highlight pixels in the range [100, 200]
sliced_image = gray_level_slicing(image, 100, 200, 255)
# Display original and gray-level sliced images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(sliced_image, cmap='gray')
plt.title('Gray Level Slicing')
plt.axis('off')
plt.tight_layout()
plt.show()