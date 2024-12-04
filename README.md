# Proyecto de Clasificación de Clientes
Este proyecto implementa un modelo de Machine Learning para clasificar clientes en tres categorías: `low_value`, `medium_value`, y `high_value`.

## Estructura del Repositorio
- `notebook.ipynb`: Notebook con exploración, preprocesamiento y entrenamiento.
- `fastapi.py`: Código de la API desarrollada con FastAPI.
- `lambda_function.py`: Código para la función Lambda en AWS.
- `info.txt`: Documentación del proyecto, URL de la API y ejemplo del POST.

## Cómo Probar la API
1. Enviar un POST al endpoint especificado en `info.txt` con el cuerpo JSON.
2. Validar la respuesta según el ejemplo.

## Despliegue
- SageMaker para el modelo.
- AWS Lambda para las solicitudes.
- FastAPI para la comunicación.