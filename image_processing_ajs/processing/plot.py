# plot.py

import matplotlib.pyplot as plt

def show_image(image, title='Image', cmap=None):
    """
    Displays an image using matplotlib.

    Parameters:
    image (ndarray): The image to be displayed.
    title (str): The title of the display window.
    cmap (str): The colormap to be used (optional).

    Returns:
    None
    """
    plt.figure(figsize=(8, 6))
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis('off')  # Removes the axes
    plt.show()

def show_images_side_by_side(images, titles):
    """
    Displays multiple images side by side.

    Parameters:
    images (list): List of images to be displayed.
    titles (list): List of titles corresponding to the images.

    Returns:
    None
    """
    num_images = len(images)
    plt.figure(figsize=(15, 5))
    
    for i in range(num_images):
        plt.subplot(1, num_images, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')  # Removes the axes
    
    plt.show()
