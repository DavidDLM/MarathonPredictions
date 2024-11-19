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
    const data = [{
      km4week: km4week,
      sp4week: sp4week,
      Category: category
    }]
  
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
  
  
  
  return (
    <div className="bg-red-500">
      <h1>Predicción de Maratón</h1>
      <div style={{ marginBottom: "20px" }}>
        <label>
          <strong>Categoría: </strong>
        </label>
        <select
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          style={{ marginLeft: "10px", padding: "5px" }}
        >
          <option value="Male">Male</option>
          <option value="Female">Female</option>
        </select>
      </div>

      <div style={{ marginBottom: "20px" }}>
        <label>
          <strong>Kilómetros por semana: </strong>
        </label>
        <input
          type="number"
          value={km4week}
          onChange={(e) => setKm4week(Number(e.target.value))}
          style={{ marginLeft: "10px", padding: "5px", width: "100px" }}
        />
      </div>

      <div style={{ marginBottom: "20px" }}>
        <label>
          <strong>Velocidad por semana (km/h): </strong>
        </label>
        <input
          type="number"
          value={sp4week}
          onChange={(e) => setSp4week(Number(e.target.value))}
          style={{ marginLeft: "10px", padding: "5px", width: "100px" }}
        />
      </div>

      <button onClick={handlePostRequest} disabled={loading}>
        {loading ? "Cargando..." : "Enviar Datos"}
      </button>

      {response && (
        <div style={{ marginTop: "20px" }}>
          <h2>Respuesta del Servidor:</h2>
          <pre>{JSON.stringify(response.predictions[0], null, 2)}</pre>
        </div>
      )}

      {error && (
        <div style={{ marginTop: "20px", color: "red" }}>
          <strong>{error}</strong>
        </div>
      )}
    </div>
  );
}

export default App;
