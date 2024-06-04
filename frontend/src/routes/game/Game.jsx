import React from "react";
import { Flex, Box } from "@chakra-ui/react";
import { Tabs, TabList, TabPanels, Tab, TabPanel } from "@chakra-ui/react";
import Summary from "./tabs/Summary";
import Scores from "./tabs/Scores";
import { useLoaderData } from "react-router-dom";
import { client } from "../../axiosClient";
import { useReducer } from "react";
import { gameReducer } from "./gameReducer";

export async function loader() {
    try {
        const response = await client.get("games/1/load_game/");
        const tableData = await response.data;
        return tableData;
    } catch (err) {
        console.log("ERROR OCCURED");
    }
}

const Game = () => {

    const [gameData, dispatch] = useReducer(gameReducer, useLoaderData());

    const gameTabs = [
        {
            tabName: "Summary",
            tabElement: <Summary />,
        },
        {
            tabName: "Score System",
            tabElement: <Summary />,
        },
        {
            tabName: "Players",
            tabElement: <Summary />,
        },
        {
            tabName: "Scores",
            tabElement: (
                <Scores
                    tableData = {gameData?.scores}
                    gameData = {gameData?.movement}
                    dealsData = {gameData?.deals}
                    playersData = {gameData?.players}
                    dispatch = {dispatch}
                />
            ),
        },
        {
            tabName: "Results",
            tabElement: <Summary />,
        },
        {
            tabName: "Penalties",
            tabElement: <Summary />,
        },
        {
            tabName: "Reports",
            tabElement: <Summary />,
        },
    ];
    return (
        <Flex
            w="100%"
            flexDirection="column"
            gap={0}
            p={0}
            m={0}
            justifyContent="flex-start"
            bgColor="gray.200"
        >
            <Tabs colorScheme="purple" size="sm" isFitted>
                <TabList bgColor="white" py={1} boxShadow="xl" px={6}>
                    {gameTabs.map((item, idx) => (
                        <Tab key={idx}>{item.tabName}</Tab>
                    ))}
                </TabList>
                <TabPanels p={4}>
                    {gameTabs.map((item, idx) => (
                        <TabPanel key={idx}>{item.tabElement}</TabPanel>
                    ))}
                </TabPanels>
            </Tabs>
        </Flex>
    );
};

export default Game;
