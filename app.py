import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
import os

# Configuración de la página
st.set_page_config(page_title="IA Restauradora", layout="wide")
st.title("Restauración de Imágenes con Deep Learning")
st.markdown("---")

# --- CONFIGURACIÓN LOCAL ---
MODEL_PATH = 'modelo_restauracion_final.keras'

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        st.error(f"Error: No encuentro el archivo '{MODEL_PATH}' en esta carpeta.")
        return None
    try:
        # Cargar modelo
        return tf.keras.models.load_model(MODEL_PATH)
    except Exception as e:
        st.error(f"Error cargando el modelo: {e}")
        return None

# Cargar el modelo
with st.spinner('Cargando modelo...'):
    model = load_model()

if model is not None:
    # Subida de archivos
    uploaded_file = st.file_uploader("Sube una foto (B/N, antigua o dañada)", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        
        # Procesar imagen
        image = Image.open(uploaded_file).convert('RGB')
        img_array = np.array(image)

        # Simular entrada B/N (lo que ve el modelo)
        img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

        with col1:
            st.subheader("Entrada (Tu foto)")
            # CORRECCIÓN AQUÍ: Usamos use_container_width=True
            st.image(img_gray, caption="Original en escala de grises", use_container_width=True)

        # Preprocesamiento para la IA
        img_resized = cv2.resize(img_gray, (256, 256))
        img_norm = img_resized.astype('float32') / 255.0
        img_input = img_norm.reshape(1, 256, 256, 1)

        # Botón para activar
        if st.button('RESTAURAR AHORA'):
            with st.spinner('La IA está trabajando...'):
                # Predicción
                prediction = model.predict(img_input)
                pred_img = prediction[0] 
            
            with col2:
                st.subheader("Resultado IA")
                # CORRECCIÓN AQUÍ TAMBIÉN
                st.image(pred_img, caption="Restaurada y Coloreada", use_container_width=True)
                st.success("¡Listo!")