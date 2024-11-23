import dlib
import cv2

def detect_faces(image_path):
    """
    Detect faces in an image using Haar Cascade.

    Args:
        image_path (str): Path to the input image.

    Returns:
        image_with_detections (numpy.ndarray): Image with bounding boxes around faces.
    """
    # Load the Haar Cascade model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the input image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image at {image_path} not found!")

    # Convert image to grayscale (required for Haar Cascade)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw bounding boxes around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return image

def detect_faces_from_camera():
    """
    Detect faces in a live video stream using Haar Cascade.

    Returns:
        None
    """
    # Load the Haar Cascade model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open the default camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open camera")
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw bounding boxes around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Face Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def detect_faces_dlib(image_path):
    """
    Detect faces in an image using DLIB's HOG-based face detector.

    Args:
        image_path (str): Path to the input image.

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

def detect_faces_from_camera_dlib():
    """
    Detect faces in a live video stream using DLIB's HOG-based face detector.

    Returns:
        None
    """
    # Load DLIB's face detector
    face_detector = dlib.get_frontal_face_detector()

    # Open the default camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Cannot open camera")
    
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
        cv2.imshow('Face Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def display_image(image, window_name="Image"):
    """
    Display an image using OpenCV.

    Args:
        image (numpy.ndarray): Image to display.
        window_name (str): Name of the display window.
    """
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
