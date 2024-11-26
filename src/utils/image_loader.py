import cv2
import face_recognition
from pathlib import Path

class ImageLoadError(Exception):
    """Custom exception for image loading failures"""
    pass

def load_image(image_path):
    """
    Load an image from path with error handling
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        image: Loaded image object
        
    Raises:
        ImageLoadError: If image cannot be loaded or path is invalid
    """
    try:
        if not Path(image_path).exists():
            raise FileNotFoundError(f"Image file not found: {image_path}")
            
        image = face_recognition.load_image_file(image_path)
        if image is None:
            raise ImageLoadError(f"Failed to load image: {image_path}")
            
        return image
    except Exception as e:
        raise ImageLoadError(f"Error loading image: {str(e)}")
