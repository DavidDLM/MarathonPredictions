import os
import pickle
import pandas as pd
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from src.train import MarathonModel
import joblib

# Cargar variables del entorno
load_dotenv()

# Configurar Flask
app = Flask(__name__)

# Rutas del modelo y los datos
model = joblib.load('./models/marathon_model.pkl')
print(type(model))

# Instancia de la clase para entrenar y predecir
marathon_model = MarathonModel()

# Endpoint para predecir
@app.route('/predict', methods=['POST'])
def predictEndpoint():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        df = pd.DataFrame(data)
        category_map = {"Male": "MAM", "Female": "WAM"}
        df['Category'] = df['Category'].map(category_map)
        if df['Category'].isnull().any():
            return jsonify({"error": "Invalid category. Use 'Male' or 'Female'."}), 400
        # Cargar el modelo
        model = joblib.load('./models/marathon_model.pkl')
        # Realizar predicción
        predictions = model.predict(df)
        return jsonify({"predictions": predictions.tolist(), "message": "Prediction successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

'''
# Endpoint para entrenar el modelo 
@app.route('/train', methods=['POST'])
def train_endpoint():
    try:
        train_flag = request.json.get('train', False)
        if train_flag:
            marathon_model.trainModel(DATA_PATH, MODEL_PATH)
            return jsonify({"message": "Model trained successfully"}), 200
        else:
            return jsonify({"message": "Training not activated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
'''
# Endpoint para actualizar datos (placeholder)
@app.route('/update-data', methods=['POST'])
def updateData():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    return jsonify({"message": "Data received successfully", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
