import face_recognition
import cv2
import os
import json
import numpy as np

class FaceRecognition:
    def __init__(self, known_faces_path="../data/known_faces.json"):
        self.known_faces_path = known_faces_path
        self.known_encodings = []
        self.known_names = []
        self.load_known_faces()

    def load_known_faces(self):
        """
        Load known faces and their encodings from a JSON file.
        """
        if os.path.exists(self.known_faces_path):
            with open(self.known_faces_path, "r") as file:
                data = json.load(file)
                self.known_encodings = [np.array(encoding) for encoding in data["encodings"]]
                self.known_names = data["names"]
        else:
            print(f"No known faces file found at {self.known_faces_path}. Starting fresh.")

    def save_known_faces(self):
        """
        Save known faces and their encodings to a JSON file.
        """
        data = {
            "encodings": [encoding.tolist() for encoding in self.known_encodings],
            "names": self.known_names,
        }
        print("Data",data)
        with open(self.known_faces_path, "w") as file:
            json.dump(data, file)

    def add_known_face(self, image_path, name):
        """
        Add a new known face from an image.

        Args:
            image_path (str): Path to the image of the face.
            name (str): Name of the person.
        """
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            self.known_encodings.append(encodings[0])
            self.known_names.append(name)
            self.save_known_faces()
            print(f"Added {name} to known faces.")
            print("Encodings:",self.known_encodings)
        else:
            print("No face found in the image.")

    def recognize_faces_in_image(self, image_path):
        """
        Recognize faces in an image.

        Args:
            image_path (str): Path to the image with unknown faces.

        Returns:
            numpy.ndarray: The image with recognized faces labeled.
        """
        image = face_recognition.load_image_file(image_path)
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
            cv2.putText(image, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    

