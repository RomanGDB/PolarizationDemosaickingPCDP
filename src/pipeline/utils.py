import numpy as np
import cv2

valid_angles = [0, 45, 90, 135]

def convert_to_uint8(I):
    """
    Convierte una imagen a formato uint8, evitando aplicar aritmética modular.

    Recibe:
        I (np.ndarray): Imagen de entrada
    Devuelve:
        np.ndarray: Imagen en uint8
    """
    return np.clip(np.round(I), 0, 255).astype(np.uint8)

def get_polarization_mask(img_shape ,angle):
  '''
  Devuelve una imagen tal que vale 1 si el pixel corresponde al angulo de polarización y 0 en otro caso.

  Recibe:
    img_shape - Tupla que contiene el tamaño de la imagen.
    angle - Angulo de polarizacion. Debe ser 0, 45, 90 o 135.
  Devuelve:
    img_sparse - Imagen con un solo angulo de polarizacion.
    mask - Mascara utilizada para obtener el resultado
  '''
  if angle not in valid_angles:
    raise ValueError(
      f'El ángulo de polarizacion debe ser 0°, 45°, 90° o 135°. El valor recibido es {angle=}')
  mask = np.zeros(img_shape)
  if angle == 0:
    mask[::2, ::2] = 1
  elif angle == 45:
    mask[::2, 1::2] = 1 
  elif angle == 90:
    mask[1::2, 1::2] = 1 
  elif angle == 135:
    mask[1::2, ::2] = 1 
  return mask
  
def quick_bilinear_interpolation(I):
  '''
  Recibe:
    I - Imagen de entrada
  Devuelve:
    I_out: Convolución entre img y kernel F
  '''
  F = (1/4)*np.array([[1,2,1],[2,4,2],[1,2,1]])
  I_out = cv2.filter2D(I, ddepth=-1, kernel=F, borderType=cv2.BORDER_REPLICATE)
  return I_out

def get_fusion_weight(angle_i, angle_j):
  """
  Calcula un peso basado en la diferencia entre dos ángulos de polarización.

  Recibe:
        angle_i (int): Primer ángulo de polarización (debe ser 0, 45, 90 o 135).
        angle_j (int): Segundo ángulo de polarización (debe ser 0, 45, 90 o 135).

  Devuelve:
        float: Un peso entre 0 y 1 según la relación angular.
  """
  if angle_i not in valid_angles or angle_j not in valid_angles:
        raise ValueError(
            "Los ángulos de polarizacion debe ser 0°, 45°, 90°, o 135°.\n"
            f"Los valores recibidos son {angle_i=}, {angle_j=}."
        )
  if np.abs(angle_i - angle_j) == 90:
    weight = np.sqrt(2) / (2 + np.sqrt(2))
  else:
    weight = 1 / (2 + np.sqrt(2))
  return weight


def reconstruct_polarized_images(I_PFA):
  """
    Reconstruye las imágenes polarizadas RGB correspondientes a los ángulos 0°, 45°, 90° y 135°,
    a partir de una imagen en escala de grises obtenida por una cámara DoFP.
    Recibe:
        I_PFA (ndarray): Imagen de entrada en escala de grises (DoFP - Division of Focal Plane).

    Devuelve:
        tuple of ndarray: Una tupla con cuatro imágenes RGB reconstruidas:
                          (I_0, I_45, I_90, I_135), correspondientes a cada ángulo de polarización.
  """
  M = {
    0: get_polarization_mask(I_PFA.shape, 0),
    45: get_polarization_mask(I_PFA.shape, 45),
    90: get_polarization_mask(I_PFA.shape, 90),
    135: get_polarization_mask(I_PFA.shape, 135)
  }
  I_hat = {
    0: I_PFA *  M[0],
    45: I_PFA *  M[45],
    90: I_PFA *  M[90],
    135: I_PFA *  M[135]
  }
  I_tilde = {
    0: quick_bilinear_interpolation(I_hat[0]),
    45: quick_bilinear_interpolation(I_hat[45]),
    90: quick_bilinear_interpolation(I_hat[90]),
    135: quick_bilinear_interpolation(I_hat[135])
  }
  polarized_images = []
  for i in valid_angles:
    complementary_angles = valid_angles.copy()
    complementary_angles.remove(i)
    I_i = np.zeros(I_PFA.shape)
    for j in complementary_angles:
      delta_hat = quick_bilinear_interpolation(I_hat[i] - (I_tilde[j] * M[i]))
      I_i += get_fusion_weight(i, j) * (I_tilde[j] + delta_hat)
    polarized_images.append(I_i)
  return tuple(polarized_images)
  