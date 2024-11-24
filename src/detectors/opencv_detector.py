import cv2

class OpenCVDetector:
    def __init__(self):
        """
        Initialize the OpenCV detector.
        """
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def detect_faces(self, image_path):
        """
        Detect faces in an image using Haar Cascade.
        Args:
            image_path (str): Path to the input image.
        Raises:
            FileNotFoundError: Image at the specified path does not exist.
        Returns:
            image_with_detections (numpy.ndarray): Image with bounding boxes around faces.
        """        
        image = cv2.imread(image_path)

        if image is None:
            raise FileNotFoundError(f"Image at {image_path} not found!")
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        return image

    def detect_faces_video(self):
        """
        Detect faces in a live video stream using Haar Cascade.
        Raises:
            IOError: Cannot open camera.
        Returns:
            None
        """

        # Open the default camera
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            raise IOError("Cannot open camera")
        
        while True:

            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                break
            
            # Convert frame to grayscale (required for Haar Cascade)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #  Detect faces
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw bounding boxes around detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display the resulting frame
            cv2.imshow('Face Detection', frame)

            # Exit loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close all windows
        cap.release()
        cv2.destroyAllWindows()