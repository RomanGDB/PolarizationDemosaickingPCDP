Title: Introducción
Date: 2025-05-28
Category: Page
Ordinal: 001

# PROYECTO: Demosaicking de imágenes polarizadas a color utilizando PCDP

## Presentación del problema
La imaginería polarimetría es una técnica que permite obtener una mayor cantidad de información a partir de la interacción con la luz que tiene un objeto captado en cámara, separando la luz según su polarización. Esta técnica ha tenido aportes valiosos en campos como la biología, donde se destacan sus aplicaciones en problemáticas como la detección del cáncer [@tuchin2016]

La técnica de polarimetría con la que se trabajará en el presente trabajo se denomina *Division of Focal Plane (DoFP)*, que consiste en superponer una rejilla, de habitualmente uno de cuatro ángulos (0°,45°,90°,135°) sobre cada píxel. De esta manera, se logra obtener la información polarimétrica de luz difractada por un objeto.

Como se puede apreciar en la [](#fig_filtro_bayer), con el Filtro de Bayer tradicional, no se capturan todos los valores de RGB para cada pixel, sino que cada uno captura un único valor de RGB. Para solucionar este problema, se suelen aplicar distintas técnicas de interpolación, como la del vecino más cercano o bilineal, entre los pixeles de un mismo color. Así se obtienen todos los valores de RGB, para todos los pixeles de la imagen capturada. Este proceso lleva el nombre de Demosaicking.
La [](#fig_filtro_de_bayer_polarizado) muestra la máscara DoFP, donde cada píxel tiene superpuesto una micro grilla de polarizadores lineales.



Figura: Filtro de Bayer tradicional {#fig_filtro_bayer}

![](images/filtro_bayer.png ){#fig_filtro_bayer width=200}

Figura: Filtro de Bayer usado en DoFP {#fig_filtro_de_bayer_polarizado}

![](images/filtro_de_bayer_polarizado.png){#fig_filtro_de_bayer_polarizado width=200}

La técnica de *DoFP* divide al sensor en cuatro, según el ángulo correspondiente al polarizador que está encima del píxel correspondiente. Es decir que, para cada uno de los cuatro ángulos, se tiene solamente la cuarta parte de la información. Un enfoque tradicional para resolver este problema consiste en agrupar los pixeles según su angulo de polarización para luego aplicar procesos de Demosaicking como en los Filtros de Bayer tradicionales. En la [](#fig_demosaicking_clasico) se ilustra el enfoque clásico de Demosaicking de imágenes polarizadas a color.

Figura: Enfoque clásico de demosaicking. {#fig_demosaicking_clasico}

![](images/demosaicking_img_polarizada.png ){#fig_demosaicking_clasico width=500}


## Aproximación
En este proyecto se implementó el algoritmo de interpolación PCDP (Polarization Channel Difference Prior) propuesto por Rongyan Wu et al. en su artículo “Fast and accurate polarization demosaicking based on polarization channel difference prior” [@liu2021]. Este algoritmo aprovecha que la diferencia entre canales correspondientes a angulos ortogonales entre sí presenta una mayor energía en las frecuencias altas. Además, se compara la precisión del algoritmo PCDP en la recuperación de los cuatro canales de luz polarizada con algunos métodos de interpolación clásicos.

La sección de [Métodos](methods.md) contiene una descripción del algoritmo implementado, así como una demostración matemática del principio de funcionamiento del mismo.

