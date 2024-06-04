import React from "react";
import { Link as ReactRouterLink } from "react-router-dom";
import { Link as ChakraLink, Text, HStack } from "@chakra-ui/react";

const stylesProps = {
    color: "purple.200",
    w: "100%",
    p: 4,
    rounded: "xl",
    _hover: {
        color: "white",
        bgColor: "purple.600"
    }
}

const MenuItem = ({icon, children, link}) => {
    return (
        <ChakraLink as={ReactRouterLink} to={link} {...stylesProps}>
            <HStack gap={4}>
                {icon}
                <Text>{children}</Text>
            </HStack>
        </ChakraLink>
    );
};

export default MenuItem;
