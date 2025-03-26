import { styled } from "@mui/material";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid2";

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: "#fff",
  ...theme.typography.body2,
  textAlign: "center",
  color: theme.palette.text.secondary,
  ...theme.applyStyles("dark", {
    backgroundColor: "#1A2027",
  }),
}));

export default function DashboardEstudiantes() {
  return (
    <Grid container spacing={1}>
      <Grid item size="auto">
        <Item>
          <iframe
            width="1800"
            height="1000"
            src="https://lookerstudio.google.com/embed/reporting/d653d448-0ca3-497b-94b7-d018dee82059/page/R0QEF"
            sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"
          ></iframe>
        </Item>
      </Grid>
    </Grid>
  );
}
