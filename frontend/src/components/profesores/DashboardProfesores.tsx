import { Box, Typography } from "@mui/material";

export default function FullScreenDashboard() {
  return (
    <Box 
      sx={{ 
        width: "100vw", 
        height: "100vh", 
        display: "flex", 
        flexDirection: "column", 
        alignItems: "center", 
        justifyContent: "center", 
        overflow: "hidden",
        padding: 2 
      }}
    >
      <Typography variant="h4" align="center" gutterBottom>
        Dashboard Profesores
      </Typography>
      <Box 
        sx={{ 
          width: "80%",  // Hace el dashboard más pequeño
          height: "85vh",  // Ajusta la altura para mejor visibilidad
          borderRadius: "10px",
          overflow: "hidden",
          boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)" 
        }}
      >
        <iframe
          src="https://lookerstudio.google.com/embed/reporting/6a99475f-4315-4f9f-be4d-5f8b259160e4/page/QnoFF" // El enlace de tu Looker Studio
          width="100%" 
          height="100%" 
          frameBorder="0"
          style={{ border: 0, borderRadius: "10px" }}
          allowFullScreen
        ></iframe>
      </Box>
    </Box>
  );
}
