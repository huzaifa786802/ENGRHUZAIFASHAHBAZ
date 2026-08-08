from PIL import Image
# Use a raw string to avoid issues with backslashes in the file path
image_path = r"D:\BSCOMPUTER ENGINEERING\4th YEAR OF COMPUTER ENGINEERING\7th SEMESTER\DIGITAL IMAGE PROCESSING\PROGRAMS OF DIGITAL IMAGE PROCESSING\Screenshot 2024-10-09 091542.jpg"
# Load the image
image = Image.open(image_path)
# Get the original dimensions
original_width, original_height = image.size
# Calculate the borders
left_right_border = int(0.10 * original_width)
# Calculate the required final size to make it a square (rows = columns)
final_size = original_width + 2 * left_right_border
# Calculate the upper and lower borders to make it a square
upper_lower_border = (final_size - original_height) // 2
# Create a new image with the final size and black borders
new_image = Image.new("RGB", (final_size, final_size), (0, 0, 0))
# Paste the original image in the center with borders
new_image.paste(image, (left_right_border, upper_lower_border))
# Save the new image
new_image.save("image_with_borders.jpg")