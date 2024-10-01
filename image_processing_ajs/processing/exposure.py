# exposure.py

from skimage.exposure import adjust_gamma, rescale_intensity
import numpy as np

def adjust_gamma_correction(image, gamma=1.0):
    """
    Adjusts the gamma correction of an image.

    Parameters:
    image (ndarray): Input image (can be grayscale or RGB).
    gamma (float): Gamma value for adjustment (gamma < 1 darkens the image, gamma > 1 lightens the image).

    Returns:
    ndarray: Image with adjusted gamma correction.
    """
# “try and except” are used to handle exceptions during code execution, allowing a block of code to run and,
# if an error occurs, handling that error in a controlled manner without interrupting the execution.
    try:
        adjusted_image = adjust_gamma(image, gamma=gamma)
        return adjusted_image
    except Exception as e:
        print(f"An error occurred while adjusting gamma: {e}")
        return np.zeros_like(image)

def rescale_pixel_intensity(image, in_range=(0, 1), out_range=(0, 1)):
    """
    Rescales the intensity of pixel values in an image.

    Parameters:
    image (ndarray): Input image to rescale.
    in_range (tuple): Range of input values (min, max) for rescaling.
    out_range (tuple): Range of output values (min, max) after rescaling.

    Returns:
    ndarray: Image with rescaled pixel intensities.
    """
# “try and except” are used to handle exceptions during code execution, allowing a block of code to run and,
# if an error occurs, handling that error in a controlled manner without interrupting the execution.
    try:
        rescaled_image = rescale_intensity(image, in_range=in_range, out_range=out_range)
        return rescaled_image
    except Exception as e:
        print(f"An error occurred while rescaling intensity: {e}")
        return np.zeros_like(image)
