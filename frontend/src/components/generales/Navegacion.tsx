import React from "react";
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
          segment: "idiomas",
          title: "Idiomas",
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
          segment: "formulario",
          title: "Recursos Humanos",
        },


        {
          segment: "ciencias-basicas",
          title: "Ciencias Básicas de Ingeniería",
        },

        {
          segment: "economia-negocios",
          title: "Economía y Negocios",
        },

        
        {
          segment: "turismo-sustentable",
          title: "Turismo Sustentable, Gastronomía y Hotelería",
        },


        {
          segment: "desarrollo-humano",
          title: "Desarrollo Humano",
        },




        {
          segment: "desarrollo-academico",
          title: "Desarrollo Académico",
        },



        {
          segment: "departamento-investigacion",
          title: "Departamento de Investigacion",
        },


        {
          segment: "tutorias",
          title: "Tutorías",
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
          segment: "anadir-usuario",
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
