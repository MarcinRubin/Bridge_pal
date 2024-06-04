import React from "react";
import ReactDOM from "react-dom/client";
import { ChakraProvider } from "@chakra-ui/react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Layout from "./routes/Layout.jsx";
import ErrorPage from "./routes/ErrorPage.jsx";
import Game, { loader as GameLoader } from "./routes/game/Game.jsx";
import MyGames, {loader as MyGamesLoader} from "./routes/my_games/MyGames.jsx";

const router = createBrowserRouter([
    {
        path: "/",
        element: <Layout />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: "/game",
                element: <Game />,
                loader: GameLoader
            },
            {
                path: "/my_games",
                element: <MyGames/>,
                loader: MyGamesLoader
            }
        ],
    },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
    <React.StrictMode>
        <ChakraProvider>
            <RouterProvider router={router} />
        </ChakraProvider>
    </React.StrictMode>
);
