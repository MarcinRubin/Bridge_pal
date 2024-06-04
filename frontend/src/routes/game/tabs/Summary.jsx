import React from 'react'
import { Flex } from '@chakra-ui/react'
import { useState } from 'react'
import axios from 'axios'

const Summary = () => {

  const [counter, setCounter] = useState(0);
  const handleClick = () => {
    setCounter(prev => prev + 1);
    setCounter(prev => prev + 1);
    setCounter(prev => prev + 1);
  }

  const handleGetPerson = async () => {
    try{
      const response = await axios.get("https://randomuser.me/api/");
      const personData = await response.data;
      const {first, last} = personData.results[0].name;
      console.log(`You fetched data of the ${first} ${last}`);
    }
    catch(err){
      console.log("Error occured");
    }
  }

  return (
    <Flex bgColor="white">
      <p>{counter}</p>
      <button onClick = {handleClick}>Increase</button>
      <button onClick = {handleGetPerson}>Get Person</button>
    </Flex>
  )
}

export default Summary