import React, { useState } from "react";
import {
  TextField,
  MenuItem,
  Button,
  Typography,
  Box,
  Container,
  Paper,
  Grid,
  Autocomplete
} from "@mui/material";

interface GradoAcademico {
  id: number;
  nombre: string;
}

interface FaseProyecto {
  id: number;
  nombre: string;
}

interface FormData {
  nombreProfesor: string;
  gradoAcademico: number | null;
  institucionTitulo: string;
  fechaGrado: string;
  capacitacion: string;
  evento: string;
  faseProyecto: number | null;
}

const FormacionAcademica = () => {
  const [formData, setFormData] = useState<FormData>({
    nombreProfesor: "",
    gradoAcademico: null,
    institucionTitulo: "",
    fechaGrado: "",
    capacitacion: "",
    evento: "",
    faseProyecto: null,
  });

  const grados: GradoAcademico[] = [
    { id: 1, nombre: "Licenciatura" },
    { id: 2, nombre: "Maestría" },
    { id: 3, nombre: "Doctorado" },
  ];

  const fases: FaseProyecto[] = [
    { id: 1, nombre: "Fase 1" },
    { id: 2, nombre: "Fase 2" },
    { id: 3, nombre: "Fase 3" },
  ];

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

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Datos a enviar:", formData);
    // Aquí va tu lógica de envío (fetch POST)
  };

  return (
    <Container maxWidth="md">
      <Paper sx={{ p: 4 }}>
        <Typography variant="h6" gutterBottom>
          Formación Personal Académica
        </Typography>
        <form onSubmit={handleSubmit}>
          <Grid container spacing={2} direction="column">
            <Grid item>
              <Autocomplete
                options={nombresProfesores}
                value={formData.nombreProfesor}
                onChange={(e, newValue) =>
                  setFormData({ ...formData, nombreProfesor: newValue || "" })
                }
                renderInput={(params) => (
                  <TextField {...params} label="Nombre del Profesor" required />
                )}
              />
            </Grid>
            <Grid item>
              <TextField
                select
                label="Grado Académico"
                fullWidth
                name="gradoAcademico"
                value={formData.gradoAcademico || ""}
                onChange={handleChange}
                required
              >
                {grados.map((grado) => (
                  <MenuItem key={grado.id} value={grado.id}>
                    {grado.nombre}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid item>
              <TextField
                fullWidth
                label="Institución que otorgó el título"
                name="institucionTitulo"
                value={formData.institucionTitulo}
                onChange={handleChange}
                required
              />
            </Grid>
            <Grid item>
              <TextField
                type="date"
                label="Fecha de obtención del grado"
                name="fechaGrado"
                value={formData.fechaGrado}
                onChange={handleChange}
                InputLabelProps={{ shrink: true }}
                fullWidth
                required
              />
            </Grid>
            <Grid item>
              <TextField
                label="Capacitación reciente"
                name="capacitacion"
                value={formData.capacitacion}
                onChange={handleChange}
                fullWidth
              />
            </Grid>
            <Grid item>
              <TextField
                label="Evento Académico"
                name="evento"
                value={formData.evento}
                onChange={handleChange}
                fullWidth
              />
            </Grid>
            <Grid item>
              <TextField
                select
                label="Fase del Proyecto"
                name="faseProyecto"
                value={formData.faseProyecto || ""}
                onChange={handleChange}
                fullWidth
              >
                {fases.map((fase) => (
                  <MenuItem key={fase.id} value={fase.id}>
                    {fase.nombre}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid item>
              <Box textAlign="center">
                <Button variant="contained" type="submit">
                  Guardar Información
                </Button>
              </Box>
            </Grid>
          </Grid>
        </form>
      </Paper>
    </Container>
  );
};

export default FormacionAcademica;
