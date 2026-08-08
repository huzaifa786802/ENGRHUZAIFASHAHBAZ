from PIL import Image, ImageDraw
import math
def create_image1(size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (size-1, size-1)], outline=(0, 0, 0))
    img.save('image1.png')
def create_image2(size):
    side_length = size // 2
    img = Image.new('RGB', (size, size), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(side_length//2, side_length//2), (size-side_length//2-1, size-side_length//2-1)], fill=(255, 255, 255))
    img.save('image2.png')   
size = int(input("Enter the size of the image: "))
create_image1(size)
create_image2(size)