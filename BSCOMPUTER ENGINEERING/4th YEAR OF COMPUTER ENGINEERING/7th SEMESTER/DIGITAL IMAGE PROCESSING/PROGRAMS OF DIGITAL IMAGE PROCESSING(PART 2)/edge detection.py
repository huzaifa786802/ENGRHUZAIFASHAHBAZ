from PIL import Image, ImageFilter
# Opening the image
image = Image.open("sample image.jpg")
# Converting the image to grayscale (required for edge detection)
image = image.convert("L")
# Applying edge detection
image = image.filter(ImageFilter.FIND_EDGES)
# Saving the processed image
image.save("Edge_Sample.png")