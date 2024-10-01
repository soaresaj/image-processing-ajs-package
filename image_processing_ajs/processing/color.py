# color.py

from skimage.color import rgb2gray
import numpy as np

def convert_to_grayscale(rgb_image):
    """
    Converts a color image (RGB) to grayscale.

    Parameters:
    rgb_image (ndarray): Color image in RGB format.

    Returns:
    ndarray: Grayscale image.
    """
# “try and except” are used to handle exceptions during code execution, allowing a block of code to run and,
# if an error occurs, handling that error in a controlled manner without interrupting the execution.
    try:
        gray_image = rgb2gray(rgb_image)
        return gray_image
    except Exception as e:
        print(f"An error occurred while converting the image to grayscale: {e}")
        return np.zeros((rgb_image.shape[0], rgb_image.shape[1]))
