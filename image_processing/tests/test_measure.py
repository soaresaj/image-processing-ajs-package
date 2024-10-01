import pytest
import numpy as np
from image_processing_ajs.measure import label_components, calculate_properties, detect_edges

def test_label_components():
    binary_image = np.array([[1, 1, 0], [0, 1, 0], [0, 0, 0]])
    labels = label_components(binary_image)
    assert labels is not None
    assert np.max(labels) == 1  # There should be one label

def test_calculate_properties():
    labels = np.array([[1, 1, 0], [0, 1, 0], [0, 0, 0]])
    properties = calculate_properties(labels)
    assert len(properties) == 1  # There should be one property for the labeled object

def test_detect_edges():
    image = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])  # Simple test image
    edges = detect_edges(image)
    assert edges is not None
    assert np.sum(edges) > 0  # There should be detected edges
