import React from "react";
import { HStack, Flex } from "@chakra-ui/react";
import DealButton from "../../../../components/DealButton";

const DealNavBar = ({ dealsData, dealsFilter, setDealsFilter}) => {
    const data = [null, ...dealsData];

    return (
        <Flex flexDir="row">
            <HStack
                gap={0}
                p={4}
                bgColor="white"
                rounded="xl"
                boxShadow="xl"
                wrap="wrap"
                justifyContent="center"
            >
                {data.map((item, idx) => (
                    <DealButton
                        onClick={() => setDealsFilter(prev => item)}
                        size="sm"
                        px={6}
                        bgColor={
                            item && item.deal_number === dealsFilter?.deal_number ? "purple.100" : "white"
                        }
                        key={idx}
                    >
                        {item ? item.deal_number : "all"}
                    </DealButton>
                ))}
            </HStack>
        </Flex>
    );
};

export default DealNavBar;
