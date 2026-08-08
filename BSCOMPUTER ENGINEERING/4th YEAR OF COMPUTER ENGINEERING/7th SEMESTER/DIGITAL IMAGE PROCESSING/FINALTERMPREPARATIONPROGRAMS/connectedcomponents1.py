import cv2
import matplotlib.pyplot as plt
# Load the image with double backslashes for the Windows path
image = cv2.imread('D:\\BSCOMPUTER ENGINEERING\\4th YEAR OF COMPUTER ENGINEERING\\7th SEMESTER\\DIGITAL IMAGE PROCESSING\\PROGRAMS OF DIGITAL IMAGE PROCESSING\\Screenshot 2024-10-16 192325.jpg')
# Check if the image is loaded properly
if image is None:
    print("Error: Could not load the image. Check the path.")
else:
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply thresholding (binary threshold)
    _, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    # Perform connected components analysis
    num_labels, labels_im = cv2.connectedComponents(thresholded_image)
    # Display the results
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 3, 2)
    plt.title("Grayscale Image")
    plt.imshow(gray_image, cmap='gray')
    plt.subplot(1, 3, 3)
    plt.title("Thresholded Image with Connected Components")
    plt.imshow(labels_im, cmap='nipy_spectral')
    plt.show()
    print(f'Number of connected components: {num_labels}')