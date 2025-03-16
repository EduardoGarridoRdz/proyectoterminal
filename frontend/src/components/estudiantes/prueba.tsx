// src/components/MyComponent.tsx
import React, { useEffect, useState } from "react";
import { fetchData } from "../../API/api";

// Define las props del componente
interface MyComponentProps {
  endpoint: string; // Prop para el endpoint dinámico
  title: string; // Prop para el título dinámico
  dataKeys: string[]; // Prop para la clave del dato a mostrar
}

const MyComponent: React.FC<MyComponentProps> = ({
  endpoint,
  title,
  dataKeys,
}) => {
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const getData = async () => {
      try {
        const result = await fetchData(endpoint); // Usa el endpoint dinámico
        setData(result);
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setLoading(false);
      }
    };

    getData();
  }, [endpoint]); // Dependencia: si el endpoint cambia, se vuelve a ejecutar

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{title}</h1>
      <ul>
        {data.map((item, index) => (
          <li key={index}>
            {dataKeys.map((key) => (
              <div key={key}>
                <strong>{key}:</strong> {item[key]}
              </div>
            ))}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MyComponent;
