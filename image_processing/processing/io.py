# io.py

from skimage.io import imread, imsave

def load_image(image_path):
    """
    Loads an image from a file.

    Parameters:
    image_path (str): The path to the image file to be loaded.

    Returns:
    ndarray: Numpy array representing the loaded image.
    """
  # “try and except” are used to handle exceptions during code execution, allowing a block of code to run and,
  # if an error occurs, handling that error in a controlled manner without interrupting the execution.
    try:
        image = imread(image_path)
        return image
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
    except Exception as e:
        print(f"An error occurred while loading the image: {e}")

def save_image(save_path, image):
    """
    Saves an image to a file.

    Parameters:
    save_path (str): The path where the image will be saved.
    image (ndarray): Numpy array representing the image to be saved.

    Returns:
    bool: True if the image was saved successfully, False otherwise.
    """
  # “try and except” are used to handle exceptions during code execution, allowing a block of code to run and,
  # if an error occurs, handling that error in a controlled manner without interrupting the execution.
    try:
        imsave(save_path, image)
        print(f"Image successfully saved at {save_path}")
        return True
    except Exception as e:
        print(f"An error occurred while saving the image: {e}")
        return False
