import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api"; // Cambia esto por la URL de tu API de Django

export const fetchData = async (endpoint: string) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/${endpoint}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

export const postData = async (endpoint: string, data: any) => {
    const response = await fetch(`http://localhost:8000/api/${endpoint}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });

    if (!response.ok) {
        throw new Error("Error al enviar los datos");
    }

    return response.json();
};
