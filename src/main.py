from utils.display import display_image
from detectors.opencv_detector import OpenCVDetector
from detectors.dlib_detector import DlibDetector    


# Path to the test image
TEST_IMAGE_PATH = "../data/test_image.jpg"

def display_menu():
    """
    Displays a menu of face detection modes and prompts the user to select one.
    
    Returns:
        str: The selected mode, which can be one of "opencv-image", "opencv-video",
             "dlib-image", or "dlib-video".
    """
        
    menu_options = {
        1: ("opencv-image", "OpenCV Image Detection"),
        2: ("opencv-video", "OpenCV Video Detection"),
        3: ("dlib-image", "Dlib Image Detection"),
        4: ("dlib-video", "Dlib Video Detection")
    }

    print("\nFace Detection Modes:")
    for key, (_, description) in menu_options.items():
        print(f"{key}. {description}")

    while True:
        try:
            choice = int(input("\nSelect mode (1-4): "))
            if 1 <= choice <= 4:
                return menu_options[choice][0]
            print("Please enter a number between 1 and 4")
        except ValueError:
            print("Please enter a valid number")


def process_image_detection(detector, window_name):
    """
    Handle image detection process

    Args:
        detector: OpenCV or DLIB face detector
        window_name: Name to display on window
    """    
    try:
        image_with_faces = detector.detect_faces(TEST_IMAGE_PATH)
        display_image(image_with_faces, window_name=window_name)
    except FileNotFoundError as e:
        print(e)


def main():
    """
    Main function to test face detection.
    """

    mode = display_menu()
    # print("Mode:",mode)

    detectors = {
        "opencv-image": (OpenCVDetector(), "Detected Faces - OpenCV"),
        "opencv-video": (OpenCVDetector(), None),
        "dlib-image": (DlibDetector(), "Detected Faces - DLIB"),
        "dlib-video": (DlibDetector(), None)
    }

    detector, window_name = detectors[mode]

    if mode.endswith("-video"):
        detector.detect_faces_video()
    else:
        process_image_detection(detector, window_name)


if __name__ == "__main__":
    main()
