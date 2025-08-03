import numpy as np

def subsampling(I):
    """
    Devuelve una versión submuestreada de la imagen de entrada, conservando únicamente
    los píxeles ubicados en filas y columnas de índice impar (es decir, descarta las filas y
    columnas de índice par).

    Recibe:
        I (ndarray): Imagen de entrada (2D o 3D, por ejemplo, en escala de grises o RGB).

    Devuelve:
        ndarray: Imagen submuestreada con forma reducida a la mitad
                 en ambas dimensiones espaciales.
    """
    return I[1::2, 1::2]


def generate_input_image(I_0, I_45, I_90, I_135):
    """
    Genera una imagen polarizada simulada con muestreo tipo DoFP (Division of Focal Plane)
    a partir de las cuatro imágenes RGB correspondientes a los ángulos de polarización
    0°, 45°, 90° y 135°.

    Recibe:
        I_0 (ndarray): Imagen RGB correspondiente a polarización 0° (shape: H x W x 3)
        I_45 (ndarray): Imagen RGB correspondiente a polarización 45° (shape: H x W x 3)
        I_90 (ndarray): Imagen RGB correspondiente a polarización 90° (shape: H x W x 3)
        I_135 (ndarray): Imagen RGB correspondiente a polarización 135° (shape: H x W x 3)

    Devuelve:
        ndarray: Imagen RGB de tamaño (2H x 2W x 3) que representa el muestreo polarimétrico tipo DoFP.
    """
    height, width, channels = I_0.shape
    I_PFA = np.zeros((2 * height, 2 * width, channels), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            I_PFA[2*i    , 2*j    ] =   I_0[i, j]
            I_PFA[2*i    , 2*j + 1] =  I_45[i, j]
            I_PFA[2*i + 1, 2*j    ] = I_135[i, j]
            I_PFA[2*i + 1, 2*j + 1] =  I_90[i, j]
    return I_PFA