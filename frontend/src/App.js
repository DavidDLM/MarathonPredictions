import React, { useState } from "react";
import axios from "axios";

function App() {
  const [category, setCategory] = useState("Male");
  const [km4week, setKm4week] = useState(100);
  const [sp4week, setSp4week] = useState(12.5);
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handlePostRequest = async () => {
    const data = [
      {
        km4week: km4week,
        sp4week: sp4week,
        Category: category,
      },
    ];

    console.log("Payload:", data);
    setLoading(true);
    setError(null);

    try {
      const result = await axios.post(
        "https://davidmlops.pythonanywhere.com/predict",
        data,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      console.log("Server Response:", result);
      setResponse(result.data); // Use the correct response structure here
    } catch (err) {
      console.error("Request Error:", err);
      setError("Error en la solicitud: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleTrainRequest = async () => {
    const data = {
      "train": true
    }

    setLoading(true);
    setError(null);

    try {
      const result = await axios.post(
        "http://127.0.0.1:5000/train",
        data,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      console.log("Server Response:", result);
      setResponse(result.data);
      if (result.status === 200) { alert("Se ha vuelto a entrenar el modelo con la información del CSV correctamente.")}
    } catch (err) {
      console.error("Request Error:", err);
      setError("Error en la solicitud: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  const formatTime = (decimalHours) => {
    const hours = Math.floor(decimalHours);
    const minutes = Math.floor((decimalHours - hours) * 60);
    const seconds = Math.round(((decimalHours - hours) * 60 - minutes) * 60);
    return `${hours} horas ${minutes} minutos ${seconds} segundos`;
  };


  return (

    <div className="area">
      <div className="min-h-screen flex items-center justify-center circles">
        <div className="bg-white shadow-lg rounded-lg p-8 max-w-md w-full">
          <h1 className="text-2xl font-bold text-center text-gray-700 mb-6">
            Predicción de Maratón
          </h1>
          <div className="mb-4">
            <label className="block text-gray-600 font-medium mb-1">
              Categoría:
            </label>
            <select
              value={category}
              onChange={(e) => setCategory(e.target.value)}
              className="w-full border rounded-lg px-3 py-2 text-gray-700 focus:outline-none focus:ring focus:ring-blue-300"
            >
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </select>
          </div>

          <div className="mb-4">
            <label className="block text-gray-600 font-medium mb-1">
              Kilómetros por semana:
            </label>
            <input
              type="number"
              value={km4week}
              onChange={(e) => setKm4week(Number(e.target.value))}
              className="w-full border rounded-lg px-3 py-2 text-gray-700 focus:outline-none focus:ring focus:ring-blue-300"
            />
          </div>

          <div className="mb-4">
            <label className="block text-gray-600 font-medium mb-1">
              Velocidad por semana (km/h):
            </label>
            <input
              type="number"
              value={sp4week}
              onChange={(e) => setSp4week(Number(e.target.value))}
              className="w-full border rounded-lg px-3 py-2 text-gray-700 focus:outline-none focus:ring focus:ring-blue-300"
            />
          </div>

          <div className="flex flex-row gap-3">
            <button
              onClick={handleTrainRequest}
              className={`p-4 rounded-xl w-fit text-white font-semibold bg-blue-500`}
            >
              Train
            </button>
            <button
              onClick={handlePostRequest}
              disabled={loading}
              className={`w-full py-2 rounded-lg text-white font-semibold ${loading
                ? "bg-gray-400 cursor-not-allowed"
                : "bg-blue-500 hover:bg-blue-600"
                }`}
            >
              {loading ? "Cargando..." : "Enviar"}
            </button>
          </div>

          {response && (
            <div className="mt-6 bg-green-100 text-green-800 p-4 rounded-lg">
              <pre className="text-sm mt-2 text-center">
                {response && formatTime(response.predictions[0])}
              </pre>
            </div>
          )}

          {error && (
            <div className="mt-6 bg-red-100 text-red-800 p-4 rounded-lg">
              <strong>{error}</strong>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
