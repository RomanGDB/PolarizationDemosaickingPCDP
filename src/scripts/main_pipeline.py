"""
Previo a ejecutar este script se debe ejecutar el script generate_input_images.py

Este script se encarga de aplicar el algoritmo PCDP (Polarization Channel Difference Prior)
sobre las imágenes de entrada, generadas a partir del dataset. Las imágenes de salida del algoritmo
son ubicada en el directorio output/PCDP en la raíz del repositorio. Este directorio
es creado por el script, no es necesario crearlo manualmente.
"""

import cv2
import os
import sys
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from pipeline.utils import reconstruct_polarized_images, convert_to_uint8

def main():
    BASE_DIR = Path(__file__).resolve().parents[2]
    output_path = BASE_DIR / 'output'
    input_path = BASE_DIR / 'input'
    os.makedirs(output_path, exist_ok=True)
    output_PCDP_path = output_path / 'PCDP'
    os.makedirs(output_PCDP_path, exist_ok=True)
    image_file_names = [name for name in os.listdir(input_path)]
    for img_file_name in image_file_names:
        I_PFA = cv2.imread(f'{input_path}/{img_file_name}')
        I_0, I_45, I_90, I_135 = reconstruct_polarized_images(I_PFA)
        img_folder_path = output_PCDP_path / img_file_name.replace(".png", "")
        os.makedirs(img_folder_path, exist_ok=True)
        cv2.imwrite(img_folder_path / 'I0.png', convert_to_uint8(I_0))
        cv2.imwrite(img_folder_path / 'I45.png', convert_to_uint8(I_45))
        cv2.imwrite(img_folder_path / 'I90.png', convert_to_uint8(I_90))
        cv2.imwrite(img_folder_path / 'I135.png', convert_to_uint8(I_135))       
        
if __name__ == '__main__':
    main()