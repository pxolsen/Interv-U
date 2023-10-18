import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import QuestionsPage from "./pages/QuestionsPage";
import AnswersPage from "./pages/AnswersPage";
import ProfilePage from "./pages/ProfilePage";

const router = createBrowserRouter([
    {
      path: "/",
      element: <App />,
      children: [
        {
          index: true,
          element: <HomePage />,
        },
        {
          path: "/questions",
          element: <QuestionsPage />,
        },
        {
          path: "/answers",
          element: <AnswersPage />
        },
        {
          path: "/profile",
          element: <ProfilePage />
        }
      ],
    },
  ]);
  
  export default router;
  