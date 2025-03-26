import { styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid2";
import { Typography } from "@mui/material";
import { BarChart } from "@mui/x-charts";
import { LineChart } from "@mui/x-charts";
import { PieChart } from "@mui/x-charts";
import SubirExcel from "./SubirExcel";

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: "#fff",
  ...theme.typography.body2,
  textAlign: "center",
  color: theme.palette.text.secondary,
  ...theme.applyStyles("dark", {
    backgroundColor: "#1A2027",
  }),
}));

export default function ServiciosEscolares() {
  return (
    <Box>
      <Grid container spacing={0.5}>
        <Grid item size="auto">
          <SubirExcel />
        </Grid>
      </Grid>
    </Box>
  );
}
