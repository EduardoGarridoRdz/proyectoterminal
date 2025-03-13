import { AppProvider } from "@toolpad/core/AppProvider";
import { SignInPage, type AuthProvider } from "@toolpad/core/SignInPage";
import { useTheme } from "@mui/material/styles";
import logo from "./../../assets/logo.svg";
import { useNavigate } from "react-router-dom";

const providers = [{ id: "credentials", name: "Credentials" }];

const BRANDING = {
  logo: <img src={logo} alt="MUI logo" style={{ height: 80 }} />,
};

export default function LoginSistema() {
  const theme = useTheme();
  const navigate = useNavigate(); // Obtén la función de navegación

  const signIn: (provider: AuthProvider) => void = async (provider) => {
    const promise = new Promise<void>((resolve) => {
      setTimeout(() => {
        console.log(`Sign in with ${provider.id}`);
        resolve();
        navigate("/inicio"); // Redirige a la página de inicio después del inicio de sesión
      }, 500);
    });
    return promise;
  };

  return (
    <AppProvider branding={BRANDING} theme={theme}>
      <SignInPage
        signIn={signIn}
        providers={providers}
        slotProps={{
          emailField: { autoFocus: false, label: "Correo Electrónico" },
          passwordField: { label: "Contraseña" },
          submitButton: {
            variant: "contained",
            fullWidth: true,
            children: "Iniciar sesión",
          },
          form: { noValidate: true },
        }}
        localeText={{
          signInTitle: "Iniciar Sesión",
          signInSubtitle: "",
          signInRememberMe: "Recordarme",
        }}
      ></SignInPage>
    </AppProvider>
  );
}
