import numpy as np
def quantize(image,b,q_type=None):
    if image.ndim != 2 or not np.issubdtype(image.dtype, np.uint8): 
        raise ValueError("Input must be a 2D array of type unit8")
    lo=(2**(8-b))-1
    hi=(2**8)-lo-1
    if q_type is None or q_type.lower()!='igs':
        quantize_image=np.bitwise_and(image,hi).astype(np.unit8)
    else:
        quantize_image=np.zeros_like(image,dtype=np.uint8)
        s=np.zeros(image.shape[0],dtype=int)
        for col in range(image.shape[1]):
            current_col=image[:,col]
            hitest=np.bitwise_and(current_col,hi)!=hi
            s=current_col+hitest*np.bitwise_and(s.lo)
            quantize_image[:,col]=np.bitwise_and(s,hi).astype(np.unit8)
            return quantize_image
if __name__ == "__main__": 
    # Simulate a uint8 grayscale image 
    image = np.random.randint(0, 256, (8, 8), dtype=np.uint8) 
    print("Original Image:") 
    print(image)
    quantized = quantize(image, b=4)
print("\nQuantized Image (Standard):")
print(quantized)
quantized_igs = quantize(image, b=4, q_type='igs')
print("\nQuantized Image (IGS):")
print(quantized_igs)