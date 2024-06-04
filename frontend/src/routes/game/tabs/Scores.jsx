import React from "react";
import { HStack, Flex, VStack } from "@chakra-ui/react";
import DealViever from "./components/DealViever";
import DealNavBar from "./components/DealNavBar";
import { useState } from "react";
import ScoreTable from "./components/ScoreTable";
import { client } from "../../../axiosClient";

const Scores = ({ tableData, gameData, dealsData, playersData, dispatch }) => {
    
    const [dealsFilter, setDealsFilter] = useState(null);

    const handleScoreInput = async (data) => {
        if (!data.score_input) return;
        try {
            const response = await client.post(
                `/scores/${data.id}/score_update/`,
                {
                    score: data.score_input,
                }
            );
            const updatedScores = await response.data;
            dispatch({ type: "SCORE_INPUT", updatedScores: updatedScores });
        } catch (err) {
            console.log("ERROR OCCURED");
        }
    };
    
    const handlePlayerNS = (record) => {
        console.log("HANDLE PLAYER NS");
        console.log(record);
    };

    const handlePlayerEW = (record) => {
        console.log("HANDLE PLAYER EW");
        console.log(record);
    };

    const handleAdd = () => {
        console.log("add");
    };

    const handleRemove = () => {
        console.log("remove");
    }

    const callbacks = {
        handleAdd: handleAdd,
        handleRemove: handleRemove,
        handlePlayerNS: handlePlayerNS,
        handlePlayerEW: handlePlayerEW,
        handleScoreInput: handleScoreInput,
    };

    return (
        <>
            <VStack gap={6}>
                <HStack w="100%" gap={6}>
                    <DealViever dealsFilter={dealsFilter} minW="110px" />
                    <DealNavBar
                        dealsData={dealsData}
                        dealsFilter={dealsFilter}
                        setDealsFilter={setDealsFilter}
                    />
                </HStack>
                <Flex
                    bgColor="white"
                    p={4}
                    rounded="xl"
                    boxShadow="xl"
                    minW="100%"
                >
                    <ScoreTable
                        tableData={tableData}
                        playersData={playersData}
                        gameData={gameData}
                        callbacks={callbacks}
                        dealsFilter={dealsFilter}
                    />
                </Flex>
            </VStack>
        </>
    );
};

export default Scores;
