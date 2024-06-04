import React from 'react'
import logo from './logo.svg'
import { Heading, HStack, Box, Image, Link as ChakraLink } from '@chakra-ui/react'
import { Link as ReactRouterLink } from "react-router-dom";


const Logo = () => {
  return (
    <HStack>
      <ChakraLink as={ReactRouterLink} to="/" boxSize="50px">
        <Image src={logo} alt="LOGO"/>
      </ChakraLink>
        <Heading size='md' w='4rem'>
            Bridge Pal
        </Heading>
    </HStack>
  )
}

export default Logo