import "./index.css";
import NavBar from "./components/NavBar";
import { Outlet } from "react-router-dom";
import { Stack } from "@mui/material";
import HomePage from "./pages/HomePage";

function App() {
  return (
    <Stack height="100%" sx={{ backgroundColor: "white" }}>
      <NavBar />
      <Outlet  />
    </Stack>
  );
}
export default App;
