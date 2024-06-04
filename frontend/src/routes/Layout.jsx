import { Outlet } from "react-router-dom";
import { Container, HStack, Flex } from "@chakra-ui/react";
import Header from "./header/Header";
import Navigation from "./navigation/Navigation";

function Layout() {
    return (
        <Flex
            minW="100%"
            display="flex"
            flexDirection="column"
            alignItems="stretch"
            minH="100vh"
            gap={0}
            p={0}
            m={0}
        >
            <Header />
            <Flex
                minW="100%"
                flex="1"
                flexDirection="row"
                gap={0}
                p={0}
                m={0}
            >
                <Navigation />
                <Outlet />
            </Flex>
        </Flex>
    );
}

export default Layout;
