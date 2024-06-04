import React from "react";
import { Grid, GridItem, Flex, Heading, Text } from "@chakra-ui/react";
import { ViewIcon } from "@chakra-ui/icons";

const DealViever = ({dealsFilter, ...property}) => {

    if (!dealsFilter){
        return <Flex {...property} bgColor="white" aspectRatio="1/1" borderWidth={2} borderColor="purple.400"></Flex>
    }


    const colorMapper = {
        "A": {
            "NS": {
                borderColor: "green.700",
                borderWidth: 2,
                bgColor: "green.300"
            },
            "EW": {
                borderColor: "green.700",
                borderWidth: 2,
                bgColor: "green.300"
            }
        },
        "B": {
            "NS": {
                borderColor: "red.700",
                borderWidth: 2,
                bgColor: "red.300"
            },
            "EW": {
                borderColor: "red.700",
                borderWidth: 2,
                bgColor: "red.300"
            },
        },
        "N": {
            "NS": {
                borderColor: "red.700",
                borderWidth: 2,
                bgColor: "red.300"
            },
            "EW": {
                borderColor: "green.700",
                borderWidth: 2,
                bgColor: "green.300"
            }
        },
        "E": {
            "NS": {
                borderColor: "green.700",
                borderWidth: 2,
                bgColor: "green.300"
            },
            "EW": {
                borderColor: "red.700",
                borderWidth: 2,
                bgColor: "red.300"
            }
        }
    }

    const styles = {
        1: {
            name: <Text size='sm' fontWeight="medium">N</Text>,
            containerStyles: {
                pt: 3, 
                px: 1.5
            },
            elementStyles: {
                ...colorMapper[dealsFilter.vul]["NS"],
                borderRadius: dealsFilter.dealer === "N" ? "25%" : "100%"
            }
        },
        3: {
            name: <Text size='sm' fontWeight="medium">W</Text>,
            containerStyles: {
                py: 1.5, 
                pl: 3
            },
            elementStyles: {
                ...colorMapper[dealsFilter.vul]["EW"],
                borderRadius: dealsFilter.dealer === "W" ? "25%" : "100%"
            }
        },
        4: {
            name: <Heading size='md'>{dealsFilter.deal_number}</Heading>,
        },
        5: {
            name: <Text size='sm' fontWeight="medium">E</Text>,
            containerStyles: {
                py: 1.5, 
                pr: 3
            },
            elementStyles: {
                ...colorMapper[dealsFilter.vul]["EW"],
                borderRadius: dealsFilter.dealer === "E" ? "25%" : "100%"
            }
        },
        7: {
            name: <Text size='sm' fontWeight="medium">S</Text>,
            containerStyles: {
                px: 1.5, 
                pb: 3
            },
            elementStyles: {
                ...colorMapper[dealsFilter.vul]["NS"],
                borderRadius: dealsFilter.dealer === "S" ? "25%" : "100%"
            }
        },

    }
    
    return (
        <Flex {...property}>
            <Grid
                templateColumns="repeat(3, 1fr)"
                templateRows="repeat(3, 1fr)"
                gap={0}
                w="100%"
                bgColor="white"
                rounded='xl'
                boxShadow='xl'
                
            >
                {[...Array(9)].map((_, idx) => (
                    <GridItem key={idx} w="100%" aspectRatio="1/1" {...styles[idx]?.containerStyles}>
                        <Flex
                        w="100%"
                        h="100%"
                        alignItems="center"
                        justifyContent="center"
                        {...styles[idx]?.elementStyles}
                    >{styles[idx]?.name}</Flex>
                    </GridItem>
                ))}
            </Grid> 
        </Flex>
    );
};

export default DealViever;
