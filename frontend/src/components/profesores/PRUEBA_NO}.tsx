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
  Autocomplete,
  Checkbox,
  FormControlLabel,
  FormControl,
  InputLabel,
  Select,
  SelectChangeEvent,
} from "@mui/material";

const departamentos = [
  "Turismo Sustentable, Gastronomía y Hotelería",
  "Ingeniería",
  "Ciencias Sociales",
];

const programas = [
  "Gastronomía",
  "Turismo",
  "Ingeniería en Datos",
];

const profesores = [
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

const sexos = ["Hombre", "Mujer"];
const grados = ["Doctorado", "Maestría"];

const FormularioRH = () => {
  const [formData, setFormData] = useState({
    departamento: "",
    programa: "",
    profesor: "",
    sexo: "",
    grado: "",
    institucionTitulo: "",
    fechaGrado: "",
    estudiaDoctorado: false,
    institucionDoctorado: "",
  });

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement> | SelectChangeEvent
  ) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleCheckboxChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, checked } = e.target;
    setFormData({ ...formData, [name]: checked });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Datos enviados:", formData);
    // fetch al backend con los campos que sí se guardan
  };

  return (
    <Container maxWidth="md">
      <Paper sx={{ p: 4 }}>
        <Typography variant="h5" gutterBottom>
          Información de Recursos Humanos - Profesor
        </Typography>
        <form onSubmit={handleSubmit}>
          <Grid container spacing={2}>
            {/* Campos válidos */}
            <Grid item xs={12} sm={6}>
              <FormControl fullWidth>
                <InputLabel>Departamento Académico</InputLabel>
                <Select
                  name="departamento"
                  value={formData.departamento}
                  label="Departamento Académico"
                  onChange={handleChange}
                >
                  {departamentos.map((dep) => (
                    <MenuItem key={dep} value={dep}>
                      {dep}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>

            <Grid item xs={12} sm={6}>
              <FormControl fullWidth>
                <InputLabel>Programa Educativo</InputLabel>
                <Select
                  name="programa"
                  value={formData.programa}
                  label="Programa Educativo"
                  onChange={handleChange}
                >
                  {programas.map((prog) => (
                    <MenuItem key={prog} value={prog}>
                      {prog}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>

            <Grid item xs={12}>
              <Autocomplete
                options={profesores}
                value={formData.profesor}
                onChange={(e, newValue) =>
                  setFormData({ ...formData, profesor: newValue || "" })
                }
                renderInput={(params) => (
                  <TextField {...params} label="Nombre del Profesor" fullWidth />
                )}
              />
            </Grid>

            <Grid item xs={12} sm={6}>
              <FormControl fullWidth>
                <InputLabel>Sexo</InputLabel>
                <Select
                  name="sexo"
                  value={formData.sexo}
                  label="Sexo"
                  onChange={handleChange}
                >
                  {sexos.map((sexo) => (
                    <MenuItem key={sexo} value={sexo}>
                      {sexo}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>

            <Grid item xs={12} sm={6}>
              <FormControl fullWidth>
                <InputLabel>Grado Académico</InputLabel>
                <Select
                  name="grado"
                  value={formData.grado}
                  label="Grado Académico"
                  onChange={handleChange}
                >
                  {grados.map((grado) => (
                    <MenuItem key={grado} value={grado}>
                      {grado}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>

            <Grid item xs={12}>
              <TextField
                name="institucionTitulo"
                value={formData.institucionTitulo}
                onChange={handleChange}
                fullWidth
                label="Institución que otorgó el título"
              />
            </Grid>

            <Grid item xs={12} sm={6}>
              <TextField
                type="date"
                name="fechaGrado"
                value={formData.fechaGrado}
                onChange={handleChange}
                label="Fecha de obtención del grado"
                fullWidth
                InputLabelProps={{ shrink: true }}
              />
            </Grid>

            <Grid item xs={12}>
              <FormControlLabel
                control={
                  <Checkbox
                    checked={formData.estudiaDoctorado}
                    onChange={handleCheckboxChange}
                    name="estudiaDoctorado"
                  />
                }
                label="¿Está estudiando un doctorado?"
              />
            </Grid>

            {formData.estudiaDoctorado && (
              <Grid item xs={12}>
                <TextField
                  name="institucionDoctorado"
                  value={formData.institucionDoctorado}
                  onChange={handleChange}
                  fullWidth
                  label="Institución donde estudia el doctorado"
                />
              </Grid>
            )}

            {/* Campos solo visibles */}
            <Grid item xs={12}>
              <Typography variant="subtitle1" fontWeight="bold">
                Información adicional (no se guarda):
              </Typography>
            </Grid>

            {[
              "¿Cuenta con Perfil PRODEP?",
              "Vigencia del Perfil PRODEP",
              "¿Es miembro del SNII o SEII?",
              "Nivel SNI / SEII",
              "Año de ingreso a SNI / SEII",
            ].map((label) => (
              <Grid item xs={12} sm={6} key={label}>
                <TextField label={label} disabled fullWidth />
              </Grid>
            ))}

            <Grid item xs={12}>
              <Box textAlign="center">
                <Button type="submit" variant="contained">
                Enviar Información

                </Button>
              </Box>
            </Grid>
          </Grid>
        </form>
      </Paper>
    </Container>
  );
};

export default FormularioRH;
