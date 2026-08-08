import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
image = cv2.imread("Screenshot 2024-10-25 103016.jpg", cv2.IMREAD_GRAYSCALE)
# Calculate the histogram of the image
hist, bins = np.histogram(image.flatten(), 256, [0, 256])
# Save the histogram as Figure_1.jpg
plt.figure()
plt.hist(image.flatten(), 256, [0, 256])
plt.title("Histogram of the Image")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.savefig("Figure_1.jpg")
# Calculate the probability density function (PDF)
rows, cols = image.shape
pdf = hist / (rows * cols)
# Save the PDF as Figure_2.jpg
plt.figure()
plt.plot(pdf)
plt.title("Probability Density Function")
plt.xlabel("Pixel Intensity")
plt.ylabel("Probability")
plt.savefig("Figure_2.jpg")
# Calculate the cumulative density function (CDF)
cdf = np.cumsum(pdf)
# Save the CDF as Figure_3.jpg
plt.figure()
plt.plot(cdf)
plt.title("Cumulative Density Function")
plt.xlabel("Pixel Intensity")
plt.ylabel("Cumulative Probability")
plt.savefig("Figure_3.jpg")
# Multiply the Cumulative PDF with 255 to find the transformation function
transform_function = cdf * 255
# Save the transformation function as Figure_4.jpg
plt.figure()
plt.plot(transform_function)
plt.title("Transformation Function")
plt.xlabel("Pixel Intensity")
plt.ylabel("Output Intensity")
plt.savefig("Figure_4.jpg")
# Apply the transformation function to the image
equalized_image = np.uint8(np.interp(image.flatten(), np.arange(256), transform_function))
equalized_image = np.reshape(equalized_image, image.shape)
# Save the contrast enhanced image as Figure_5.jpg
cv2.imwrite("Figure_5.jpg", equalized_image)
# Calculate the histogram of the output image
hist, bins = np.histogram (equalized_image.flatten(), 256, [0, 256])
# Save the histogram of the output image as Figure_6.jpg
plt.figure()
plt.hist(equalized_image.flatten(), 256, [0, 256])
plt.title("Histogram of the Equalized Image")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.savefig("Figure_6.jpg")