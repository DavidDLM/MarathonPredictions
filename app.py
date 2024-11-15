import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

# Configurar Flask
app = Flask(__name__)

# Recibir y actualizar datos
@app.route('/update-data', methods=['POST'])
def update_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    return jsonify({"message": "Data received successfully", "data": data}), 200

# Predecir
@app.route('/predict', methods=['GET'])
def predict():
    return jsonify({
        "prediction": "2:45:30",
        "message": "Prediction successful"
    }), 200

if __name__ == '__main__':
    app.run(
        host=os.getenv('FLASK_HOST'),
        port=int(os.getenv('FLASK_PORT')),
        debug=os.getenv('FLASK_DEBUG') == 'True'
    )
