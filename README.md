# 🚀 Proyecto de Clasificación de Clientes  

Este proyecto implementa un modelo de **Machine Learning** para clasificar clientes en tres categorías:  
- 🟢 `low_value`  
- 🟡 `medium_value`  
- 🔴 `high_value`  

El objetivo es ayudar a identificar clientes según su valor potencial y mejorar la toma de decisiones de negocio.  

---

## 📂 Estructura del Repositorio  

- 📒 **Notebook-Final-Lab.ipynb** → Exploración, preprocesamiento y entrenamiento del modelo.  
- 🤖 **xgboost-model** → Archivo del modelo entrenado con **XGBoost**.  
- ⚡ **fastapi.py** → Código de la **API** desarrollada con **FastAPI**.  
- ☁️ **lambda_function.txt** → Código para la función **AWS Lambda**.  
- 📑 **DOCUMENTACION PROYECTO MINERIA_VERSION I.docx** → Documentación completa:  
  - URL del endpoint de la API  
  - Ejemplo de request **POST**  
  - Capturas del dashboard de monitoreo  

---

## ⚙️ Tecnologías utilizadas  

- **Python 3.9+**  
- **XGBoost** (modelo de ML)  
- **FastAPI** (exposición de la API REST)  
- **AWS SageMaker** (entrenamiento y despliegue del modelo)  
- **AWS Lambda** (ejecución sin servidor para solicitudes)  

---

## ▶️ Cómo Probar la API  

1. Enviar un **POST** al endpoint especificado en la documentación:  
   ```json
   {"data": [0.812959, 0, -0.560700, 1.701895, -1.478080, -0.121517, 0.125643, 0, 0.489832, 0.340994]}
Validar la respuesta según el ejemplo:

json
Copy
Edit
{
  "prediction": "medium_value",
  "confidence": 0.82
}
🛠️ Despliegue
📦 Modelo → Entrenado y almacenado en AWS SageMaker.

⚡ API REST → Desarrollada con FastAPI.

☁️ Función Lambda → Maneja solicitudes entrantes y conecta con el modelo.

📊 Monitoreo → Dashboard para métricas en tiempo real.

📊 Resultados esperados
Clasificación automática de clientes en tres categorías.

Mejora en la segmentación y toma de decisiones de negocio.

Infraestructura escalable y serverless en AWS.

Ciencia de Datos, Machine Learning & APIs
