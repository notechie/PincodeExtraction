import pytesseract
import re
import cv2

# def capture_image(image_path=""):
#     # Read the image from the provided path
#     image = cv2.imread(image_path)
    
#     # Check if image was loaded
#     if image is None:
#         raise FileNotFoundError(f"Image at path '{image_path}' not found.")
    
#     # Convert image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     # Apply thresholding to make text more clear
#     _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

#     return thresh  # Return the preprocessed image

def extract_pincodes(image):
    # Use Tesseract to extract text from the preprocessed image
    text = pytesseract.image_to_string(image)
    
    # Print the extracted text for debugging
    print("Extracted Text:")
    print(text)
    
    # Initialize variables to store the pincodes
    from_pincode = "Not found"
    to_pincode = "Not found"

    # Split the text into lines for easier processing
    lines = text.splitlines()

    # Flags to track if we have already found each pincode
    found_to = False
    found_from = False

    # Loop through each line to find keywords and pincodes
    for line in lines:
        # Convert the line to lowercase to make the search case-insensitive
        line_lower = line.lower()
        
        # Check for 'to' keyword and pincode if not already found
        if "to" in line_lower and not found_to:
            # Search for a 6-digit pincode in this line and following lines if needed
            pincode_match = re.search(r'\b\d{6}\b', line)
            if pincode_match:
                to_pincode = pincode_match.group(0)
                found_to = True
            else:
                # If not found in the same line, check the next few lines
                for next_line in lines[lines.index(line) + 1:]:
                    pincode_match = re.search(r'\b\d{6}\b', next_line)
                    if pincode_match:
                        to_pincode = pincode_match.group(0)
                        found_to = True
                        break  # Stop searching once found

        # Check for 'from' keyword and pincode if not already found
        elif "from" in line_lower and not found_from:
            # Search for a 6-digit pincode in this line and following lines if needed
            pincode_match = re.search(r'\b\d{6}\b', line)
            if pincode_match:
                from_pincode = pincode_match.group(0)
                found_from = True
            else:
                # If not found in the same line, check the next few lines
                for next_line in lines[lines.index(line) + 1:]:
                    pincode_match = re.search(r'\b\d{6}\b', next_line)
                    if pincode_match:
                        from_pincode = pincode_match.group(0)
                        found_from = True
                        break  # Stop searching once found

    # Return the found pincodes
    return from_pincode, to_pincode
