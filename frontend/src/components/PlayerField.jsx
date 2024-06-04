import React from "react";
import { Text } from "@chakra-ui/react";
import { Tooltip } from "@chakra-ui/react";
import { useDisclosure } from "@chakra-ui/react";
import ChangePlayersModal from "../routes/game/tabs/components/ChangePlayersModal";


const PlayerField = ({ pairing, type, players, onClick, children }) => {
  const { isOpen, onOpen, onClose } = useDisclosure();
        const playerNE = players.find(item => item.id === children[pairing[0]])?.name;
        const playerSW = players.find(item => item.id === children[pairing[1]])?.name;
        return (

          <>
          <ChangePlayersModal isOpen={isOpen} onClose={onClose}/>
            <Tooltip
                label={`${playerNE}/${playerSW}`}>
                <Text color="black" onClick={onOpen} cursor="pointer">
                  {type === "pairs" ? 
                    children[pairing[0]] :
                    children[pairing[0]] + "/" + children[pairing[1]]
                  }
                </Text>
            </Tooltip>
            </>
        );
};

export default PlayerField;
