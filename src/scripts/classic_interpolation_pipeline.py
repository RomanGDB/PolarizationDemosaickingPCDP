"""
Previo a ejecutar este script se debe tener la carpeta dataset, que se puede descargar de
https://drive.google.com/drive/folders/1gZFhTpv1Ul_UGjjxA0PSv7flf2AZOQmA, en la raíz del proyecto.

Este script se encarga de generar los resultados correspondientes a aplicar el interpolación bilineal
sobre las imágenes de entrada del algortimo PCDP. Las imágenes de salida de este script son ubicadas
en el directorio output/bilinear en la raíz del repositorio. Este directorio es creado por el script,
no es necesario crearlo manualmente.
"""


import cv2
import os
import sys
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from pipeline.utils import quick_bilinear_interpolation, get_polarization_mask, convert_to_uint8

def main():
    BASE_DIR = Path(__file__).resolve().parents[2]
    dataset_path = BASE_DIR / 'dataset'
    output_path = BASE_DIR / 'output'
    os.makedirs(output_path, exist_ok=True)
    output_biliear_path = output_path / 'bilinear'
    os.makedirs(output_biliear_path, exist_ok=True)
    dataset_subdirs = [name for name in os.listdir(dataset_path)]
    for img_name in dataset_subdirs:
        for angle in [0, 45, 90, 135]:
            img_folder_path = output_biliear_path / img_name
            os.makedirs(img_folder_path, exist_ok=True)
            I_i = cv2.imread(f'{dataset_path}/{img_name}/I{angle}.png')
            M_i = get_polarization_mask(I_i.shape, angle)
            I_bilineal_reconstr = quick_bilinear_interpolation(I_i * M_i)
            cv2.imwrite(img_folder_path / f'I{angle}.png', convert_to_uint8(I_bilineal_reconstr))
        
if __name__ == '__main__':
    main()