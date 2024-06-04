import React from "react";
import StyledTable from "../../../../components/StyledTable";
import { Input, HStack, Button } from "@chakra-ui/react";
import ContractField from "../../../../components/ContractField";
import PlayerField from "../../../../components/PlayerField";
import { useReducer, useEffect } from "react";
import { tableReducer } from "../../../../components/tableReducer";

const ScoreTable = ({
    tableData,
    playersData,
    gameData,
    callbacks,
    dealsFilter,
}) => {
    const columnHeaders = [
        {
            columnName: "Deal",
            keyName: ["deal"],
        },
        {
            columnName: "Round",
            keyName: ["pairing", "round_number"],
        },
        {
            columnName: "Table",
            keyName: ["pairing", "table"],
        },
        {
            columnName: gameData.type === "ind" ? "N/S" : "NS",
            keyName: ["pairing"],
            asProps: true,
            wrapper: (
                <PlayerField
                    pairing={["n", "s"]}
                    type={gameData?.type}
                    players={playersData}
                />
            ),
            callback: callbacks.handlePlayerNS,
        },
        {
            columnName: gameData.type === "ind" ? "E/W" : "EW",
            keyName: ["pairing"],
            asProps: true,
            wrapper: (
                <PlayerField
                    pairing={["e", "w"]}
                    type={gameData?.type}
                    players={playersData}
                />
            ),
            callback: callbacks.handlePlayerEW,
        },
        {
            columnName: "Contract",
            keyName: ["contract"],
            wrapper: <ContractField />,
        },
        {
            columnName: "By",
            keyName: ["by"],
        },
        {
            columnName: "Score",
            keyName: ["score"],
        },
        {
            columnName: "Result",
            keyName: ["result"],
        },
        {
            columnName: "Score Input",
            keyName: ["score_input"],
            element: <Input size="sm" w="10rem" />,
            callback: callbacks.handleScoreInput,
        },
    ];

    const ui = () => {
        const elements = [
            {
                name: "Add",
                style: {
                    bgColor: "green.200",
                    size: "sm",
                },
                callbackfn: callbacks.handleAdd,
                isDetail: false,
            },
            {
                name: "Remove",
                style: {
                    bgColor: "red.200",
                    size: "sm",
                },
                callbackfn: callbacks.handleRemove,
                isDetail: true,
            },
        ];
        return (
            <HStack>
                {elements.map((item, idx) => (
                    <Button key={idx} {...item.style} onClick={() => item.callbackfn()}>{item.name}</Button>
                ))}
            </HStack>
        )
    }

    const [tableState, tableStateSetter] = useReducer(tableReducer, {
        selectedRow: null,
        columnHeaders: columnHeaders,
        settings: {
            limit: 5,
        },
        filters: [
            {
                columnName: "Deal",
                filterPath: ["deal"],
                value: "",
            },
            {
                columnName: "Round",
                filterPath: ["pairing", "round_number"],
                value: "",
                options: [...Array(gameData.n_rounds)].map((_, idx) => idx + 1),
            },
            {
                columnName: "Table",
                filterPath: ["pairing", "table"],
                value: "",
                options: [...Array(gameData.n_tables)].map((_, idx) => idx + 1),
            },
        ],
        sorts: [
            {
                columnName: "Deal",
                sortPath: ["deal"],
                state: "normal",
            },
            {
                columnName: "Round",
                sortPath: ["pairing", "round_number"],
                state: "normal",
            },
            {
                columnName: "Table",
                sortPath: ["pairing", "table"],
                state: "normal",
            },
        ],
        slice: {
            start: 0,
            end: 5,
            limit: 5
        },
        ui: ui
    });

    
        

    useEffect(() => {
        tableStateSetter({
            type: "SET_FILTER",
            data: {
                columnName: "Deal",
                value: dealsFilter?.deal_number ? dealsFilter.deal_number : "",
            },
        });
    }, [dealsFilter]);

    return (
        <StyledTable
            tableState={tableState}
            tableStateSetter={tableStateSetter}
            tableData={tableData}
        />
    );
};

export default ScoreTable;
