import pytest
import numpy as np
from image_processing_ajs.exposure import adjust_gamma_correction, rescale_intensity

def test_adjust_gamma_correction():
    image = np.array([[0, 0.5, 1], [0, 0.5, 1]])  # Simple test image
    adjusted_image = adjust_gamma_correction(image, gamma=1.5)
    assert adjusted_image is not None
    assert adjusted_image.shape == image.shape  # Check the shape remains the same

def test_rescale_intensity():
    image = np.array([[0, 255], [128, 64]])  # Simple test image
    rescaled_image = rescale_intensity(image)
    assert rescaled_image is not None
    assert rescaled_image.min() >= 0 and rescaled_image.max() <= 1  # Check intensity scaling
