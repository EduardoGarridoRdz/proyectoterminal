import React, { useState } from "react";
import {
  TextField,
  Button,
  Grid,
  Container,
  Paper,
  Typography,
  Autocomplete,
  MenuItem,
  FormControl,
  InputLabel,
  Select,
  SelectChangeEvent,
} from "@mui/material";

const nombresProfesores = [
  "Dr. Mauro Felipe Berumen Calderón",
  "Dr. César Yáñez Santamaría",
  "Dra. Angelica Sterling Zozoaga",
  "Dr. Edgar Fernando Peña Torres",
  "Dr. Héctor Santana Duarte",
  "Mtra. Guadalupe Carolina Moreno Ortíz",
  "Mtra. Ana Victoria Flores Vega",
  "Mtro. Juan Manuel Carvajal Sánchez",
  "Mtra. Elena Xitlali Gamarra Hernández",
  "Mtro. Guillermo Álvarez Estrada",
  "Mtro. Bernardo Lopez Rivera",
  "Mtra. Sonia Beatriz Pacheco Castro",
  "Dr. José Francisco Domínguez Estrada",
  "Dr. Ricardo Sonda de la Rosa",
  "Dr. Pedro Moncada Jiménez",
  "Dr. Ventura Enrique Mota Flores",
  "Dr. Oswaldo Gallegos Jiménez",
  "Dr. Jorge Mendoza Lara",
  "Dra. Sandra Guerra Mondragon",
  "Mtra. Damayanti Estolano Cristerna",
  "Mtra. Consepción Escalona Hernández",
  "Mtra. Claudia Inés Martinez",
  "Dr. Juan Bautista Boggio Vázquez",
  "Dr. Abelardo Castillo Galeana",
  "Dra. Rosiluz Ceballos Povedano",
  "Dr. Enrique Corona Sandoval",
  "Mtra. Wendy Sebastiana Hernández Del Puerto",
  "Dra. Lorena Hernández Von Wobeser",
  "Mtro. Francisco José May Hernández",
  "Mtro. Farid Alfonso Pool Estrada",
  "Dra. Carmen Lilia Cervantes Bello",
  "Dr. Sergio Lagunas Puls",
  "Dra. Elda Leticia León Vite",
  "Dra. Christine Elizabeth Mccoy Cador",
  "Dr. Miguel Ángel Olivares Urbina",
  "Mtra. Brenda Lizeth Soto Pérez",
  "Mtro. Jorge Vallejo Filoteo",
  "Dra. Lucila Zárraga Cano",
  "Dr. Rodrigo Leonardo Guillen Breton",
  "Dr. Juan Francisco Bárcenas Graniel",
  "Dra. Estela Cerezo Acevedo",
  "Dr. Víctor Manuel Romero Medina",
  "Dra. Laura Margarita Hernández Terrones",
  "Mtra. Nancy Aguas García",
  "Dra. Jessica Carmin Mendiola Fuentes",
  "Dra. Erika Zavala López",
  "Dr. Héctor Fernando Gómez García",
  "Dr. Ismael Domínguez Jiménez",
  "Dr. César Hernández Brito",
  "Dra. Candelaria Elizabeth Sansores Pérez",
  "Mtro. Francisco Manzano Pinzón",
  "Dra. Marina Isabel García Rosas",
  "Mtra. Diana del Pilar Cobos del Angel",
  "Dr. Antonio José Sucre Salas",
  "Dra. Mirbella Gallareta Negrón",
  "Dr. Alejandro Charbel Cárdenas León",
  "Dr. Juan Felipe Pérez Vázquez",
  "Mtro. Nicolás Francisco Mateo Díaz",
  "Mtro. Jarmen Said Virgen Suárez",
  "Dr. Francisco López Monzalvo",
  "Dr. Mijaíl Armenta Aranceta",
  "Dr. Víctor Cantero Flores",
  "Mtro. Victor Manuel Peralta Del Riego",
  "Dra. Alejandra Cazal Ferreira",
  "Mtro. Eduardo Suárez Díaz Barriga",
  "Dra. María del Pilar Jiménez Márquez",
  "Mtro. Roberto Parra Dorantes",
  "Dra. Sabrina Ivonne Rodríguez Ogaz",
  "Mtra. Graciela Vázquez Flores",
  "Mtra. Pilivet Aguiar Alayola",
  "Dr. Oscar Miguel Reyes Hernández",
  "Dra. Minerva Alavez San Pedro",
  "Dra. Libertad Fidelina Díaz Molina",
  "Dr. José Felipe Reyes Miranda",
];

const tiposProyecto = ["Investigación", "Artículo", "Desarrollo tecnológico"];

interface FormData {
  nombreProfesor: string;
  proyectoNombre: string;
  tipoProyecto: string;
  colaboradores: string;
  institucionColaboradora: string;
  resultadosImpactos: string;
}

const ProyectoInvestigacionForm = () => {
  const [formData, setFormData] = useState<FormData>({
    nombreProfesor: "",
    proyectoNombre: "",
    tipoProyecto: "",
    colaboradores: "",
    institucionColaboradora: "",
    resultadosImpactos: "",
  });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSelectChange = (e: SelectChangeEvent, field: keyof FormData) => {
    setFormData({ ...formData, [field]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:8000/api/proyectos-investigacion/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        alert("Proyecto enviado correctamente");
        setFormData({
          nombreProfesor: "",
          proyectoNombre: "",
          tipoProyecto: "",
          colaboradores: "",
          institucionColaboradora: "",
          resultadosImpactos: "",
        });
      } else {
        alert("Error al enviar el proyecto");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Error al enviar el proyecto");
    }
  };

  return (
    <Container maxWidth="md">
      <Paper elevation={3} sx={{ p: 4 }}>
        <Typography variant="h5" align="center" gutterBottom>
          Proyecto de Investigación
        </Typography>
        <form onSubmit={handleSubmit}>
          <Grid container spacing={2} direction="column">
            <Grid item xs={12}>
              <Autocomplete
                options={nombresProfesores}
                value={formData.nombreProfesor}
                onChange={(e, newValue) =>
                  setFormData({ ...formData, nombreProfesor: newValue || "" })
                }
                renderInput={(params) => (
                  <TextField {...params} label="Nombre del Profesor" required fullWidth />
                )}
              />
            </Grid>

            <Grid item xs={12}>
              <TextField
                label="Nombre del Proyecto"
                name="proyectoNombre"
                value={formData.proyectoNombre}
                onChange={handleInputChange}
                fullWidth
                required
              />
            </Grid>

            <Grid item xs={12}>
              <FormControl fullWidth>
                <InputLabel id="tipoProyectoLabel">Tipo de Proyecto</InputLabel>
                <Select
                  labelId="tipoProyectoLabel"
                  label="Tipo de Proyecto"
                  value={formData.tipoProyecto}
                  onChange={(e) => handleSelectChange(e, "tipoProyecto")}
                >
                  {tiposProyecto.map((tipo) => (
                    <MenuItem key={tipo} value={tipo}>
                      {tipo}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>

            <Grid item xs={12}>
              <TextField
                label="Colaboradores"
                name="colaboradores"
                value={formData.colaboradores}
                onChange={handleInputChange}
                fullWidth
              />
            </Grid>

            <Grid item xs={12}>
              <TextField
                label="Institución Colaboradora"
                name="institucionColaboradora"
                value={formData.institucionColaboradora}
                onChange={handleInputChange}
                fullWidth
              />
            </Grid>

            <Grid item xs={12}>
              <TextField
                label="Resultados o Impacto"
                name="resultadosImpactos"
                value={formData.resultadosImpactos}
                onChange={handleInputChange}
                multiline
                rows={4}
                fullWidth
              />
            </Grid>

            <Grid item xs={12}>
              <Button type="submit" variant="contained" color="primary" fullWidth>
                Enviar Proyecto
              </Button>
            </Grid>
          </Grid>
        </form>
      </Paper>
    </Container>
  );
};

export default ProyectoInvestigacionForm;
