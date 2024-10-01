# Image Processing AJS

## Description
***"image_processing_ajs"*** is an image processing package developed in Python that offers a variety of functionalities for image manipulation and analysis. This package utilizes popular libraries such as scikit-image and matplotlib, making it easy to perform common image processing tasks.

### Package Structure
```bash
image_processing_ajs/  
├── processing/                        # Main package directory  
│   ├── __init__.py                    # Marks this directory as a Python package  
│   ├── io.py                          # Loads and saves images  
│   ├── measure.py                     # Labels and measures connected components  
│   ├── exposure.py                    # Adjusts intensity and gamma correction  
│   ├── color.py                       # Converts colored images to grayscale  
│   └── plot.py                        # Functions for visualizing results  
├── tests/                             # Directory for tests  
│   ├── __init__.py                    # Marks this directory as a Python package  
│   ├── test_io.py                     # Tests for loads and saves images  
│   ├── test_measure.py                # Tests for labels and measures connected components  
│   ├── test_exposure.py               # Tests for adjusts intensity and gamma correction  
│   ├── test_color.py                  # Tests for converts colored images to grayscale  
│   └── test_plot.py                   # Tests for functions for visualizing results  
├── README.md                          # Basic documentation  
├── setup.py                           # Setup script for setuptools  
└── requirements.txt                   # Dependencies file  
```
### Package Modules
***“io.py”:***  
Uses the functions “skimage.io.imread()” and “skimage.io.imsave()” to load and save images in various formats such as JPG, PNG, TIFF, etc.

***“measure.py”:***  
Uses “skimage.measure.label()” to label connected components in a binary image.  
Uses “skimage.measure.regionprops()” to calculate properties of labeled objects, such as area, perimeter, etc.  
Uses “skimage.feature.canny()” to perform edge detection using the Canny algorithm.  

***“exposure.py”:***  
Uses “skimage.exposure.adjust_gamma()” to adjust the gamma correction of an image.  
Uses “skimage.exposure.rescale_intensity()” to rescale the intensity of pixel values.  

***“color.py”:***  
Uses “skimage.color.rgb2gray()” to convert colored images (RGB) to grayscale.  

***“plot.py”:***  
Uses functions “show_image()” and “show_images_side_by_side()” from the “matplotlib” library to display the results from the “io”, “measure”, “exposure”, and “color” modules.  

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install image_processing_ajs:  
```bash  
pip install image_processing_ajs
```  
If you are developing the package locally, clone the repository and install the dependencies:  
```bash  
git clone https://github.com/soaresaj/image-processing-ajs-package
cd image_processing_ajs
pip install -r requirements.txt
```  
## Usage
An example of how to use the package:  
```python
from image_processing_ajs import io, measure, exposure, color, plot

# Load an image
image = io.imread('path/to/image.jpg')

# Adjust the image gamma correction
adjusted_image = exposure.adjust_gamma(image, gamma=1.5)

# Convert the image to grayscale
gray_image = color.rgb2gray(image)

# Label connected components
labels = measure.label(gray_image)

# Display the results
plot.show_image(image)
```
## Tests
The package contains a test directory where you can find test cases to ensure the proper functionality of the features.

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

## Author
Antonio José Soares

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.
