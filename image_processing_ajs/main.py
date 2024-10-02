from image_processing_ajs.processing.color import convert_to_grayscale
from image_processing_ajs.processing.io import load_image, save_image
from image_processing_ajs.processing.measure import detect_edges, label_components, calculate_properties
from image_processing_ajs.processing.exposure import adjust_gamma_correction, rescale_intensity  # Importação das funções de exposure
from image_processing_ajs.processing.plot import show_image, show_images_side_by_side  # Importa as funções de plotagem
import numpy as np
from PIL import Image
from skimage import img_as_ubyte

def is_valid_image(path):
    try:
        img = Image.open(path)
        img.verify()  # Verifica se é uma imagem válida
        return True
    except (IOError, SyntaxError) as e:
        print(f"Erro ao verificar a imagem: {e}")
        return False

def save_properties_to_txt(properties, file_path):
    try:
        with open(file_path, 'w') as f:
            for prop in properties:
                f.write(str(prop) + '\n')
        print(f"Propriedades salvas com sucesso em {file_path}")
    except Exception as e:
        print(f"Erro ao salvar propriedades: {e}")

def main():
    try:
        image_path = str(input('Entrar com a localização e a identificação da imagem: ')).strip()
        # Verifique se o arquivo é uma imagem válida
        #image_path = 'C:/workspace/ntt-data-python-dio/image-processing-ajs-package/original_image.jpg'
        if not is_valid_image(image_path):
            raise ValueError("O arquivo não é uma imagem válida.")

        # Carregar a imagem
        image = load_image(image_path)
        if image is None:
            raise ValueError("A imagem não pôde ser carregada. Verifique o caminho do arquivo.")
        
        # Verifique se a imagem é um array NumPy
        if not isinstance(image, np.ndarray):
            raise TypeError("O objeto carregado não é uma imagem válida.")
        
        # Converter para escala de cinza
        gray_image = convert_to_grayscale(image)
        
        # Verifique se gray_image é um array NumPy
        if not isinstance(gray_image, np.ndarray):
            raise TypeError("O objeto convertido não é uma imagem válida.")
        
        # Converta a imagem para uint8
        gray_image = (gray_image * 255).astype(np.uint8)

        # Ajustar a correção gama
        gamma_corrected_image = adjust_gamma_correction(image, gamma=1.5)
        print("Correção gama aplicada com sucesso.")
        
        # Converta para uint8 antes de salvar
        gamma_corrected_image_uint8 = img_as_ubyte(gamma_corrected_image)

        # Reescalar a intensidade da imagem
        rescaled_image = rescale_intensity(image, in_range=(50, 200), out_range=(0, 255))
        print("Intensidade da imagem reescalada com sucesso.")
        
        # Normalizar valores para garantir que estejam no intervalo [0, 1]
        rescaled_image_normalized = rescale_intensity(rescaled_image, out_range=(0, 1))

        # Converta para uint8 antes de salvar
        rescaled_image_uint8 = img_as_ubyte(rescaled_image_normalized)
        
        # Detectar bordas na imagem convertida para escala de cinza
        edges_image = detect_edges(gray_image)
        print("Bordas detectadas com sucesso.")
        
        # Converta a imagem para uint8
        edges_image = (edges_image * 255).astype(np.uint8)

        # Rotular componentes conectados na imagem de bordas
        labeled_image = label_components(edges_image)
        print("Componentes conectados rotulados com sucesso.")
        
        # Converta a imagem para uint8
        labeled_image = (labeled_image * 255).astype(np.uint8)

        # Calcular propriedades dos componentes rotulados
        properties = calculate_properties(labeled_image)
        print(f"Propriedades calculadas com sucesso.")
        
        # Salvar a imagem convertida
        if not save_image('gray_image.jpg', gray_image):
            raise ValueError("A imagem não pôde ser salva. Verifique o caminho do arquivo e o formato da imagem.")

        # Salvar a imagem corrigida com gama
        if not save_image('gamma_image.jpg', gamma_corrected_image_uint8):
            raise ValueError("A imagem corrigida com gama não pôde ser salva.")
        
        # Salvar a imagem com a intensidade reescalada
        if not save_image('rescaled_image.jpg', rescaled_image_uint8):
            raise ValueError("A imagem com intensidade reescalada não pôde ser salva.")

        # Salvar a imagem de bordas detectadas
        if not save_image('edges_image.jpg', edges_image):
            raise ValueError("A imagem de bordas não pôde ser salva.")
        
        # Salvar a imagem rotulada
        if not save_image('labeled_image.jpg', labeled_image):
            raise ValueError("A imagem rotulada não pôde ser salva.")
        
        # Salvar as propriedades
        save_properties_to_txt(properties, 'properties_image.txt')

        # Exibir as imagens geradas lado a lado
        show_images_side_by_side(
            [image, gray_image, gamma_corrected_image_uint8, rescaled_image_uint8],
            titles=["Original", "Gray Scale", "Gamma Corrected", "Rescaled Intensity"]
        )

        # Exibir individualmente outras imagens geradas
        show_image(edges_image, title="Edges Detected")
        show_image(labeled_image, title="Labeled Components")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
