import React, { useState } from "react";
import readXlsxFile from "read-excel-file";
import { Button } from "@mui/material";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";
import { styled } from "@mui/material/styles";

const VisuallyHiddenInput = styled("input")({
  clip: "rect(0 0 0 0)",
  clipPath: "inset(50%)",
  height: 1,
  overflow: "hidden",
  position: "absolute",
  bottom: 0,
  left: 0,
  whiteSpace: "nowrap",
  width: 1,
});

const ExcelToJsonConverter: React.FC = () => {
  const [jsonData, setJsonData] = useState<Array<Record<string, any>> | null>(
    null
  );

  const handleFileChange = async (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const file = event.target.files?.[0];
    if (!file) {
      alert("Por favor, selecciona un archivo.");
      return;
    }

    try {
      // Leer el archivo Excel
      const rows = await readXlsxFile(file);

      // Mostrar el JSON en la consola
      console.log("Datos convertidos a JSON:", rows);

      // Guardar el JSON en el estado (opcional, si quieres mostrarlo en la UI)
      setJsonData(rows);

      // Enviar el JSON al backend
      const response = await fetch("http://127.0.0.1:8000/api/recibirDatos/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(rows), // Envía el JSON como cuerpo de la solicitud
      });

      if (response.ok) {
        console.log("JSON enviado correctamente al backend.");
      } else {
        console.error("Error al enviar el JSON al backend.");
      }
    } catch (error) {
      console.error("Error al leer el archivo o enviar el JSON:", error);
      alert("Hubo un error al procesar el archivo.");
    }
  };

  return (
    <Button
      component="label"
      role={undefined}
      variant="contained"
      tabIndex={-1}
      startIcon={<CloudUploadIcon />}
    >
      Subir archivos
      <VisuallyHiddenInput type="file" onChange={handleFileChange} multiple />
    </Button>

    /*<div>
      <h1>Cargar y convertir archivo Excel a JSON</h1>
      <input type="file" accept=".xlsx, .xls" onChange={handleFileChange} />
      {jsonData && (
        <div>
          <h2>Datos convertidos:</h2>
          <pre>{JSON.stringify(jsonData, null, 2)}</pre>
        </div>
      )}
    </div>*/
  );
};

export default ExcelToJsonConverter;
