import React from "react";
import StyledTable from "../../../components/StyledTable";
import { useReducer } from "react";
import { tableReducer } from "../../../components/tableReducer";
import { HStack, Button } from "@chakra-ui/react";

const GamesTable = ({ gamesData, callbacks }) => {
    const columnHeaders = [
        {
            columnName: "Name",
            keyName: ["name"],
        },
        {
            columnName: "Players",
            keyName: ["movement", "n_players"],
        },
        {
            columnName: "Boards",
            keyName: ["movement", "n_rounds"],
        },
        {
            columnName: "Tables",
            keyName: ["movement", "n_tables"],
        },
        {
            columnName: "Rounds",
            keyName: ["movement", "n_rounds"],
        },
        {
            columnName: "Scorer",
            keyName: ["scorer"],
        },
        {
            columnName: "Status",
            keyName: ["status"],
        },
        {
            columnName: "Type",
            keyName: ["movement", "type"],
        },
        {
            columnName: "Data",
            keyName: ["date"],
        },
    ];

    const ui = () => {
        const elements = [
            {
                name: "Add",
                style: {
                    bgColor: "green.200",
                    size: "md",
                },
                callbackfn: callbacks.handleAdd,
                isDetail: false,
            },
            {
                name: "Remove",
                style: {
                    bgColor: "red.200",
                    size: "md",
                },
                callbackfn: callbacks.handleRemove,
                isDetail: true,
            },
            {
                name: "Load",
                style: {
                    bgColor: "red.200",
                    size: "md",
                },
                callbackfn: callbacks.handleLoad,
                isDetail: true,
            },
        ];

        return (
            <HStack>
                {elements.map((item, idx) => (
                    <Button
                        key={idx}
                        {...item.style}
                        onClick={() => item.callbackfn()}
                    >
                        {item.name}
                    </Button>
                ))}
            </HStack>
        );
    };

    const [tableState, tableStateSetter] = useReducer(tableReducer, {
        selectedRow: null,
        columnHeaders: columnHeaders,
        settings: {
            limit: 5,
        },
        filters: [],
        sorts: [],
        slice: {
            start: 0,
            end: 5,
            limit: 5
        },
        ui: ui
    });

    return (
        <StyledTable
            tableState={tableState} 
            tableStateSetter={tableStateSetter} 
            tableData={gamesData}
        />
    );
};

export default GamesTable;
