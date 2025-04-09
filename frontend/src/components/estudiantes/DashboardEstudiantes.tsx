import { useState, useEffect } from "react";
import Grid from "@mui/material/Grid2";

export default function DashboardEstudiantes() {
  const [windowSize, setWindowSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight,
  });

  useEffect(() => {
    function handleResize() {
      setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    }

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  // Ajustamos las dimensiones del iframe con márgenes
  const iframeWidth = Math.min(windowSize.width * 0.95, 1920); // 95% del ancho o máximo 1800px
  const iframeHeight = Math.min(windowSize.height * 0.8, 1080); // 90% del alto o máximo 1000px

  return (
    <Grid container spacing={1}>
      <Grid item xs={12}></Grid>
    </Grid>
  );
}
