Parcel Address Extraction

This project extracts the From and To addresses from a parcel image using OCR (Optical Character Recognition). It calculates the distance between the two locations and displays the weight and distance of the parcel.


Project Overview

The Parcel Address Extraction system processes parcel images, extracts the From and To addresses using OCR, and retrieves the corresponding pincodes. The system then calculates the distance between the two pincodes and displays the parcel's weight.


---------------------------------------------------------------------------------------------------------------------


Features:

-Image preprocessing using OpenCV for clarity.

-OCR using Tesseract to extract text.

-Pincode extraction from From and To addresses.

-Distance calculation between two pincodes (can be extended for integration with a distance API).

-Weight measurement integration (from a USB-connected scale).


---------------------------------------------------------------------------------------------------------------------


DEPENDENCIES


This project requires the following Python libraries:

-opencv-python: For image processing and visualization.

-pytesseract: For OCR (Optical Character Recognition).

-requests: If you need to fetch data (e.g., for distance calculation between pincodes).


Additional Tools:

-Tesseract: OCR tool used for text extraction from images. Installation Guide.

Installation

1. Clone the Repository

Clone this repository to your local machine:

    bash: Copy code

        git clone https://github.com/your-username/parcel-address-extraction.git
        cd parcel-address-extraction


2. Create a Virtual Environment (optional but recommended)

Create a virtual environment to isolate your project dependencies:

    bash: Copy code

        python -m venv venv
    
Activate the virtual environment:

    - Windows: bash: Copy code

        .\venv\Scripts\activate

    -Linux/MacOS: bash: Copy code

        source venv/bin/activate


3. Install Dependencies

Install the required Python libraries:

    bash: Copy code

        pip install opencv-python pytesseract requests


4. Install Tesseract

Follow the Tesseract installation guide for your platform:

    -Windows: Download from Tesseract GitHub and install it.

    -Linux: Use the following command: bash: Copy code

        sudo apt install tesseract-ocr

    -MacOS: Use Homebrew: bash: Copy code

        brew install tesseract

Ensure that Tesseract is in your system path, or set the path in image_processing.py (Windows example):

python: Copy code

    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Set your Tesseract path here


---------------------------------------------------------------------------------------------------------------------


ENVIRONMENT SETUP


1. Python Version

Ensure that you are using Python 3.x (preferably 3.7 or higher). You can verify the version with:

bash: Copy code

    python --version


2. IDE Setup

You can use any Python IDE, but we recommend:

VSCode:

    -Install Python extension from the Extensions tab.
    -Use the integrated terminal for managing dependencies.
    -Set the Python interpreter to your virtual environment.

PyCharm:

    -Install the Python plugin (if not already installed).
    -Set the Python interpreter in the settings.


---------------------------------------------------------------------------------------------------------------------


USAGE


-Place the image file (e.g., sample_images/test.png) in the sample_images folder.

-Run the main.py script to start processing:

    bash: Copy code

        python main.py

Example Output:

    vbnet: Copy code

        Extracted Text:
        From: John Doe, 123 Street, City, XYZ
        To: Jane Smith, 456 Avenue, City, ABC

        From Pincode: 123456
        To Pincode: 654321


---------------------------------------------------------------------------------------------------------------------


TESSERACT SETUP


If you're using Windows, ensure that the Tesseract executable path is correctly specified in the image_processing.py script:

python: Copy code

    import pytesseract
    # Set the path to Tesseract executable (adjust the path as per your installation)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


For Linux or MacOS, Tesseract should be automatically available after installation.


---------------------------------------------------------------------------------------------------------------------


This README provides all the necessary details to set up, run, and extend the Parcel Address Extraction project. You can use this template to track the progress and install dependencies