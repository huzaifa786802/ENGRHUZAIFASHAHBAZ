from PIL import Image
import numpy as np
import os

def combine_images(image1_path, image2_path, output_path, orientation='horizontal'):
    """
    Combine two images into one image.
    
    Parameters:
        image1_path (str): Path to the first image
        image2_path (str): Path to the second image
        output_path (str): Path where the combined image will be saved
        orientation (str): 'horizontal' or 'vertical' orientation for combining images
    """
    # Open the images
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)
    
    # Get dimensions
    width1, height1 = img1.size
    width2, height2 = img2.size
    
    # Resize second image to match height of first image if combining horizontally
    # or match width if combining vertically
    if orientation == 'horizontal':
        # Calculate new dimensions for the second image to maintain aspect ratio
        new_height = height1
        new_width = int(width2 * (new_height / height2))
        img2 = img2.resize((new_width, new_height), Image.LANCZOS)
        
        # Create a new image with the combined width and the height of the first image
        new_img = Image.new('RGB', (width1 + new_width, height1))
        
        # Paste the images
        new_img.paste(img1, (0, 0))
        new_img.paste(img2, (width1, 0))
    else:  # vertical
        # Calculate new dimensions for the second image to maintain aspect ratio
        new_width = width1
        new_height = int(height2 * (new_width / width2))
        img2 = img2.resize((new_width, new_height), Image.LANCZOS)
        
        # Create a new image with the width of the first image and the combined height
        new_img = Image.new('RGB', (width1, height1 + new_height))
        
        # Paste the images
        new_img.paste(img1, (0, 0))
        new_img.paste(img2, (0, height1))
    
    # Save the combined image
    new_img.save(output_path)
    print(f"Combined image saved to {output_path}")
    
    return new_img

# Example usage
if __name__ == "__main__":
    # Replace these paths with the actual paths to your images
    image1_path = "breadboard_setup.jpg"  # The breadboard setup image
    image2_path = "pms5003_sensor.jpg"    # The blue PMS5003 sensor image
    output_path = "combined_images.jpg"   # Where to save the result
    
    # Combine images horizontally (side by side)
    # To stack them vertically, change 'horizontal' to 'vertical'
    combined_image = combine_images(image1_path, image2_path, output_path, orientation='horizontal')
    
    # Optional: display the combined image if running in a notebook or environment with display capabilities
    # combined_image.show()