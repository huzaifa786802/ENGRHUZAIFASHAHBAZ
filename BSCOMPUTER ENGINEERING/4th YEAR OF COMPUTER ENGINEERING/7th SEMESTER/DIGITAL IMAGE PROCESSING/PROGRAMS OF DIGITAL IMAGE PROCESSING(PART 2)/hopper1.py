from PIL import Image

# List of image filenames
image_filenames = [
    "hopper.jpg",
    "rotated_hopper_270.jpg",
    "rotated_hopper_180.jpg",
    "rotated_hopper_90.jpg",
]

# Open images and create a list
images = [Image.open(filename) for filename in image_filenames]

# Save the images as an animated GIF
images[0].save(
    "animated_hopper.gif",
    save_all=True,
    append_images=images[1:],
    duration=500,  # duration of each frame in milliseconds
    loop=0  # loop forever
)
