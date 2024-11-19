from flask import Flask, request, jsonify
import pandas as pd
import joblib
from src.train import MarathonModel
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

# Cargar el modelo
model = joblib.load('./models/marathon_model.pkl')
print(type(model))

# Instancia de la clase para entrenar y predecir
marathon_model = MarathonModel()

# Endpoint para predecir
@application.route('/predict', methods=['POST'])
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
        predictions = model.predict(df)
        return jsonify({"predictions": predictions.tolist(), "message": "Prediction successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Placeholder para futuros endpoints
@application.route('/update-data', methods=['POST'])
def updateData():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    return jsonify({"message": "Data received successfully", "data": data}), 200

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
