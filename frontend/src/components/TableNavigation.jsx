import React from "react";
import { HStack, IconButton, Text } from "@chakra-ui/react";
import {
    ChevronLeftIcon,
    ChevronRightIcon,
    ArrowLeftIcon,
    ArrowRightIcon,
} from "@chakra-ui/icons";

const styles = {
    minW: "1.5rem",
    h: "1.5rem",
    bgColor: "white",
    borderColor: "purple.200",
    color: "gray.700",
    borderWidth: 2,
    _hover: {
        bgColor: "purple.50",
    },
};

const TableNavigation = ({ length, slice, tableStateSetter }) => {
    
    const handleIncrement = () => {
        const newSlice = {
            ...slice,
            start: slice.start + slice.limit,
            end: slice.end + slice.limit,
        };
        tableStateSetter({type: "SET_SLICE", data: newSlice});
    };

    const handleDecrement = () => {
        const newSlice = {
            ...slice,
            start: slice.start - slice.limit,
            end: slice.end - slice.limit,
        };
        tableStateSetter({type: "SET_SLICE", data: newSlice});
    };

    const handleToBegin = () => {
        const newSlice = {
            ...slice,
            start: 0,
            end: slice.limit,
        };
        tableStateSetter({type: "SET_SLICE", data: newSlice});
    }

    const handleToEnd = () => {
        const steps = Math.floor(length/slice.limit)
        const newSlice = {
            ...slice,
            start: steps * slice.limit,
            end: steps * slice.limit + slice.limit,
        };
        tableStateSetter({type: "SET_SLICE", data: newSlice});
    }

    return (
        <HStack>
            <Text fontSize="sm">
                {slice.start + 1}-{Math.min(slice.end, length)} of {length}
            </Text>
            <IconButton
                fontSize="0.5rem"
                onClick={handleToBegin}
                isDisabled={slice.start === 0 ? true : false}
                {...styles}
                icon={<ArrowLeftIcon />}
            />
            <IconButton
                fontSize="1rem"
                onClick={handleDecrement}
                isDisabled={slice.start === 0 ? true : false}
                {...styles}
                icon={<ChevronLeftIcon />}
            />
            <IconButton
                fontSize="1rem"
                onClick={handleIncrement}
                isDisabled={slice.start + slice.limit >= length ? true : false}
                {...styles}
                icon={<ChevronRightIcon />}
            />
            <IconButton
                fontSize="0.5rem"
                onClick={handleToEnd}
                isDisabled={slice.start + slice.limit >= length ? true : false}
                {...styles}
                icon={<ArrowRightIcon />}
            />
        </HStack>
    );
};

export default TableNavigation;
