import cv2
import numpy as np
import matplotlib.pyplot as plt
# Step 1: Load the RGB image
image_path = ('RGB Smoothning.jpg')  # Replace this with your file path
image = cv2.imread(image_path)  # Read the image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR (OpenCV format) to RGB
# Display the original image
plt.figure()
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')
# Step 2: Add salt-and-pepper noise
def add_salt_pepper_noise(image, noise_level):
    noisy_image = image.copy()  # Make a copy of the image to modify
    num_pixels = int(noise_level * image.size * 0.5)  # Half for salt, half for pepper
    # Add salt (white pixels)
    salt_coords = [np.random.randint(0, dim, num_pixels) for dim in image.shape[:2]]
    noisy_image[salt_coords[0], salt_coords[1], :] = 255  # Set to white
    # Add pepper (black pixels)
    pepper_coords = [np.random.randint(0, dim, num_pixels) for dim in image.shape[:2]]
    noisy_image[pepper_coords[0], pepper_coords[1], :] = 0  # Set to black
    return noisy_image
# Apply salt-and-pepper noise with 12% corruption
noisy_image = add_salt_pepper_noise(image, 0.12)
# Display the noisy image
plt.figure()
plt.imshow(noisy_image)
plt.title("Noisy Image")
plt.axis('off')
# Step 3: Create the average filter
avg_filter = np.ones((5, 5)) / 25.0  # The filter is a 5x5 matrix where all values are 1/25
# Step 4: Apply the filter to each color channel
# Separate the Red, Green, and Blue channels
R = noisy_image[:, :, 0]
G = noisy_image[:, :, 1]
B = noisy_image[:, :, 2]
# Use OpenCV's filter2D to apply the average filter
R_smooth = cv2.filter2D(R, -1, avg_filter)  # Smooth the Red channel
G_smooth = cv2.filter2D(G, -1, avg_filter)  # Smooth the Green channel
B_smooth = cv2.filter2D(B, -1, avg_filter)  # Smooth the Blue channel
# Step 5: Combine the smoothed channels back into one image
smoothed_image = cv2.merge([R_smooth, G_smooth, B_smooth])
# Step 6: Display the results
plt.figure(figsize=(10, 5))
# Show noisy image
plt.subplot(1, 2, 1)
plt.imshow(noisy_image)
plt.title("Noisy Image")
plt.axis('off')
# Show smoothed image
plt.subplot(1, 2, 2)
plt.imshow(smoothed_image.astype(np.uint8))
plt.title("Smoothed Image")
plt.axis('off')
plt.show()
# Step 7: Visualize each channel
plt.figure(figsize=(15, 5))
# Red channel
plt.subplot(1, 3, 1)
plt.imshow(R_smooth, cmap='gray')
plt.title("Smoothed Red Channel")
plt.axis('off')
# Green channel
plt.subplot(1, 3, 2)
plt.imshow(G_smooth, cmap='gray')
plt.title("Smoothed Green Channel")
plt.axis('off')
# Blue channel
plt.subplot(1, 3, 3)
plt.imshow(B_smooth, cmap='gray')
plt.title("Smoothed Blue Channel")
plt.axis('off')
plt.show()