import pytest
import numpy as np
from image_processing_ajs.plot import show_image, show_images_side_by_side

def test_show_image():
    image = np.zeros((100, 100))  # Simple test image
    try:
        show_image(image, title='Test Image')
    except Exception as e:
        pytest.fail(f"show_image raised an exception: {e}")

def test_show_images_side_by_side():
    images = [np.zeros((100, 100)), np.ones((100, 100))]  # Create test images
    titles = ['Black Image', 'White Image']
    try:
        show_images_side_by_side(images, titles)
    except Exception as e:
        pytest.fail(f"show_images_side_by_side raised an exception: {e}")
