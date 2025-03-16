import React, { useState, ChangeEvent, FormEvent } from "react";
import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api"; // Cambia esto por la URL de tu API de Django

// Definimos la interfaz para la respuesta del backend
interface ApiResponse {
  status: string;
  message: string;
  data: Record<string, any>[]; // Los datos del Excel en formato de lista de diccionarios
}

// Función para subir un archivo Excel
const uploadExcelFile = async (file: File): Promise<ApiResponse> => {
  const formData = new FormData();
  formData.append("file", file); // 'file' debe coincidir con el nombre esperado en el backend

  try {
    const response = await axios.post<ApiResponse>(
      `${API_BASE_URL}/subir_excel/upload_excel/`,
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );
    return response.data;
  } catch (error) {
    console.error("Error uploading file:", error);
    throw error;
  }
};

const ExcelUploader: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [response, setResponse] = useState<ApiResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  // Maneja el cambio de archivo seleccionado
  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  // Maneja el envío del formulario
  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!file) {
      alert("Por favor, selecciona un archivo");
      return;
    }

    try {
      const result = await uploadExcelFile(file);
      setResponse(result);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error desconocido");
      setResponse(null);
    }
  };

  return (
    <div>
      <h1>Subir Archivo Excel</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" accept=".xlsx, .xls" onChange={handleFileChange} />
        <button type="submit">Subir Archivo</button>
      </form>

      {response && (
        <div>
          <h2>Respuesta del servidor:</h2>
          <p>Estado: {response.status}</p>
          <p>Mensaje: {response.message}</p>
          <h3>Datos del Excel:</h3>
          <pre>{JSON.stringify(response.data, null, 2)}</pre>
        </div>
      )}

      {error && (
        <div style={{ color: "red" }}>
          <h2>Error:</h2>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
};

export default ExcelUploader;
