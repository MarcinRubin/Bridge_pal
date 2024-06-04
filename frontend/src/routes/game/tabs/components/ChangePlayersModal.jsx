import {
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalFooter,
    ModalBody,
    ModalCloseButton,
    Button,
    Select,
} from "@chakra-ui/react";

const ChangePlayersModal = ({ isOpen, onClose }) => {
    return (
        <Modal isOpen={isOpen} onClose={onClose}>
            <ModalOverlay />
            <ModalContent>
                <ModalHeader>ChangePlayer</ModalHeader>
                <ModalCloseButton />
                <ModalBody>
                    LA
                </ModalBody>

                <ModalFooter>
                    <Button colorScheme="blue" mr={3} onClick={onClose}>
                        Close
                    </Button>
                    <Button variant="ghost">Submit</Button>
                </ModalFooter>
            </ModalContent>
        </Modal>
    );
};

export default ChangePlayersModal;
