import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginSistema from "./components/generales/LoginSistema" // Página de login
import PaginaInicio from "./components/generales/PaginaInicio"; // Página de inicio

function AppRouter() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginSistema />} />
        <Route path="/inicio" element={<PaginaInicio />} />
      </Routes>
    </Router>
  );
}

export default AppRouter;
