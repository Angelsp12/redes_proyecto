# 🧠 Restauración de Imágenes con Redes Neuronales Profundas

Este repositorio contiene un proyecto de **Redes Neuronales y Aprendizaje Profundo** cuyo objetivo es la **restauración y colorización automática de imágenes antiguas o dañadas** mediante técnicas de **Deep Learning**, utilizando TensorFlow/Keras y una interfaz interactiva desarrollada con Streamlit.

El sistema permite al usuario cargar una imagen en escala de grises y obtener como resultado una versión restaurada y coloreada generada por la red neuronal.

---

## 🎯 Objetivo del proyecto

Desarrollar e implementar una red neuronal profunda capaz de aprender la relación entre imágenes degradadas (blanco y negro) y sus versiones restauradas, demostrando la aplicación práctica del aprendizaje profundo en el procesamiento digital de imágenes.

---

## 🧠 Descripción general

El proyecto está compuesto por tres elementos principales: un notebook donde se desarrolla el análisis, preprocesamiento, entrenamiento y evaluación del modelo; un modelo entrenado que encapsula el conocimiento aprendido por la red neuronal; y una aplicación interactiva que permite utilizar el modelo de forma sencilla mediante una interfaz gráfica.

---

## 🏗️ Arquitectura del sistema

- **Entrada:** Imagen en escala de grises (simulación de fotografías antiguas).
- **Preprocesamiento:** Normalización y redimensionamiento a 256×256 píxeles.
- **Modelo:** Red neuronal convolucional entrenada con TensorFlow/Keras.
- **Salida:** Imagen restaurada y coloreada generada por la IA.
- **Interfaz:** Aplicación web local desarrollada con Streamlit.

---

## 📂 Estructura del repositorio

```
PROYECTO/
├── app.py
├── proyecto_redes.ipynb
├── modelo_restauracion_final.keras
└── README.md
```

---


## 🛠️ Requisitos del sistema

### Hardware
- Computadora con CPU moderna
- GPU opcional (recomendado para entrenamiento)

### Software
- Python 3.9 o superior
- TensorFlow
- Streamlit
- NumPy
- OpenCV
- Pillow

---

## ▶️ Ejecución del proyecto

1️⃣ Clonar el repositorio
git clone https://github.com/USUARIO/NOMBRE_DEL_REPOSITORIO.git
cd NOMBRE_DEL_REPOSITORIO

2️⃣ Instalar dependencias
pip install tensorflow streamlit numpy opencv-python pillow

3️⃣ Ejecutar la aplicación
streamlit run app.py


La aplicación se abrirá automáticamente en el navegador y permitirá cargar una imagen para restaurarla con la IA.