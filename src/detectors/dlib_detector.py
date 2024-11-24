import dlib
import cv2

class DlibDetector:
    def __init__(self):
        """
        Initialize the Dlib detector.
        """
        self.face_detector = dlib.get_frontal_face_detector()

    def detect_faces(self, image_path):
        """
        Detect faces in an image using DLIB's HOG-based face detector.
        Args:
            image_path (str): Path to the input image.
        Raises:
            FileNotFoundError: Image at the specified path does not exist.
        Returns:
            image_with_detections (numpy.ndarray): Image with bounding boxes around faces.
        """
        # Load DLIB's face detector
        face_detector = dlib.get_frontal_face_detector()

        # Read the input image
        image = cv2.imread(image_path)

        if image is None:
            raise FileNotFoundError(f"Image at {image_path} not found!")

        # Convert image to grayscale (DLIB works better with grayscale images)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_detector(gray)

        # Draw bounding boxes around detected faces
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)    

        return image
    
    def detect_faces_video(self):
        """
        Detect faces in a live video stream using DLIB's HOG-based face detector.
        Raises:
            IOError: Cannot open camera.
        Returns:
            None
        """
        
        # Load DLIB's face detector
        face_detector = dlib.get_frontal_face_detector()

        # Open the default camera
        cap = cv2.VideoCapture(0)

        # Check if the camera opened successfully
        if not cap.isOpened():
            raise IOError("Cannot open camera")

        # Loop over frames from the camera
        while True:

            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                break

            # Convert frame to grayscale (DLIB works better with grayscale images)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = face_detector(gray)

            # Draw bounding boxes around detected faces
            for face in faces:
                x, y, w, h = face.left(), face.top(), face.width(), face.height()
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video Face Detection - DLIB', frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()


