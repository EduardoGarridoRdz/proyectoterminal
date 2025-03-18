import { styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid2";
import { Typography } from "@mui/material";
import { BarChart } from "@mui/x-charts";
import { LineChart } from "@mui/x-charts";
import { PieChart } from "@mui/x-charts";
import ExcelToJsonConverter from "./SubirExcel";

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: "#fff",
  ...theme.typography.body2,
  textAlign: "center",
  color: theme.palette.text.secondary,
  ...theme.applyStyles("dark", {
    backgroundColor: "#1A2027",
  }),
}));

export default function FullWidthGrid() {
  return (
    <Box>
      <Grid container spacing={0.5}>
        <Grid item size="auto">
          <Item>
            <Typography variant="h5" align="center" gutterBottom>
              Situación de estudiantes por programa educativo
            </Typography>
            <BarChart
              series={[
                { data: [90, 44, 24, 34] },
                { data: [51, 6, 49, 30] },
                { data: [15, 25, 30, 50] },
              ]}
              height={300}
              width={800}
              xAxis={[{ data: ["CBeI", "EyN", "TyGH"], scaleType: "band" }]}
              margin={{ top: 5, bottom: 30, left: 65, right: 30 }}
            />
          </Item>
        </Grid>
        <Grid item size="auto">
          <Item>
            <Typography variant="h5" align="center" gutterBottom>
              Crecimiento de la matrícula por semestre
            </Typography>
            <LineChart
              xAxis={[{ data: [100, 200, 300, 500, 600] }]}
              series={[
                {
                  data: [1, 2, 3, 4, 5],
                },
              ]}
              height={400}
              width={700}
              margin={{ top: 5, bottom: 30, left: 65, right: 30 }}
            />
          </Item>
        </Grid>
        <Grid item size="auto">
          <Item>
            <Typography variant="h5" align="center" gutterBottom>
              Estado general de alumnos
            </Typography>
            <PieChart
              series={[
                {
                  data: [
                    { id: 0, value: 10, label: "Inscrito" },
                    { id: 1, value: 15, label: "Baja temporal" },
                    { id: 2, value: 20, label: "Baja definitiva" },
                  ],
                },
              ]}
              height={400}
              width={500}
              margin={{ top: 5, bottom: 30, left: 65, right: 30 }}
            />
          </Item>
        </Grid>
        <Grid item size="auto">
          <ExcelToJsonConverter></ExcelToJsonConverter>
        </Grid>
      </Grid>
    </Box>
  );
}
