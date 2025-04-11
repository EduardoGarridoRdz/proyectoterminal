import React, { useState, useEffect } from "react";
import Grid from "@mui/material/Grid2";
import { Typography } from "@mui/material";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import SendIcon from '@mui/icons-material/Send';
import MenuItem from '@mui/material/MenuItem';


const tipo_usuario = [
  {
    value: 'administrador',
    label: 'Administrador',
  },
  {
    value: 'jefe_departamento',
    label: 'Jefe de Departamento',
  },
  {
    value: 'profesor',
    label: 'Profesor',
  }
];

const departamentos = [
  {
    value: 'Servicios Escolares',
    label: 'Servicios Escolares'
  },
  {
    value: 'Servicio Social',
    label: 'Servicio Social'
  },
  {
    value: 'Practicas Profesionales',
    label: 'Prácticas Profesionales'
  },
  {
    value: 'Idiomas',
    label: 'Idiomas'
  },
  {
    value: 'Desarrollo Estudiantil',
    label: 'Desarrollo Estudiantil'
  },
  {
    value: 'Vinculacion Universitaria',
    label: 'Vinculación Universitaria'
  },
  {
    value: 'Desarrollo Humano',
    label: 'Desarrollo Humano'
  },
  {
    value: 'Ciencias Basicas e Ingenierias',
    label: 'Ciencias Básicas e Ingenierías'
  },
  {
    value: 'Turismo Sustentable, Gastronomia y Hoteleria',
    label: 'Turismo Sustentable, Gastronomía y Hotelería'
  },
  {
    value: 'Desarrollo Academico',
    label: 'Desarrollo Académico'
  },
  {
    value: 'Economia y Negocios',
    label: 'Economía y Negocios'
  },
  {
    value: 'Departamento de Investigacion',
    label: 'Departamento de Investigación'
  },
  {
    value: 'Recursos Humanos',
    label: 'Recursos Humanos'
  },
]

export default function AñadirUsuario() {

  return (
    <>
      <Grid container spacing={5} direction="column"
        sx={{
          justifyContent: "center",
          alignItems: "center",
          pt: 5,
        }}
      >
        <Typography variant="h6"> Nombre:
          <TextField
            sx={{ width: "600px", pl: 1 }}
            id="nombre"
            label="nombre"
            variant="outlined"
            required
          />
        </Typography>

        <Typography variant="h6"> Apellido Paterno:
          <TextField
            sx={{ width: "600px", pl: 1 }}
            id="apellido_pat"
            label="Apellido Paterno"
            variant="outlined"
            required
          />
        </Typography>

        <Typography variant="h6"> Apellido Materno:
          <TextField
            sx={{ width: "600px", pl: 1 }}
            id="apellido_mat"
            label="Apellido Materno"
            variant="outlined"
            required
          />
        </Typography>

        <Typography variant="h6"> Correo:
          <TextField
            sx={{ width: "600px", pl: 1 }}
            id="Correo"
            label="Correo"
            variant="outlined"
            required
          />
        </Typography>

        <TextField
          id="outlined-select-currency"
          select
          label="Seleccionar tipo de usuario"
          defaultValue="Administrador"
          helperText="Selecciona el tipo de usuario"
        >
          {tipo_usuario.map((option) => (
            <MenuItem key={option.value} value={option.value}>
              {option.label}
            </MenuItem>
          ))}
        </TextField>

        <TextField
          id="outlined-select-currency"
          select
          label="Seleccionar Departamento"
          defaultValue=" "
          helperText="Selecciona el departamento del usuario"
        >
          {departamentos.map((option) => (
            <MenuItem key={option.value} value={option.value}>
              {option.label}
            </MenuItem>
          ))}
        </TextField>

        <Button variant="outlined" startIcon={<SendIcon />}>
          Envíar
        </Button>



      </Grid>
    </>
  );
}
