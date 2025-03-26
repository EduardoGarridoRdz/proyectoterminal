import * as React from "react";
import { styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid2";
import AssignmentIndIcon from "@mui/icons-material/AssignmentInd";
import { Typography } from "@mui/material";

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: "#fff",
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: "center",
  color: theme.palette.text.secondary,
  ...theme.applyStyles("dark", {
    backgroundColor: "#1A2027",
  }),
}));

export default function Estudiantes() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Grid container spacing={2}>
        <Grid size={6}>
          <Item
            sx={{
              height: "250px",
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <AssignmentIndIcon center />
            <Typography center>Dashboard Estudiantes</Typography>
          </Item>
        </Grid>
        <Grid size={6} sx={{ height: "250px" }}>
          <Item
            sx={{
              height: "250px",
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <AssignmentIndIcon center />
            <Typography center>Servicios Escolares</Typography>
          </Item>
        </Grid>
        <Grid size={6} sx={{ height: "250px" }}>
          <Item
            sx={{
              height: "250px",
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <AssignmentIndIcon center />
            <Typography center>Servicio Social</Typography>
          </Item>
        </Grid>
        <Grid size={6} sx={{ height: "250px" }}>
          <Item
            sx={{
              height: "250px",
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <AssignmentIndIcon center />
            <Typography center>Desarrollo estudiantil</Typography>
          </Item>
        </Grid>
        <Grid size={6}>
          <Item
            sx={{
              height: "250px",
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <AssignmentIndIcon center />
            <Typography center>Desarrollo académico</Typography>
          </Item>
        </Grid>
        <Grid size={6}>
          <Item
            sx={{
              height: "250px",
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <AssignmentIndIcon center />
            <Typography center>Vinculación Universitaria</Typography>
          </Item>
        </Grid>
      </Grid>
    </Box>
  );
}
