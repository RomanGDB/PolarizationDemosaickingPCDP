"""
Previo a ejecutar este script se debe ejecutar el classic_interpolation_pipeline.py

Este script se encarga de generar métricas de referencia que se utilizarán para evaluar
la precisión del algoritmo principal (PCDP). Estas métricas corresponden a aplicar interpolación
bilineal sobre el dataset, y así poder comparar su presición con el algorimo PCDP. Las métricas
son ubicadas en el directorio /reference_results/bilinear que se encontrará en la raíz del repositorio.
Este directorio es creado por el script, no es necesario crearlo manualmente.
"""


import os
import sys
from pathlib import Path
import cv2
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from evaluation.performance_metrics import compute_metrics

def main():
    BASE_DIR = Path(__file__).resolve().parents[2]
    dataset_path = BASE_DIR / 'dataset'
    output_path = BASE_DIR / 'output' / 'bilinear'
    reference_results_path = BASE_DIR / 'reference_results' / 'bilinear'
    os.makedirs(reference_results_path, exist_ok=True)
    dataset_subdirs = [name for name in os.listdir(dataset_path)]
    metrics_summary_rows = []
    for image_dir in dataset_subdirs:
        for angle in [0, 45, 90, 135]:
            I_angle_original = cv2.imread(f'{dataset_path}/{image_dir}/I{angle}.png')
            I_angle_interpolated = cv2.imread(f'{output_path}/{image_dir}/I{angle}.png')
            metrics = compute_metrics(I_angle_original, I_angle_interpolated)
            img_data = {'Image': image_dir, 'Polarization angle (°)': angle}
            metrics_summary_rows.append(img_data | metrics)
    os.makedirs(reference_results_path, exist_ok=True)
    pd.DataFrame(metrics_summary_rows).to_csv(reference_results_path / 'metrics_summary.csv', index=False)
         
if __name__ == '__main__':
    main()