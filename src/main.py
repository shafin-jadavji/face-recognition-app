from face_detection import detect_faces, display_image, detect_faces_from_camera

def main():
    """
    Main function to test face detection.
    """

    mode = input("Choose mode (image/video): ").strip().lower()

    if mode == "image":
        # Path to the test image
        test_image_path = "../data/test_image.jpg"
        
        try:
            image_with_faces = detect_faces(test_image_path)
            display_image(image_with_faces, window_name="Detected Faces")
        except FileNotFoundError as e:
            print(e)
    elif mode == "video":
        detect_faces_from_camera()
    else:
        print("Invalid mode. Please choose 'image' or 'video'.")



if __name__ == "__main__":
    main()
