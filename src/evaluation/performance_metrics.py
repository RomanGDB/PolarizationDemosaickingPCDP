import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

def compute_metrics(I1, I2):
    """
    Calcula tres métricas de similitud entre dos imágenes del mismo tamaño:
    el error cuadrático medio (MSE), el índice de similitud estructural (SSIM)
    y la relación señal-ruido pico (PSNR).

    Recibe:
        I1 (ndarray): Primera imagen de entrada (uint8 o float, 2D o 3D).
        I2 (ndarray): Segunda imagen de entrada, del mismo tamaño que I1.
    Devuelve:
        dict: Un diccionario con las siguientes métricas:
            - 'MSE'  : Error cuadrático medio
            - 'SSIM' : Índice de similitud estructural
            - 'PNSR' : Relación señal-ruido pico
    """
    I1_float = I1.astype(np.float64)
    I2_float = I2.astype(np.float64)
    metrics = {
        'MSE': np.mean((I1_float - I2_float) ** 2),
        'SSIM': ssim(
            I1_float, I2_float, data_range=255,
            channel_axis=-1 if I1_float.ndim == 3 else None
            ),
        'PNSR': psnr(I1_float, I2_float, data_range=255)
    }
    return metrics

def compute_error_map(I1, I2):
    """
    Calcula un mapa de error entre dos imágenes del mismo tamaño.

    Recibe:
        I1 (ndarray): Primera imagen de entrada (escala de grises o RGB).
        I2 (ndarray): Segunda imagen de entrada, del mismo tamaño que I1.
    Retorna:
        ndarray: Mapa de error de la misma forma que las imágenes de entrada.
    """
    return np.abs(I1.astype(int) - I2.astype(int))