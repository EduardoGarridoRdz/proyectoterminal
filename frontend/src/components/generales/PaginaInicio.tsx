import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import { createTheme } from "@mui/material/styles";
import { AppProvider } from "@toolpad/core/AppProvider";
import { DashboardLayout } from "@toolpad/core/DashboardLayout";
import getNavigation from "./Navegacion";
import { useDemoRouter } from "@toolpad/core/internal";
import BasicLineChart from "../estudiantes/ServiciosEscolares";

const NAVIGATION = getNavigation();

const BRANDING = {
  logo: "",
  title: "Departamento de planeación",
};

const demoTheme = createTheme({
  cssVariables: {
    colorSchemeSelector: "data-toolpad-color-scheme",
  },
  colorSchemes: { light: true, dark: true },
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 600,
      lg: 1200,
      xl: 1536,
    },
  },
});

function DemoPageContent({ pathname }: { pathname: string }) {
  return (
   <>
      <Typography>Ruta actual: {pathname}</Typography>

      {pathname === "/estudiantes/dashboard-estudiantes" && (
       <BasicLineChart></BasicLineChart>        
      )}
      {pathname === "/dashboard" && (
        <Typography>Bienvenido al Dashboard</Typography>
      )}
      {pathname === "/otra-ruta" && <Typography>Esta es otra ruta</Typography>}
    </>
  );
}

interface DemoProps {
  window?: () => Window;
}

export default function PaginaInicio(props: DemoProps) {
  const { window } = props;

  const router = useDemoRouter();

  // Remove this const when copying and pasting into your project.
  const demoWindow = window !== undefined ? window() : undefined;

  return (
    // preview-start
    <AppProvider
      navigation={NAVIGATION}
      router={router}
      branding={BRANDING}
      theme={demoTheme}
      window={demoWindow}
    >
      <DashboardLayout>
        <DemoPageContent pathname={router.pathname} />
      </DashboardLayout>
    </AppProvider>
    // preview-end
  );
}
