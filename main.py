import cv2
from image_processing import extract_pincodes

def capture_image_from_droidcam():
    cap = cv2.VideoCapture(1)
    
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return None

    print("Press 'c' to capture an image.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        cv2.imshow("DroidCam Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            print("Image captured.")
            break

    cap.release()
    cv2.destroyAllWindows()
    return frame

def display_info(image, from_pincode, to_pincode):
    cv2.imshow("Captured Parcel Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    print(f"From Pincode: {from_pincode}")
    print(f"To Pincode: {to_pincode}")

def main():
    image = capture_image_from_droidcam()
    
    if image is None:
        print("Error: Could not capture image.")
        return

    from_pincode, to_pincode = extract_pincodes(image)
    
    display_info(image, from_pincode, to_pincode)

if __name__ == "__main__":
    main()
