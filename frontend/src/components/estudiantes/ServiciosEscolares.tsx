import { LineChart } from "@mui/x-charts/LineChart";
import InputFileUpload from "../generales/SubirArchivos";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid2";
import { BarChart } from "@mui/x-charts";
import { PieChart } from "@mui/x-charts";
import { Typography } from "@mui/material";

export default function BasicLineChart() {
  return (
    <>
      <Box sx={{ width: "100%" }}>
        <Grid container rowSpacing={10}>
          <Grid size={5}>
            <Typography variant="h5" align="center" gutterBottom>
              Situación de estudiantes por programa educativo
            </Typography>
            <BarChart
              series={[
                { data: [90, 44, 24, 34] },
                { data: [51, 6, 49, 30] },
                { data: [15, 25, 30, 50] },
              ]}
              height={400}
              width={600}
              xAxis={[{ data: ["CBeI", "EyN", "TyGH"], scaleType: "band" }]}
              margin={{ top: 10, bottom: 30, left: 100, right: 10 }}
            />
          </Grid>
          <Grid size={5}>
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
              width={600}
              margin={{ top: 10, bottom: 30, left: 100, right: 10 }}
            />
          </Grid>
          <Grid>
            <PieChart
              series={[
                {
                  data: [
                    { id: 0, value: 10, label: "series A" },
                    { id: 1, value: 15, label: "series B" },
                    { id: 2, value: 20, label: "series C" },
                  ],
                },
              ]}
              width={400}
              height={200}
            />
          </Grid>
          <Grid size={6}>
            <InputFileUpload></InputFileUpload>
          </Grid>
        </Grid>
      </Box>
    </>
  );
}
