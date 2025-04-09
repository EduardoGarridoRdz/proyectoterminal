import React, { useState } from "react";
import {
  TextField,
  Button,
  Box,
  Typography,
  Container,
  Paper,
  MenuItem,
  Select,
  FormControl,
  InputLabel,
} from "@mui/material";
import Grid from "@mui/material/Grid2"; // Importa Grid2 correctamente

interface FormData {
  nombreProfesor: string;
  proyectoNombre: string;
  tipoEstancia: string;
  asesoria: string;
  estancia: string;
  tutorias: string;
  investigacion: string;
  capacitacion: string;
  tipoCapacitacion: string;
  evento: string;
  faseProyecto: string;
}

const Formulario = () => {
  const [formData, setFormData] = useState<FormData>({
    nombreProfesor: "",
    proyectoNombre: "",
    tipoEstancia: "",
    asesoria: "",
    estancia: "",
    tutorias: "",
    investigacion: "",
    capacitacion: "",
    tipoCapacitacion: "",
    evento: "",
    faseProyecto: "",
  });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSelectChange = (e: any, field: keyof FormData) => {
    setFormData({
      ...formData,
      [field]: e.target.value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/Guardar/`, {

        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        alert("Formulario enviado correctamente");
        setFormData({
          nombreProfesor: "",
          proyectoNombre: "",
          tipoEstancia: "",
          asesoria: "",
          estancia: "",
          tutorias: "",
          investigacion: "",
          capacitacion: "",
          tipoCapacitacion: "",
          evento: "",
          faseProyecto: "",
        });
      } else {
        alert("Hubo un error al enviar el formulario");
      }
    } catch (error) {
      console.error("Error al enviar el formulario", error);
      alert("Hubo un error al enviar el formulario");
    }
  };

  return (
    <Container maxWidth="lg">
      <Paper elevation={3} sx={{ padding: 3 }}>
        <Typography variant="h4" gutterBottom align="center">
          Formulario de Registro Académico
        </Typography>
        <form onSubmit={handleSubmit}>
          <Grid container spacing={3}>
            <Grid xs={12}>
              <TextField
                label="Nombre del Profesor"
                variant="outlined"
                fullWidth
                name="nombreProfesor"
                value={formData.nombreProfesor}
                onChange={handleInputChange}
                required
              />
            </Grid>

            <Grid xs={12}>
              <TextField
                label="Nombre del Proyecto"
                variant="outlined"
                fullWidth
                name="proyectoNombre"
                value={formData.proyectoNombre}
                onChange={handleInputChange}
                required
              />
            </Grid>

            <Grid xs={12}>
              <FormControl fullWidth>
                <InputLabel id="tipoEstanciaLabel">Tipo de Estancia</InputLabel>
                <Select
                  labelId="tipoEstanciaLabel"
                  label="Tipo de Estancia"
                  value={formData.tipoEstancia}
                  onChange={(e) => handleSelectChange(e, "tipoEstancia")}
                >
                  <MenuItem value="EstanciaAcadémica">
                    Estancia Académica
                  </MenuItem>
                  <MenuItem value="EstanciaLaboral">Estancia Laboral</MenuItem>
                  <MenuItem value="EstanciaDeInvestigación">
                    Estancia de Investigación
                  </MenuItem>
                </Select>
              </FormControl>
            </Grid>

            <Grid xs={12}>
              <TextField
                label="Asesoría"
                variant="outlined"
                fullWidth
                name="asesoria"
                value={formData.asesoria}
                onChange={handleInputChange}
              />
            </Grid>

            <Grid xs={12}>
              <TextField
                label="Estancia"
                variant="outlined"
                fullWidth
                name="estancia"
                value={formData.estancia}
                onChange={handleInputChange}
              />
            </Grid>

            <Grid xs={12}>
              <TextField
                label="Tutoría"
                variant="outlined"
                fullWidth
                name="tutorias"
                value={formData.tutorias}
                onChange={handleInputChange}
              />
            </Grid>

            <Grid xs={12}>
              <TextField
                label="Investigación"
                variant="outlined"
                fullWidth
                name="investigacion"
                value={formData.investigacion}
                onChange={handleInputChange}
              />
            </Grid>

            <Grid xs={12}>
              <TextField
                label="Capacitación"
                variant="outlined"
                fullWidth
                name="capacitacion"
                value={formData.capacitacion}
                onChange={handleInputChange}
              />
            </Grid>

            <Grid xs={12}>
              <FormControl fullWidth>
                <InputLabel id="tipoCapacitacionLabel">
                  Tipo de Capacitación
                </InputLabel>
                <Select
                  labelId="tipoCapacitacionLabel"
                  label="Tipo de Capacitación"
                  value={formData.tipoCapacitacion}
                  onChange={(e) => handleSelectChange(e, "tipoCapacitacion")}
                >
                  <MenuItem value="CapacitacionOnline">
                    Capacitación Online
                  </MenuItem>
                  <MenuItem value="CapacitacionPresencial">
                    Capacitación Presencial
                  </MenuItem>
                  <MenuItem value="CapacitacionMixta">
                    Capacitación Mixta
                  </MenuItem>
                </Select>
              </FormControl>
            </Grid>

            <Grid xs={12}>
              <TextField
                label="Evento Académico"
                variant="outlined"
                fullWidth
                name="evento"
                value={formData.evento}
                onChange={handleInputChange}
              />
            </Grid>

            <Grid xs={12}>
              <TextField
                label="Fase del Proyecto"
                variant="outlined"
                fullWidth
                name="faseProyecto"
                value={formData.faseProyecto}
                onChange={handleInputChange}
              />
            </Grid>

            <Grid xs={12}>
              <Box textAlign="center">
                <Button
                  type="submit"
                  variant="contained"
                  color="primary"
                  size="large"
                >
                  Enviar Formulario
                </Button>
              </Box>
            </Grid>
          </Grid>
        </form>
      </Paper>
    </Container>
  );
};

export default Formulario;
