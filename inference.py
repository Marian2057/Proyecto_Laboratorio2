import os
import joblib
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Función de entrada para el modelo
def model_fn(model_dir):
    """Carga el modelo entrenado desde el directorio"""
    model_path = os.path.join(model_dir, 'model.joblib')
    model = joblib.load(model_path)  # Cargar el modelo guardado
    return model

# Función para realizar la predicción
def predict_fn(input_data, model):
    """Realiza la predicción usando el modelo cargado"""
    # Convertir la entrada a formato adecuado (asegúrate de que el modelo espera datos tipo float32)
    input_data = np.array(input_data).astype('float32')
    prediction = model.predict(input_data)  # Realizar la predicción
    return prediction

# Función de post-procesamiento (si es necesario, puedes transformar los resultados aquí)
def output_fn(prediction, content_type):
    """Convierte la predicción en formato de salida"""
    # Si necesitas una respuesta JSON, puedes convertirla a JSON
    return str(prediction)