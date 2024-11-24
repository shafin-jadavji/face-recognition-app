from face_detection import detect_faces_from_camera_dlib
from utils.display import display_image
from detectors.opencv_detector import OpenCVDetector
from detectors.dlib_detector import DlibDetector    


# Path to the test image
TEST_IMAGE_PATH = "../data/test_image.jpg"

def main():
    """
    Main function to test face detection.
    """

    mode = input("Choose mode (opencv-image/opencv-video/dlib-image/dlib-video): ").strip().lower()

    if mode == "opencv-image":

        detector = OpenCVDetector()

        try:
            image_with_faces = detector.detect_faces(TEST_IMAGE_PATH)
            display_image(image_with_faces, window_name="Detected Faces - OpenCV")
        except FileNotFoundError as e:
            print(e)

    elif mode == "opencv-video":
        detector = OpenCVDetector()
        detector.detect_faces_video()
        
    elif mode == "dlib-image":

        detector = DlibDetector()

        try:
            image_with_faces = detector.detect_faces(TEST_IMAGE_PATH)
            display_image(image_with_faces, window_name="Detected Faces - DLIB")
        except FileNotFoundError as e:
            print(e)

    elif mode == "dlib-video":
        detector = DlibDetector()
        detector.detect_faces_video()

    else:
        print("Invalid mode. Please choose 'opencv-image' or 'opencv-video' or 'dlib-image' or 'dlib-video'.")

if __name__ == "__main__":
    main()
