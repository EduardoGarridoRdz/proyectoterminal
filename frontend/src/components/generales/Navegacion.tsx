import React from "react";
import DashboardIcon from "@mui/icons-material/Dashboard";
import SchoolIcon from "@mui/icons-material/School";
import Person4Icon from "@mui/icons-material/Person4";
import SettingsIcon from "@mui/icons-material/Settings";
import GroupIcon from "@mui/icons-material/Group";

// Definimos el tipo para los elementos de navegación
type HeaderItem = {
  kind: "header";
  title: string;
};

type DividerItem = {
  kind: "divider";
};

type SingleItemHijo = {
  segment: string;
  title: string;
  icon?: React.ReactNode;
};

type SingleItemPadre = {
  segment: string;
  title: string;
  icon?: React.ReactNode;
  children: SingleItemHijo;
};

// Definimos el tipo para la navegación completa
type Navigation = HeaderItem | DividerItem | SingleItemHijo | SingleItemPadre;

// Función que genera y devuelve la navegación
const getNavigation = (): Navigation => {
  return [
    {
      kind: "header",
      title: "Menú principal",
    },
    {
      segment: "dashboard-general",
      title: "Dashboard General",
      icon: <DashboardIcon />,
    },
    {
      segment: "estudiantes",
      title: "Estudiantes",
      icon: <SchoolIcon />,
      children: [
        {
          segment: "dashboard-estudiantes",
          title: "Dashboard Estudiantes",
        },
        {
          segment: "servicios-escolares",
          title: "Servicios Escolares",
        },
        {
          segment: "practicas-profesionales",
          title: "Prácticas Profesionales",
        },
        {
          segment: "servicio-social",
          title: "Servicio Social",
        },
        {
          segment: "desarrollo-estudiantil",
          title: "Desarrollo Estudiantil",
        },
        {
          segment: "desarrollo-académico",
          title: "Desarrollo Académico",
        },
        {
          segment: "vinculacion-universitaria",
          title: "Vinculación Universitaria",
        },
      ],
    },

    // Profesores departamentos
    {
      segment: "profesores",
      title: "Profesores",
      icon: <Person4Icon />,

      children: [
        {
          segment: "dashboard-profesor",
          title: "Dashboard Profesores",
        },

        {
          segment: "desarrollo-humano",
          title: "Desarrollo Humano",
        },

        {
          segment: "ciencias-basicas",
          title: "Ciencias básicas de ingeniería",
        },

        {
          segment: "turismo-sustentable",
          title: "Turismo sustentable y gestión",
        },

        {
          segment: "servicicios-escolares",
          title: "Servicios escolares",
        },

        {
          segment: "tutorias",
          title: "Tutorías",
        },

        {
          segment: "desarrollo-académico",
          title: "Desarrollo académico",
        },
      
        {
          segment: "economia-negocios",
          title: "Economía y Negocios",
        },

      ],
    },

    {
      kind: "divider",
    },
    {
      kind: "header",
      title: "Configuraciones",
    },

    {
      segment: "administrar-usuarios",
      title: "Administrar Usuarios",
      icon: <GroupIcon />,
      children: [
        {
          segment: "añadir-usuario",
          title: "Añadir Usuario",
        },
        {
          segment: "eliminar-usuario",
          title: "Eliminar Ususario",
        },
      ],
    },
    {
      segment: "configuracion",
      title: "Configuración",
      icon: <SettingsIcon />,
      children: [
        {
          segment: "Editar cuenta",
          title: "Editar cuenta",
        },
      ],
    },
  ];
};

// Exportamos la función
export default getNavigation;
