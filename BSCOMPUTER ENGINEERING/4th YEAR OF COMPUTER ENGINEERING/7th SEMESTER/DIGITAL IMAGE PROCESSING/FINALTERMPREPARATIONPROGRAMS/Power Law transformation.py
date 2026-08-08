import cv2
import numpy as np
# Load the image
img = cv2.imread('Screenshot 2024-10-26 200104.jpg', cv2.IMREAD_GRAYSCALE)
# Define the gamma values
gamma_values = [0.2, 0.5, 1.2, 1.8]
# Apply Power Law transformation for each gamma value
for gamma in gamma_values:
    # Convert image to float type
    img_float = img.astype(np.float32) / 255.0
    # Apply Power Law transformation
    img_gamma = np.power(img_float, gamma)
    # Convert image back to uint8 type
    img_gamma = (img_gamma * 255.0).astype(np.uint8)
    # Display the image
    cv2.imshow(f'Gamma: {gamma}', img_gamma)
    cv2.waitKey(0)
# Close all windows
cv2.destroyAllWindows()