import cv2

def display_image(image, window_name="Image"):
    """
    Display an image in a window.
    Args:
        image (numpy.ndarray): Image to display.
        window_name (str): Name of the window.
    """
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()