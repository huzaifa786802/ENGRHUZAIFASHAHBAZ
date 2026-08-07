import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure
from scipy import ndimage
def preprocess_image(image):
    """Convert image to grayscale and float32 format"""
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return np.float32(image)
def remove_noise(image, kernel_size=5):
    """Apply noise removal techniques"""
    denoised = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    denoised = cv2.medianBlur(denoised.astype(np.uint8), kernel_size)
    return np.float32(denoised)
def enhance_contrast(image):
    """Apply CLAHE enhancement"""
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_eq = clahe.apply(image.astype(np.uint8))
    return np.float32(clahe_eq)
def normalize_image(image):
    """Normalize image to 0-1 range"""
    normalized = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    return normalized
def detect_edges(image):
    """Apply Canny edge detection"""
    edges = cv2.Canny(image.astype(np.uint8), 50, 150)
    return edges
def apply_morphological_operations(image):
    """Apply morphological operations"""
    kernel = np.ones((5,5), np.uint8)
    dilated = cv2.dilate(image.astype(np.uint8), kernel, iterations=1)
    eroded = cv2.erode(image.astype(np.uint8), kernel, iterations=1)
    return dilated, eroded
def process_and_display_xray(image_path):
    # Read image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not read the image")
    # Process image
    preprocessed = preprocess_image(image)
    denoised = remove_noise(preprocessed)
    enhanced = enhance_contrast(denoised)
    normalized = normalize_image(enhanced)
    edges = detect_edges(normalized)
    dilated, eroded = apply_morphological_operations(normalized)
    # Create figure for visualization
    plt.figure(figsize=(20, 10))
    # Original
    plt.subplot(231)
    plt.imshow(preprocessed, cmap='gray')
    plt.title('Original Grayscale')
    plt.axis('off')
    # Denoised
    plt.subplot(232)
    plt.imshow(denoised, cmap='gray')
    plt.title('Denoised')
    plt.axis('off')
    # Enhanced
    plt.subplot(233)
    plt.imshow(enhanced, cmap='gray')
    plt.title('CLAHE Enhanced')
    plt.axis('off')
    # Normalized
    plt.subplot(234)
    plt.imshow(normalized, cmap='gray')
    plt.title('Normalized')
    plt.axis('off')
    # Edges
    plt.subplot(235)
    plt.imshow(edges, cmap='gray')
    plt.title('Canny Edges')
    plt.axis('off')
    # Morphological
    plt.subplot(236)
    plt.imshow(dilated, cmap='gray')
    plt.title('Dilated')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    return {
        'preprocessed': preprocessed,
        'denoised': denoised,
        'enhanced': enhanced,
        'normalized': normalized,
        'edges': edges,
        'dilated': dilated,
        'eroded': eroded
    }
# Run the processing
try:
    # Save the current image as a temporary file
    cv2.imwrite('temp_xray.jpg', cv2.imread('LUNGSEGMENTATIONCHESTX-RAYS.jpg'))
    # Process the image
    results = process_and_display_xray('temp_xray.jpg')
    print("Processing completed successfully!")
except Exception as e:
    print(f"An error occurred: {str(e)}")