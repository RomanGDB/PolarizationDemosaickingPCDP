# TIMAG 2025 - PROYECTO FINAL - DEMOSAICKING DE IMÁGENES POLARIZADAS A COLOR UTILIZANDO PCDP

Este repositorio contiene el proyecto final del grupo 07 del curso de Tratamiento de Imágenes por Computadora de la Facultad de Ingeniería de la Udelar, edición 2025.

Este repositorio tiene como objetivo principal aplicar el algoritmo PCDP (Polarization Channel Difference Prior) para solucionar el problema de Demosaicking de Imágenes polarizadas a color [1]. La documentación y el código fuente del proyecto, pueden encontrarse accediendo a los siguientes links:

[Página web del proyecto](https://2025-proyecto-grupo-07-639332.pages.fing.edu.uy/)

## Documentación del Proyecto

La documentación completa del proyecto se encuentra organizada en la carpeta [`docs/`](docs/). A continuación, se presentan los enlaces directos a cada sección:

- [Acerca del proyecto (`about.md`)]: Introducción general y objetivos del trabajo.
- [Experimentos (`experiments.md`)]: Descripción de los experimentos realizados.
- [Conjunto de datos (`datasets.md`)]: Detalles sobre los datasets utilizados.
- [Metodología (`methods.md`)]: Métodos aplicados y justificación técnica.
- [Índice general (`index.md`)]: Estructura general de la documentación.
- [Conclusiones (`conclusions.md`)]: Análisis final y observaciones del proyecto.

[Repositorio del proyecto](https://gitlab.fing.edu.uy/timag/2025/proyectos/2025-proyecto-grupo-07)

El dataset utilizado en el proyecto, puede encontrarse accediendo al siguiente link:

[Dataset del proyecto](https://drive.google.com/drive/folders/1gZFhTpv1Ul_UGjjxA0PSv7flf2AZOQmA?usp=sharing)

En la página **Dataset** de la documentación pueden verse ejemplos de las imágenes de este dataset.

En la carpeta **src** se encuentra el código desarrollado en el proyecto. A continuación se resumen los archivos principales que se encuentran dentro de este directorio.  

En la carpeta **src/notebooks** se encuentran los siguientes python notebooks:

* *data_exploration*: su función es explorar las imágenes contenidas en el dataset.
* *pipeline_inspection*: su función es inspeccionar el flujo de procesamiento principal de las imágenes.
* *analyze_results*: su función es evaluar los resultados del algoritmo implementado, según distintas métricas (MSE, SSIM, PSNR, mapas de error).

En la carpeta **src/scripts** se encuentran los siguientes python scripts encargados de las distintas etapas del procesamiento:

* *generate_input_images*: Se encarga de generar las imágenes de entrada del algortimo a partir de las imágenes del dataset.
* *main_pipeline*: Se encarga de ejecutar el algoritmo principal (PCDP) en todas las imágenes del dataset.
* *evaluate_PCDP_results*: Se encarga de generar las métricas y los mapas de error correspondientes a los resultados generados por el algortimo principal (PCDP).

## Estructura de directorios

```plaintext
/
├── docs/               # Archivos de la página web de documentación.
├── src/                    
│   ├── scripts/        # Scripts encargados de procesar imágenes.
│   ├── notebooks/      # Notebooks utilizadas para visaulizar y analizar resultados.
│   ├── pipeline/       # Funciones del algortimo principal (PCDP).
│   ├── preprocessing/  # Funciones auxiliares utiliadas en la etapa de procesamiento.
│   └── evaluation/     # Funciones auxiliar utilzadas para evaluar los resultados más importantes.
│   
├── requirements.txt    # Dependencias del proyecto
├── .gitlab-ci.yml      # Environment variables
├── README.md           # Archivo de despliegue de la página web de documentación.
└── .gitignore          # Archivos ignorados por git.
```

## Prerequisitos

* Sistema operativo: **Windows 10 o superior**
* Python 3.10+
* Pip (Python package manager)

## Instalar dependencias
Ejecutar el siguiente comando desde la raíz del proyecto:

```bash
pip install -r requirements.txt
```

## Ejecutar scripts
Ejecutar el siguiente comando desde el directorio **src/scripts**:

```bash
python ejemplo_script.py
```

Se recomienda fuertemente leer el encabezado que se encuentra dentro de cada archivo script previo a su ejecución.

## Generar documentación local
Ejecutar el siguiente comando desde la raíz del proyecto:

```bash
mkdocs serve
```

## Referencias

[1] Wu, R., Zhao, Y., Li, N., Seong, G., & Kong, S. (2021). Fast and accurate polarization demosaicking based on polarization channel difference prior. Optics Express, 29(14), 22066–22081. Optica Publishing Group. 
