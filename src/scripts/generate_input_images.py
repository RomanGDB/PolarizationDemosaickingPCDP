"""
Previo a ejecutar este script se debe tener la carpeta dataset, que se puede descargar de
https://drive.google.com/drive/folders/1gZFhTpv1Ul_UGjjxA0PSv7flf2AZOQmA, en la raíz del proyecto.

Este script genera las imágenes de entrada del algoritmo principal (PCDP), estas imágenes son ubicadas
en el directorio /input en la raíz del proyecto. Este directorio es creado por el script, no es necesario
crearlo manualmente.
"""

import cv2
import os
import sys
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from preprocessing.subsample_polarized_images import generate_input_image, subsampling

def main():
    BASE_DIR = Path(__file__).resolve().parents[2]
    dataset_path = BASE_DIR / 'dataset'
    input_path = BASE_DIR / 'input'
    os.makedirs(input_path, exist_ok=True)
    dataset_subdirs = [name for name in os.listdir(dataset_path)]
    for img_folder in dataset_subdirs:
        I_0 = subsampling(cv2.imread(f'{dataset_path}/{img_folder}/I0.png'))
        I_45 = subsampling(cv2.imread(f'{dataset_path}/{img_folder}/I45.png'))
        I_90 = subsampling(cv2.imread(f'{dataset_path}/{img_folder}/I90.png'))
        I_135 = subsampling(cv2.imread(f'{dataset_path}/{img_folder}/I135.png'))
        I_PFA = generate_input_image(I_0, I_45, I_90, I_135)
        cv2.imwrite(input_path / f'{img_folder}.png', I_PFA)
        
if __name__ == '__main__':
    main()