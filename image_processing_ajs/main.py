from image_processing_ajs.processing.color import convert_to_grayscale
from image_processing_ajs.processing.io import load_image, save_image
from image_processing_ajs.processing.measure import detect_edges, label_components, calculate_properties
from image_processing_ajs.processing.exposure import adjust_gamma_correction, rescale_intensity  # Importing exposure functions
from image_processing_ajs.processing.plot import show_image, show_images_side_by_side  # Importing plotting functions
import numpy as np
from PIL import Image
from skimage import img_as_ubyte

def is_valid_image(path):
    try:
        img = Image.open(path)
        img.verify()  # Verifies if the file is a valid image
        return True
    except (IOError, SyntaxError) as e:
        print(f"Error verifying the image: {e}")
        return False

def save_properties_to_txt(properties, file_path):
    try:
        with open(file_path, 'w') as f:
            for prop in properties:
                f.write(str(prop) + '\n')
        print(f"Properties successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving properties: {e}")

def main():
    try:
        image_path = str(input('Enter the location and identification of the image: ')).strip()
        # Check if the file is a valid image
        # image_path = 'C:/workspace/ntt-data-python-dio/image-processing-ajs-package/original_image.jpg'
        if not is_valid_image(image_path):
            raise ValueError("The file is not a valid image.")

        # Load the image
        image = load_image(image_path)
        if image is None:
            raise ValueError("The image could not be loaded. Check the file path.")
        
        # Check if the image is a NumPy array
        if not isinstance(image, np.ndarray):
            raise TypeError("The loaded object is not a valid image.")
        
        # Convert to grayscale
        gray_image = convert_to_grayscale(image)
        
        # Check if gray_image is a NumPy array
        if not isinstance(gray_image, np.ndarray):
            raise TypeError("The converted object is not a valid image.")
        
        # Convert the image to uint8
        gray_image = (gray_image * 255).astype(np.uint8)

        # Adjust gamma correction
        gamma_corrected_image = adjust_gamma_correction(image, gamma=1.5)
        print("Gamma correction applied successfully.")
        
        # Convert to uint8 before saving
        gamma_corrected_image_uint8 = img_as_ubyte(gamma_corrected_image)

        # Rescale the image intensity
        rescaled_image = rescale_intensity(image, in_range=(50, 200), out_range=(0, 255))
        print("Image intensity successfully rescaled.")
        
        # Normalize values to ensure they are within [0, 1] range
        rescaled_image_normalized = rescale_intensity(rescaled_image, out_range=(0, 1))

        # Convert to uint8 before saving
        rescaled_image_uint8 = img_as_ubyte(rescaled_image_normalized)
        
        # Detect edges in the grayscale image
        edges_image = detect_edges(gray_image)
        print("Edges successfully detected.")
        
        # Convert the image to uint8
        edges_image = (edges_image * 255).astype(np.uint8)

        # Label connected components in the edge-detected image
        labeled_image = label_components(edges_image)
        print("Connected components successfully labeled.")
        
        # Convert the image to uint8
        labeled_image = (labeled_image * 255).astype(np.uint8)

        # Calculate properties of the labeled components
        properties = calculate_properties(labeled_image)
        print(f"Properties successfully calculated.")
        
        # Save the converted grayscale image
        if not save_image('gray_image.jpg', gray_image):
            raise ValueError("The image could not be saved. Check the file path and image format.")

        # Save the gamma corrected image
        if not save_image('gamma_image.jpg', gamma_corrected_image_uint8):
            raise ValueError("The gamma corrected image could not be saved.")
        
        # Save the rescaled intensity image
        if not save_image('rescaled_image.jpg', rescaled_image_uint8):
            raise ValueError("The rescaled intensity image could not be saved.")

        # Save the edge-detected image
        if not save_image('edges_image.jpg', edges_image):
            raise ValueError("The edge-detected image could not be saved.")
        
        # Save the labeled image
        if not save_image('labeled_image.jpg', labeled_image):
            raise ValueError("The labeled image could not be saved.")
        
        # Save the properties
        save_properties_to_txt(properties, 'properties_image.txt')

        # Display the generated images side by side
        show_images_side_by_side(
            [image, gray_image, gamma_corrected_image_uint8, rescaled_image_uint8],
            titles=["Original", "Gray Scale", "Gamma Corrected", "Rescaled Intensity"]
        )

        # Display the other generated images individually
        show_image(edges_image, title="Edges Detected")
        show_image(labeled_image, title="Labeled Components")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
