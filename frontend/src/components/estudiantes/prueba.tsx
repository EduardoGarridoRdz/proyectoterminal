import React, { useState } from "react";
import { postData } from "../../API/api"; // Asegúrate de que la ruta sea correcta

const PostDataComponent: React.FC = () => {
  // Estado para manejar los datos del formulario
  const [formData, setFormData] = useState({
    nombre: "",
  });

  // Estado para manejar la respuesta de la API
  const [responseData, setResponseData] = useState<any>(null);

  // Estado para manejar errores
  const [error, setError] = useState<string | null>(null);

  // Estado para manejar el estado de carga
  const [loading, setLoading] = useState<boolean>(false);

  // Función para manejar cambios en los campos del formulario
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // Función para manejar el envío del formulario
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault(); // Evita que el formulario se envíe de forma predeterminada
    setLoading(true); // Indica que la carga ha comenzado
    setError(null); // Limpia cualquier error previo

    try {
      // Llama a la función postData para enviar los datos al servidor
      const result = await postData("nombreTaller/", formData); // Cambia "mi-endpoint" por tu endpoint real
      setResponseData(result); // Guarda la respuesta de la API en el estado
    } catch (err) {
      console.error("Error:", err);
      setError("Error al enviar los datos"); // Guarda el error en el estado
    } finally {
      setLoading(false); // Indica que la carga ha terminado
    }
  };

  return (
    <div>
      <h1>Enviar datos a la API</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Nombre:</label>
          <input
            type="text"
            id="nombre"
            name="nombre"
            value={formData.nombre}
            onChange={handleInputChange}
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? "Enviando..." : "Enviar datos"}
        </button>
      </form>
      {error && <div style={{ color: "red" }}>Error: {error}</div>}{" "}
      {/* Muestra un mensaje de error si existe */}
      {responseData && (
        <div>
          <h2>Respuesta de la API:</h2>
          <pre>{JSON.stringify(responseData, null, 2)}</pre>{" "}
          {/* Muestra la respuesta de la API en formato JSON */}
        </div>
      )}
    </div>
  );
};

export default PostDataComponent;
