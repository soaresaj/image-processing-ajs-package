import pytest
import numpy as np
from image_processing_ajs.io import load_image, save_image

def test_load_image():
    # Test if the image loads correctly
    image = load_image('path/to/test_image.jpg')
    assert image is not None
    assert isinstance(image, np.ndarray)

def test_save_image():
    test_image = np.zeros((100, 100, 3))  # Create a test image
    result = save_image('saved_image.jpg', test_image)
    assert result is True  # Check if the image was saved successfully
