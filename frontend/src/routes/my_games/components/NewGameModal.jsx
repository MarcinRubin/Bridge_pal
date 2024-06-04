import React from "react";
import {
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalFooter,
    ModalBody,
    ModalCloseButton,
    Button,
    VStack,
    HStack,
    Text,
    Input,
    Flex,
    Select,
} from "@chakra-ui/react";
import {
    NumberInput,
    NumberInputField,
    NumberInputStepper,
    NumberIncrementStepper,
    NumberDecrementStepper,
} from "@chakra-ui/react";
import MovementTable from "./MovementTable";
import { useState } from "react";

const NewGameModal = ({ isOpen, onClose, movementData }) => {
    const TYPES = ["IND", "PAIRS"];
    const SCORERS = ["CROSS-IMP", "IMP", "MAX"];
    
    const [selectedRow, setSelectedRow] = useState(null);

    const [filter, setFilter] = useState({
        playerNumber: 12,
        type: "IND",
    });

    const [newGameState, setNewGameState] = useState({
        name: "",
        movement: "",
        scorer: "CROSS_IMP",
        dealsNumber: 3,
    });
    

    const filteredMovementData = movementData?.filter(
        (item) =>
            item.n_players === Number(filter?.playerNumber) &&
            item.type === filter?.type
    );

    console.log(filteredMovementData);

    return (
        <Modal
            isOpen={isOpen}
            onClose={onClose}
            size="4xl"
            closeOnOverlayClick={false}
        >
            <ModalOverlay />
            <ModalContent>
                <ModalHeader>Create new game</ModalHeader>
                <ModalCloseButton />
                <ModalBody p={4} bgColor="gray.100">
                    <VStack gap={6}>
                        <VStack
                            bgColor="white"
                            w="100%"
                            rounded="xl"
                            p={4}
                            boxShadow="xl"
                        >
                            <VStack justifyContent="center" w="100%" p={4}>
                                <Text>Tournament name</Text>
                                <Input />
                            </VStack>
                            <HStack p={4} gap={2}>
                                <VStack justifyContent="center">
                                    <Text>Type</Text>
                                    <Select
                                        value={filter.type}
                                        onChange={(e) =>
                                            setFilter((prev) => ({
                                                ...prev,
                                                type: e.target.value,
                                            }))
                                        }
                                    >
                                        {TYPES.map((item, idx) => (
                                            <option key={idx} name={item}>
                                                {item}
                                            </option>
                                        ))}
                                    </Select>
                                </VStack>
                                <VStack justifyContent="center">
                                    <Text>Players</Text>
                                    <NumberInput
                                        value={filter.playerNumber}
                                        min={4}
                                        max={99}
                                        onChange={(valueString) =>
                                            setFilter((prev) => ({
                                                ...prev,
                                                playerNumber: valueString,
                                            }))
                                        }
                                    >
                                        <NumberInputField />
                                        <NumberInputStepper>
                                            <NumberIncrementStepper />
                                            <NumberDecrementStepper />
                                        </NumberInputStepper>
                                    </NumberInput>
                                </VStack>
                                <VStack justifyContent="center">
                                    <Text>Scorer</Text>
                                    <Select
                                        value={newGameState.scorer}
                                        onChange={(e) =>
                                            setNewGameState((prev) => ({
                                                ...prev,
                                                scorer: e.target.value,
                                            }))
                                        }
                                    >
                                        {SCORERS.map((item, idx) => (
                                            <option key={idx} name={item}>
                                                {item}
                                            </option>
                                        ))}
                                    </Select>
                                </VStack>
                                <VStack justifyContent="center">
                                    <Text>Deals in round</Text>
                                    <NumberInput
                                        value={newGameState.dealsNumber}
                                        min={1}
                                        max={10}
                                        onChange={(valueString) =>
                                            setNewGameState((prev) => ({
                                                ...prev,
                                                dealsNumber: valueString,
                                            }))
                                        }
                                    >
                                        <NumberInputField />
                                        <NumberInputStepper>
                                            <NumberIncrementStepper />
                                            <NumberDecrementStepper />
                                        </NumberInputStepper>
                                    </NumberInput>
                                </VStack>
                            </HStack>
                        </VStack>
                        <Flex
                            bgColor="white"
                            w="100%"
                            rounded="xl"
                            p={4}
                            boxShadow="xl"
                        >
                            <MovementTable
                                movementData={filteredMovementData}
                                selectedRow={selectedRow}
                                setSelectedRow={setSelectedRow}
                            />
                        </Flex>
                    </VStack>
                </ModalBody>

                <ModalFooter justifyContent="space-between">
                    <Button
                        colorScheme="gray"
                        variant="outline"
                        mr={3}
                        onClick={onClose}
                    >
                        Cancel
                    </Button>
                    <Button colorScheme="purple">Create</Button>
                </ModalFooter>
            </ModalContent>
        </Modal>
    );
};

export default NewGameModal;
