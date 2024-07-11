import sys
import cv2
import numpy as np
import easyocr

def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Resize the image
    scale_percent = 200  # Percentage to increase the size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

    # Convert to grayscale
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Remove noise
    denoised = cv2.fastNlMeansDenoising(binary, h=30)

    return denoised

def ocr_with_easyocr(image):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)
    extracted_text = ' '.join([text for _, text, _ in result])
    return extracted_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_image.py <image_path>")
        sys.exit(1)

    input_image_path = sys.argv[1]

    # Preprocess the image
    preprocessed_image = preprocess_image(input_image_path)

    # Perform OCR on the preprocessed image
    extracted_text = ocr_with_easyocr(preprocessed_image)
    print(extracted_text)
