"""
Previo a ejecutar este script se debe ejecutar el script main_pipeline.py

Este script se encarga de generar métricas y mapas de error que se utilizarán para evaluar
la precisión del algoritmo principal (PCDP). Las métricas y mapas de error son ubicadas en
el directorio /results que se encontrará en la raíz del repositorio. Este directorio
es creado por el script, no es necesario crearlo manualmente.
"""


import os
import sys
from pathlib import Path

import cv2
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from pipeline.utils import convert_to_uint8
from evaluation.performance_metrics import compute_metrics, compute_error_map


def main():
    BASE_DIR = Path(__file__).resolve().parents[2]
    dataset_path = BASE_DIR / 'dataset'
    output_path = BASE_DIR / 'output' / 'PCDP'
    results_path = BASE_DIR / 'results'

    results_all_channels = results_path / 'all_channels'
    results_green_channel = results_path / 'green_channel'
    error_maps_path = results_all_channels / 'error_maps'
    metrics_all_path = results_all_channels / 'metrics'
    metrics_green_path = results_green_channel / 'metrics'

    dirs_to_create = [
    results_all_channels,
    results_green_channel,
    error_maps_path,
    metrics_all_path,
    metrics_green_path
    ]
    
    for path in dirs_to_create:
        os.makedirs(path, exist_ok=True)

    dataset_subdirs = os.listdir(dataset_path)
    all_channels_metrics = []
    green_channel_metrics = []

    for image_name in dataset_subdirs:
        error_map_dir = error_maps_path / image_name
        os.makedirs(error_map_dir, exist_ok=True)

        for angle in [0, 45, 90, 135]:
            original_path = dataset_path / image_name / f'I{angle}.png'
            interpolated_path = output_path / image_name / f'I{angle}.png'

            I_orig = cv2.imread(str(original_path))
            I_interp = cv2.imread(str(interpolated_path))

            error_map = compute_error_map(I_orig, I_interp)
            cv2.imwrite(str(error_map_dir / f'I{angle}.png'), convert_to_uint8(error_map))

            metrics_all = compute_metrics(I_orig, I_interp)
            metrics_green = compute_metrics(I_orig[:, :, 1], I_interp[:, :, 1])

            row_info = {'Image': image_name, 'Polarization angle (°)': angle}
            all_channels_metrics.append(row_info | metrics_all)
            green_channel_metrics.append(row_info | metrics_green)

    pd.DataFrame(all_channels_metrics).to_csv(metrics_all_path / 'metrics_summary.csv', index=False)
    pd.DataFrame(green_channel_metrics).to_csv(metrics_green_path / 'metrics_summary.csv', index=False)


if __name__ == '__main__':
    main()