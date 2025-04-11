import React, { useState } from "react";
import {
  TextField,
  Button,
  Typography,
  Box,
  Container,
  Paper,
  Grid,
} from "@mui/material";

const ActividadVinculacion = () => {
  const [formData, setFormData] = useState({
    institucionVinculada: "",
    descripcionActividad: "",
    fechaVinculacion: "",
    resultadoVinculacion: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Datos enviados:", formData);
    // Aquí puedes conectar con tu backend
  };

  return (
    <Container maxWidth="md">
      <Paper sx={{ p: 4 }}>
        <Typography variant="h6" gutterBottom>
          Actividad de Vinculación
        </Typography>
        <form onSubmit={handleSubmit}>
          <Grid container spacing={2} direction="column">
            <Grid item>
              <TextField
                label="Institución vinculada"
                name="institucionVinculada"
                value={formData.institucionVinculada}
                onChange={handleChange}
                fullWidth
              />
            </Grid>
            <Grid item>
              <TextField
                label="Descripción de la actividad"
                name="descripcionActividad"
                value={formData.descripcionActividad}
                onChange={handleChange}
                fullWidth
                multiline
              />
            </Grid>
            <Grid item>
              <TextField
                label="Fecha de vinculación"
                type="date"
                name="fechaVinculacion"
                value={formData.fechaVinculacion}
                onChange={handleChange}
                InputLabelProps={{ shrink: true }}
                fullWidth
              />
            </Grid>
            <Grid item>
              <TextField
                label="Resultado de la vinculación"
                name="resultadoVinculacion"
                value={formData.resultadoVinculacion}
                onChange={handleChange}
                fullWidth
              />
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

export default ActividadVinculacion;