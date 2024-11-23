from face_detection import detect_faces, display_image, detect_faces_from_camera, detect_faces_dlib, detect_faces_from_camera_dlib

def main():
    """
    Main function to test face detection.
    """

    mode = input("Choose mode (image/video/dlib/dlib-video): ").strip().lower()

    if mode == "image":
        # Path to the test image
        test_image_path = "../data/test_image.jpg"
        
        try:
            image_with_faces = detect_faces(test_image_path)
            display_image(image_with_faces, window_name="Detected Faces - OpenCV")
        except FileNotFoundError as e:
            print(e)
            
    elif mode == "video":
        detect_faces_from_camera()
        
    elif mode == "dlib":
        # Path to the test image
        test_image_path = "../data/test_image.jpg"

        try:
            image_with_faces = detect_faces_dlib(test_image_path)
            display_image(image_with_faces, window_name="Detected Faces - DLIB")
        except FileNotFoundError as e:
            print(e)

    elif mode == "dlib-video":
        detect_faces_from_camera_dlib()

    else:
        print("Invalid mode. Please choose 'image' or 'video'.")



if __name__ == "__main__":
    main()
