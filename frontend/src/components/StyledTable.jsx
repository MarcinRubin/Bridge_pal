import React from "react";
import {
    Table,
    Thead,
    Tbody,
    Tr,
    Th,
    Td,
    TableContainer,
    VStack,
    HStack,
    Select,
} from "@chakra-ui/react";
import { ChevronDownIcon, ChevronUpIcon, DeleteIcon} from "@chakra-ui/icons";
import { IconButton } from "@chakra-ui/react";
import TableNavigation from "./TableNavigation";

const ICONMAPPER = {
    asc: <ChevronDownIcon />,
    desc: <ChevronUpIcon />,
};

const StyledTable = ({ tableState, tableStateSetter, tableData}) => {

    if (!tableState?.columnHeaders){
        return <></>
    }    
    
    const sortBy = tableState.sorts.find(item => ["asc", "desc"].includes(item.state));
    const possibleSortBy = tableState.sorts.map(item => item.columnName);

    //wrappers and special fields defined below
    const handleBlur = (e, record, attribute) => {
        attribute.callback({ ...record, [attribute.keyName]: e.target.value });
        e.currentTarget.value = "";
    };

    const renderSpecialElement = (record, attribute) => {
        const element = React.cloneElement(attribute.element, {
            onKeyDown: (e) =>
                e.key === "Enter" ? e.currentTarget.blur() : null,
            onBlur: (e) => handleBlur(e, record, attribute),
        });
        return element;
    };

    const renderTableElement = (attribute, record) => {
        const value = attribute.keyName.reduce(
            (accum, item) => (accum = accum[item]),
            record
        );
        if (attribute.wrapper) {
            const element = React.cloneElement(attribute.wrapper, {
                onClick: attribute.callback
                    ? () => attribute.callback(record)
                    : null,
                children: value,
            });
            return element;
        }
        if (attribute.element) {
            return renderSpecialElement(record, attribute);
        }
        return value;
    };

    // //filter functionality
    const handlefilterChange = (e) => {
        tableStateSetter({type: "SET_FILTER", data: {columnName: e.target.name, value: e.target.value}});
        tableStateSetter({type: "SELECT_ROW", data: {selectedRow: null}});
    };

    const handleResetFilters = () => {
        tableStateSetter({type: "CLEAR_FILTERS_BUT", data: {columnName: "Deal"}});
        tableStateSetter({type: "SELECT_ROW", data: {selectedRow: null}});
        setSlice(prev => ({
            start: 0,
            end: tableState.settings.limit,
            limit: tableState.settings.limit,
    }));
    }

    // //Sorting functionality below
    const changeSortState = (e) => {
        const name = e.currentTarget.getAttribute("name");
        tableStateSetter({type: "CHANGE_SORT_STATE", data: {columnName: name}});
    };

    const sortFunction = (a, b) => {     
        const a_value = sortBy.sortPath.reduce(
            (accum, item) => (accum = accum[item]),
            a
        );
        const b_value = sortBy.sortPath.reduce(
            (accum, item) => (accum = accum[item]),
            b
        );

        if (sortBy.state === "asc") {
            return a_value - b_value;
        }
        return b_value - a_value;
    };

    let tableDataToShow = tableData.filter((record) =>
        tableState.filters.every((filter) =>
            filter.value === ""
                ? true
                : filter.filterPath.reduce(
                      (accum, item) => (accum = accum[item]),
                      record
                  ) === Number(filter.value)
        )
    );
    sortBy && tableDataToShow.sort(sortFunction);
    const length = tableDataToShow.length;
    tableDataToShow = tableDataToShow.slice(tableState.slice.start, tableState.slice.end);

    return (
        <VStack w="100%" alignItems="flex-start" gap={2}>
            <HStack gap={3} w="100%" justifyContent="space-between">
                <HStack gap={3}>
                   {tableState.ui ? tableState.ui() : null}
                    <HStack>
                        {/* <DragHandleIcon /> */}
                        {tableState.filters.map((item, idx) => (
                            item.options ? 
                            <Select
                                key={idx}
                                size="sm"
                                placeholder={item.columnName}
                                name={item.columnName}
                                w="6rem"
                                value={item.value}
                                onChange={handlefilterChange}
                            >
                                {item.options.map((option, option_idx) => (
                                    <option key={option_idx}>{option}</option>
                                ))}
                            </Select>: null
                        ))}
                        {tableState.filters.length ? <IconButton
                            icon={<DeleteIcon/>}
                            size="sm"
                            onClick={handleResetFilters}
                        /> : null}
                    </HStack>
                </HStack>
                <HStack>
                    <TableNavigation
                        length={length}
                        slice={tableState.slice}
                        tableStateSetter={tableStateSetter}
                    />
                </HStack>
            </HStack>
            <TableContainer w="100%" h={tableState.settings?.minHeight ? tableState.settings?.minHeight : null}>
                <Table variant="simple" size="sm">
                    <Thead bgColor="purple.50">
                        <Tr>
                            {tableState.columnHeaders.map((item, idx) => (
                                <Th
                                    key={idx}
                                    name={item.columnName}
                                    onClick={
                                        possibleSortBy.includes(item.columnName) ? changeSortState : null
                                    }
                                    cursor={possibleSortBy.includes(item.columnName) ? "pointer" : "auto"}
                                    pr={
                                        possibleSortBy.includes(item.columnName)
                                            ? 1
                                            : 4
                                    }
                                >
                                    {item.columnName}
                                    {sortBy && sortBy.columnName === item.columnName
                                        ? ICONMAPPER[sortBy.state]
                                        : null}
                                </Th>
                            ))}
                        </Tr>
                    </Thead>
                    <Tbody>
                        {tableDataToShow.map((record, nRow) => (
                            <Tr
                                key={nRow}
                                _hover={
                                    tableState.selectedRow?.id !== record.id
                                        ? { bgColor: "gray.50" }
                                        : {}
                                }
                                bgColor={
                                    tableState.selectedRow?.id === record.id
                                        ? "purple.50"
                                        : "white"
                                }
                                onClick={(prev) => tableStateSetter({type: "SELECT_ROW", data: {selectedRow: record}})}
                            >
                                {tableState.columnHeaders.map((attribute, nCol) => (
                                    <Td key={nCol}>
                                        {renderTableElement(attribute, record)}
                                    </Td>
                                ))}
                            </Tr>
                        ))}
                    </Tbody>
                </Table>
            </TableContainer>
        </VStack>
    );
};

export default StyledTable;
