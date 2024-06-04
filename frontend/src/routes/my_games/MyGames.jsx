import React from "react";
import { Box, VStack, Heading, Flex } from "@chakra-ui/react";
import { useLoaderData } from "react-router-dom";
import { useState } from "react";
import { client } from "../../axiosClient";
import GamesTable from "./components/GamesTable";
import { useDisclosure } from "@chakra-ui/react";
import NewGameModal from "./components/NewGameModal";

export async function loader() {
    try {
        const response = await client.get("games/");
        const gamesData = await response.data;
        return gamesData;
    } catch (err) {
        console.log("ERROR OCCURED");
    }
}

const myGames = () => {
    const [gamesData, setGamesData] = useState(useLoaderData());
    const {isOpen, onOpen, onClose} = useDisclosure();
    const [movementData, setMovementData] = useState(null);
    const [selectedRow, setSelectedRow] = useState(null);

    const loadMovementData = async () => {
        try {
            const response = await client.get("movements/");
            const movementData = await response.data;
            return movementData;
        } catch (err) {
            console.log("ERROR OCCURED");
        }
    }

    const handleAdd = async () =>{
        const movementData = await loadMovementData();
        setMovementData(prev => movementData);
        onOpen();
    }

    const handleRemove = () =>{
        console.log("handle remove")
    }

    const handleLoad = () =>{
        console.log("handle load")
    }

    const callbacks = {
        handleAdd: handleAdd,
        handleRemove: handleRemove,
        handleLoad: handleLoad
    }

    return (
        <>
        <NewGameModal isOpen={isOpen} onClose={onClose} movementData={movementData}/>
        <VStack gap={4} borderWidth={1} borderColor="red" w="100%" px={8} bgColor="gray.100">
            <Box w="100%" mt={4}>
                <Heading size="md" >
                    My Games
                </Heading>
            </Box>
            <Flex bgColor="white" p={4} rounded="xl" boxShadow="xl" minW="100%">
            <GamesTable
                gamesData = {gamesData}
                callbacks={callbacks}
                selectedRow={selectedRow}
                setSelectedRow={setSelectedRow}
            />
            </Flex>

        </VStack>
        </>
    );
};

export default myGames;
