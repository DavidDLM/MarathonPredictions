from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulación de almacenamiento de datos
athlete_data = []

# Endpoint para actualizar datos del atleta
@app.route('/update-data', methods=['POST'])
def update_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    athlete_data.append(data)
    print(f"Data received: {data}")
    return jsonify({"message": "Data updated successfully", "data": data}), 200

# Endpoint para predecir el tiempo de maratón
@app.route('/predict', methods=['GET'])
def predict():
    return jsonify({
        "prediction": "2:45:30",  # Placeholder, cambiar por predicción real
        "message": "Prediction successful"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
