# measure.py

from skimage.measure import label, regionprops
from skimage.feature import canny
import numpy as np

def label_components(binary_image):
    """
    Labels the connected components in a binary image.

    Parameters:
    binary_image (ndarray): Binary image (with values 0 and 1) for labeling connected components.

    Returns:
    ndarray: Labeled array where each connected component receives a unique label.
    """
# “try and except” are used to handle exceptions during code execution, allowing a block of code to run and,
# if an error occurs, handling that error in a controlled manner without interrupting the execution.
    try:
        labels = label(binary_image)
        return labels
    except Exception as e:
        print(f"An error occurred while labeling the components: {e}")
        return None

def calculate_properties(labels):
    """
    Calculates the properties of labeled objects, such as area, perimeter, etc.

    Parameters:
    labels (ndarray): Labeled array with connected components.

    Returns:
    list: List of properties for each labeled object.
    """
# “try and except” are used to handle exceptions during code execution, allowing a block of code to run and,
# if an error occurs, handling that error in a controlled manner without interrupting the execution.
    try:
        properties = regionprops(labels)
        return properties
    except Exception as e:
        print(f"An error occurred while calculating the properties: {e}")
        return []

def detect_edges(image, sigma=1.0):
    """
    Performs edge detection on an image using the Canny algorithm.

    Parameters:
    image (ndarray): Input image (grayscale) for edge detection.
    sigma (float): Smoothing parameter for the image (standard deviation of the Gaussian filter).

    Returns:
    ndarray: Binary image with detected edges.
    """
# “try and except” are used to handle exceptions during code execution, allowing a block of code to run and,
# if an error occurs, handling that error in a controlled manner without interrupting the execution.
    try:
        edges = canny(image, sigma=sigma)
        return edges
    except Exception as e:
        print(f"An error occurred while detecting edges: {e}")
        return np.zeros_like(image)
