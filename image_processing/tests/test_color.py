import pytest
import numpy as np
from image_processing_ajs.color import convert_to_gray

def test_convert_to_gray():
    rgb_image = np.array([[[0, 0, 0], [255, 255, 255]], [[128, 128, 128], [0, 255, 0]]])  # Simple test RGB image
    gray_image = convert_to_gray(rgb_image)
    assert gray_image is not None
    assert gray_image.shape == (2, 2)  # Should be 2D after conversion
