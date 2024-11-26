import face_recognition
import cv2
import os
import json
import numpy as np
from pathlib import Path

class FaceRecognitionError(Exception):
    """Custom exception for face recognition operations"""
    pass

class FaceRecognition:
    def __init__(self, known_faces_path="../data/known_faces.json"):
        self.known_faces_path = known_faces_path
        self.known_encodings = []
        self.known_names = []
        try:
            self.load_known_faces()
        except Exception as e:
            raise FaceRecognitionError(f"Failed to initialize face recognition: {str(e)}")

    def load_known_faces(self):
        try:
            if os.path.exists(self.known_faces_path):
                with open(self.known_faces_path, "r") as file:
                    data = json.load(file)
                    self.known_encodings = [np.array(encoding) for encoding in data["known_encodings"]]
                    self.known_names = data["known_names"]
        except json.JSONDecodeError:
            raise FaceRecognitionError("Invalid JSON format in known faces file")
        except Exception as e:
            raise FaceRecognitionError(f"Error loading known faces: {str(e)}")

    def save_known_faces(self):
        try:
            data = {
                "known_encodings": [encoding.tolist() for encoding in self.known_encodings],
                "known_names": self.known_names,
            }
            os.makedirs(os.path.dirname(self.known_faces_path), exist_ok=True)
            with open(self.known_faces_path, "w") as file:
                json.dump(data, file)
        except Exception as e:
            raise FaceRecognitionError(f"Error saving known faces: {str(e)}")

    def add_known_face(self, image, name):
        try:
            if not isinstance(name, str) or not name.strip():
                raise ValueError("Name must be a non-empty string")
                
            encodings = face_recognition.face_encodings(image)
            if len(encodings) == 0:
                raise FaceRecognitionError("No face found in the image")
            
            self.known_encodings.append(encodings[0])
            self.known_names.append(name)
            self.save_known_faces()
            return True
        except Exception as e:
            raise FaceRecognitionError(f"Error adding known face: {str(e)}")


    def recognize_faces_in_image(self, image):
        """
        Recognize faces in an image object.

        Args:
            image: Image object (numpy array)
        """
        locations = face_recognition.face_locations(image)
        encodings = face_recognition.face_encodings(image, locations)

        for (top, right, bottom, left), encoding in zip(locations, encodings):
            matches = face_recognition.compare_faces(self.known_encodings, encoding)
            name = "Unknown"

            if True in matches:
                match_index = matches.index(True)
                name = self.known_names[match_index]

            # Draw a label with the name
            cv2.rectangle(image, (left, top), (right, bottom), (255, 0, 0), 2)
            cv2.rectangle(image, (left, bottom - 15), (right, bottom), (255, 0, 0), cv2.FILLED)
            # cv2.putText(image, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

            cv2.putText(
                img=image, 
                text=name, 
                org=(left + 6, bottom - 2), 
                fontFace=cv2.FONT_HERSHEY_DUPLEX,
                fontScale=0.5,
                color=(255,255, 255), # white = (255, 255, 255)
                thickness=1
            )

        return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    def recognize_faces_in_video(self, video):
        """
        Recognize faces in a video. This function will continuously process frames from the video.
        Args:
            video (str): Path to the video file.
        """
        try:
            cap = cv2.VideoCapture(video)
            if not cap.isOpened():
                raise ValueError("Error opening video file")

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Recognize faces in the frame
                recognized_frame = self.recognize_faces_in_image(rgb_frame)

                # Display the frame with recognized faces
                cv2.imshow("Recognized Faces", recognized_frame)    

                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        finally:
            cap.release()
            cv2.destroyAllWindows()