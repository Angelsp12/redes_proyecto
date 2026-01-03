 Restauración de Imágenes con Redes Neuronales Profundas

Este repositorio contiene un proyecto de Redes Neuronales y Aprendizaje Profundo cuyo objetivo es la restauración y colorización automática de imágenes antiguas o dañadas mediante Deep Learning, integrando un modelo entrenado en TensorFlow/Keras y una interfaz interactiva desarrollada con Streamlit.

El sistema permite al usuario cargar una imagen en escala de grises y obtener como resultado una versión restaurada y coloreada generada por la red neuronal.

 Objetivo del proyecto

Desarrollar e implementar una red neuronal profunda capaz de aprender la relación entre imágenes degradadas (blanco y negro) y sus versiones restauradas, demostrando la aplicación práctica del aprendizaje profundo en el procesamiento digital de imágenes.

 Descripción general

El proyecto consta de tres componentes principales:

Un notebook (proyecto_redes.ipynb) donde se realiza el análisis, preprocesamiento, diseño, entrenamiento y evaluación del modelo de red neuronal.

Un modelo entrenado (modelo_restauracion_final.keras) que encapsula el conocimiento aprendido por la red.

Una aplicación interactiva (app.py) que permite usar el modelo de forma sencilla a través de una interfaz gráfica.

 Arquitectura del sistema

Entrada: Imagen en escala de grises (simulando fotografías antiguas).

Preprocesamiento: Normalización y redimensionamiento a 256×256 píxeles.

Modelo: Red neuronal convolucional entrenada con TensorFlow/Keras.

Salida: Imagen restaurada y coloreada generada por la IA.

Interfaz: Aplicación web local desarrollada con Streamlit.

 Estructura del repositorio
PROYECTO/
│
├── app.py                         # Aplicación Streamlit para usar el modelo
├── proyecto_redes.ipynb           # Notebook de desarrollo y entrenamiento
├── modelo_restauracion_final.keras# Modelo entrenado
└── README.md                      # Documentación del proyecto

 Requisitos del sistema
Hardware

Computadora con CPU moderna

GPU opcional (recomendado para entrenamiento)

Software

Python 3.9 o superior

TensorFlow

Streamlit

NumPy

OpenCV

Pillow

▶ Ejecución del proyecto
1️⃣ Clonar el repositorio
git clone https://github.com/USUARIO/NOMBRE_DEL_REPOSITORIO.git
cd NOMBRE_DEL_REPOSITORIO

2️⃣ Instalar dependencias
pip install tensorflow streamlit numpy opencv-python pillow

3️⃣ Ejecutar la aplicación
streamlit run app.py


La aplicación se abrirá automáticamente en el navegador y permitirá subir una imagen para restaurarla con la IA.

 Funcionamiento de la aplicación

El usuario carga una imagen (jpg, png o jpeg).

La imagen se convierte internamente a escala de grises.

El modelo procesa la imagen.

Se muestra el resultado restaurado y coloreado.

 Resultados

El modelo logra reconstruir información visual perdida y añadir color de forma automática, demostrando la capacidad de las redes neuronales convolucionales para resolver problemas complejos de restauración de imágenes.