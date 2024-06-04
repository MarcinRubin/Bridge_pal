import {
    Flex,
    Box,
    HStack,
    Link as ChakraLink,
} from "@chakra-ui/react";
import Logo from "./components/Logo";
import RightMenu from "./components/RightMenu";

const Header = ({}) => {

    return (
        <Flex
            flexDirection="row"
            bg="purple.700"
            color="white"
            h="3.5rem"
            px={8}
            py={4}
            justifyContent="space-between"
            top="0"
            zIndex="10"
            w="100%"
        >
        <Logo/>
        <RightMenu/>
        </Flex>
    );
};

export default Header;
