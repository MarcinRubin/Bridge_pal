import React from 'react'
import { Flex, Button } from '@chakra-ui/react'

const styles = {
    px: 8,
    bgColor: "white",

    _hover: {
        bgColor: "purple.100",
        borderColor: "purple.400"
    },
    borderRadius: 0,
    borderTopRightRadius: "12%",
    borderTopLeftRadius: "12%",
    borderBottomWidth: 2,
    borderColor: "purple.200"

    
}

const DealButton = ({children, ...props}) => {
  return (
    <Button {...styles} {...props}>{children}</Button>
  )
}

export default DealButton