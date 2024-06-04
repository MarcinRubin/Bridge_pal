import React from "react";
import { IconButton } from "@chakra-ui/react";
import { HStack, Heading } from "@chakra-ui/react";
import { BellIcon, TriangleDownIcon } from "@chakra-ui/icons";
import { Avatar } from "@chakra-ui/react";

const RightMenu = () => {
    return (
        <HStack gap={2}>
            <IconButton
                aria-label="Search database"
                bgColor="purple.700"
                color="white"
                _hover={{ backgroundColor: "purple.600" }}
                icon={<BellIcon boxSize={5} />}
            />
            <Avatar bg="purple.700" borderWidth={2} size="sm" />
            <Heading size="sm">Hello, Marcin!</Heading>
            <TriangleDownIcon />
        </HStack>
    );
};

export default RightMenu;
