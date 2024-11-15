import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Leer variables del entorno
host = os.getenv('FLASK_HOST', '127.0.0.1')
port = int(os.getenv('FLASK_PORT', 5000))

athlete_data = []

# Endpoint para actualizar datos
@app.route('/update-data', methods=['POST'])
def update_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    athlete_data.append(data)
    return jsonify({"message": "Data updated successfully", "data": data}), 200

# Endpoint para predecir
@app.route('/predict', methods=['GET'])
def predict():
    return jsonify({
        "prediction": "2:45:30",
        "message": "Prediction successful"
    }), 200

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
