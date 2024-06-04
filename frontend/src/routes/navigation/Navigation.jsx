import React from 'react'
import { VStack, Flex } from '@chakra-ui/react'
import MenuItem from './components/MenuItem'
import { ArrowRightIcon } from "@chakra-ui/icons";

const navigationItems = [
  {
    name: "My Games",
    icon: <ArrowRightIcon/>,
    link: "/game/"
  },{
    name: "Movements",
    icon: <ArrowRightIcon/>,
    link: "/my_games"
  },{
    name: "Players",
    icon: <ArrowRightIcon/>,
    link: "/"
  },
  {
    name: "Deals",
    icon: <ArrowRightIcon/>,
    link: "/"
  },
  {
    name: "Settings",
    icon: <ArrowRightIcon/>,
    link: "/"
  }
]

const Navigation = () => {
  return (
    <Flex flex="1">
    <VStack bgColor="purple.700" w="200px" pt={6} h="100%">
      {navigationItems.map((item, idx) => (
        <MenuItem key = {idx} icon={item.icon} link={item.link}>{item.name}</MenuItem>
      ))}
    </VStack>
    </Flex>
  )
}

export default Navigation