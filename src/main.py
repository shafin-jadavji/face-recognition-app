from recognition import FaceRecognition, FaceRecognitionError
from utils.display import display_image
from utils.image_loader import load_image, ImageLoadError
import sys

WEB_CAM_ID = 0

def main():
    try:
        face_recognition_system = FaceRecognition()

        while True:
            mode = input("Choose mode (add/image/video/quit): ").strip().lower()
            
            if mode == "quit":
                print("Exiting program...")
                break

            if mode not in ["add", "image", "video"]:
                print("Invalid mode. Please choose 'add', 'image', 'video', or 'quit'")
                continue

            try:
                if mode == "add":
                    image_path = input("Enter the path to the image of the known face: ").strip()
                    name = input("Enter the name of the person: ").strip()
                    
                    image = load_image(image_path)
                    face_recognition_system.add_known_face(image, name)
                    print(f"Successfully added {name} to known faces.")
                    
                elif mode == "image":
                    image_path = input("Enter the path to the image to recognize: ").strip()
                    image = load_image(image_path)
                    result_image = face_recognition_system.recognize_faces_in_image(image)
                    display_image(result_image, "Recognized Faces")
                    
                elif mode == "video":
                    video_source = WEB_CAM_ID
                    result_video = face_recognition_system.recognize_faces_in_video(video_source)

            except ImageLoadError as e:
                print(f"Image loading error: {str(e)}")
            except FaceRecognitionError as e:
                print(f"Face recognition error: {str(e)}")
            except Exception as e:
                print(f"Unexpected error: {str(e)}")

    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"Critical error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()