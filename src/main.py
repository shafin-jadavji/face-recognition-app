from recognition import FaceRecognition
from utils.display import display_image

def main():
    face_recognition_system = FaceRecognition()

    mode = input("Choose mode (add/recognize): ").strip().lower()

    if mode == "add":
        image_path = input("Enter the path to the image of the known face: ").strip()
        name = input("Enter the name of the person: ").strip()
        face_recognition_system.add_known_face(image_path, name)
    elif mode == "recognize":
        image_path = input("Enter the path to the image to recognize: ").strip()
        result_image = face_recognition_system.recognize_faces_in_image(image_path)
        display_image(result_image, "Recognized Faces")
    else:
        print("Invalid mode. Please choose 'add' or 'recognize'.")

if __name__ == "__main__":
    main()