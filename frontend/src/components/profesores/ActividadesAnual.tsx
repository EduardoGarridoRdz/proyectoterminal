import React, { useState } from "react";
import {
  TextField,
  Button,
  Typography,
  Box,
  Container,
  Paper,
  Grid
} from "@mui/material";

const ActividadesAnuales = () => {
  const [formData, setFormData] = useState({
    sedeActividad: "",
    productosAcademicos: "",
    anioPublicacion: "",
    linkProducto: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Datos enviados:", formData);
    // Aquí puedes hacer fetch POST al backend
  };

  return (
    <Container maxWidth="md">
      <Paper sx={{ p: 4 }}>
        <Typography variant="h6" gutterBottom>
          Actividades Anuales
        </Typography>
        <form onSubmit={handleSubmit}>
          <Grid container spacing={2} direction="column">
            <Grid item>
              <TextField
                label="Sede de la actividad"
                name="sedeActividad"
                value={formData.sedeActividad}
                onChange={handleChange}
                fullWidth
              />
            </Grid>
            <Grid item>
              <TextField
                label="Productos académicos"
                name="productosAcademicos"
                value={formData.productosAcademicos}
                onChange={handleChange}
                fullWidth
              />
            </Grid>
            <Grid item>
              <TextField
                label="Año de publicación"
                name="anioPublicacion"
                value={formData.anioPublicacion}
                onChange={handleChange}
                fullWidth
                type="number"
              />
            </Grid>
            <Grid item>
              <TextField
                label="Link del producto (URL)"
                name="linkProducto"
                value={formData.linkProducto}
                onChange={handleChange}
                fullWidth
                type="url"
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

export default ActividadesAnuales;
