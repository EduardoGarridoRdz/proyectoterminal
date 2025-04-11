import Typography from "@mui/material/Typography";
import { createTheme } from "@mui/material/styles";
import { AppProvider } from "@toolpad/core/AppProvider";
import { DashboardLayout } from "@toolpad/core/DashboardLayout";
import getNavigation from "./Navegacion";
import { useDemoRouter } from "@toolpad/core/internal";
import ServiciosEscolares from "../estudiantes/ServiciosEscolares";
import DashboardProfesores from "../profesores/DashboardProfesores";
import DashboardEstudiantes from "../estudiantes/DashboardEstudiantes";
import Estudiantes from "../estudiantes/DashboardEstudiantes";
import Formulario from "../profesores/Formulario";
import PracticasProfesionales from "../estudiantes/PracticasProfesionales";
import DesarrolloEstudiantil from "../estudiantes/DesarrolloEstudiantil";
import ServicioSocial from "../estudiantes/ServicioSocial";
import AñadirUsuario from "./AñadirUsuario";
import Idiomas from "../estudiantes/Idiomas";
import logouni from "../../assets/logo.png"; // Ensure the path is correct
import Direccion from "../profesores/Direccion";
import Formacion from "../profesores/FormacionPersonal";
import Proyecto from "../profesores/ProyectosInvestigacion";
import Anual from "../profesores/ActividadesAnual";
import Vinculacion from "../profesores/ActividadVinculacion";

const NAVIGATION = getNavigation();

const BRANDING = {
  logo: (
    <img
      src={logouni}
      alt="Universidad del Caribe"
      style={{ height: 50, width: 40 }}
    />
  ),
  title: "Secretaría de Planeación y Desarrollo Institucional",
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
      {pathname === "/estudiantes" && (
        <Estudiantes />)
      }
      {pathname === "/estudiantes/dashboard-estudiantes" && (
        <DashboardEstudiantes />
      )}
      {pathname === "/estudiantes/servicios-escolares" && (
        <ServiciosEscolares />
      )}
      {pathname === "/estudiantes/practicas-profesionales" && (
        <PracticasProfesionales />
      )}
      {pathname === "/estudiantes/desarrollo-estudiantil" && (
        <DesarrolloEstudiantil />
      )}
      {pathname === "/estudiantes/idiomas" && (
        <Idiomas />)
      }
      {pathname === "/estudiantes/servicio-social" && (
        <ServicioSocial />
      )}
      {pathname === "/administrar-usuarios/anadir-usuario" && <AñadirUsuario />}

      {pathname === "/profesores/dashboard-profesor" && <DashboardProfesores />}
      {pathname === "/otra-ruta" && <Typography>Esta es otra ruta</Typography>}


      {pathname === "/profesores/desarrollo-humano" && < Anual />}


      {pathname === "/profesores/formulario" && <Formulario />}

      {pathname === "/profesores/ciencias-basicas" && <Direccion />}
      {pathname === "/profesores/turismo-sustentable" && <Formacion />}
      {pathname === "/profesores/servicios-escolares" && <Vinculacion />}
      {pathname === "/profesores/departamento-investigacion" && <Proyecto />}

      <Typography>{pathname}</Typography>
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
