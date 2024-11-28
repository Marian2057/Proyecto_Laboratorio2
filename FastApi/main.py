from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import xgboost as xgb
import numpy as np
from starlette.requests import Request
import os
import pickle

# Crear la aplicación FastAPI
app = FastAPI()

# Configurar las plantillas y archivos estáticos
templates = Jinja2Templates(directory="templates")

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Variable global para almacenar el modelo cargado
model = None

# Endpoint para cargar el modelo
@app.post("/upload_model/")
async def upload_model(model_file: UploadFile = File(...)):
    global model
    try:
        # Validar si el archivo cargado es un modelo de XGBoost
        if not model_file.filename.endswith(".model"):
            raise HTTPException(status_code=400, detail="El archivo debe ser un modelo XGBoost (.model)")

        # Guardar el archivo del modelo
        model_path = "uploaded_model.model"
        with open(model_path, "wb") as f:
            f.write(await model_file.read())

        # Cargar el modelo con XGBoost
        model = xgb.Booster()
        model.load_model(model_path)
        
        return {"message": "Modelo cargado correctamente."}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el modelo: {str(e)}")

# Modelo de entrada para los datos de la predicción
class InputData(BaseModel):
    data: List[float]

# Endpoint para mostrar el formulario principal
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# Endpoint para hacer la predicción
@app.post("/predict/")
async def predict(input_data: InputData, request: Request):
    try:
        # Asegúrate de que el modelo esté cargado
        if model is None:
            raise HTTPException(status_code=400, detail="Modelo no cargado.")
        
        # Convertir la entrada de datos a formato correcto
        data = np.array(input_data.data).reshape(1, -1)

        # Realizar la predicción
        dmatrix_data = xgb.DMatrix(data)
        prediction = model.predict(dmatrix_data)

        # Mapear la predicción
        label_map = {0: "low_value", 1: "medium_value", 2: "high_value"}
        predicted_label = label_map.get(int(prediction[0]), "unknown")

        return templates.TemplateResponse("form.html", {"request": request, "predicted_label": predicted_label})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {str(e)}")