import pytest
from image_processing_ajs.io import load_image, save_image
import numpy as np

def test_load_image():
    # Tests if the image is loaded correctly
    image = load_image('path/to/test_image.jpg')
    assert image is not None
    assert isinstance(image, np.ndarray)

def test_save_image():
    test_image = np.zeros((100, 100, 3))  # Create a test image
    result = save_image('saved_image.jpg', test_image)
    assert result is True  # Checks if the image was saved successfully
