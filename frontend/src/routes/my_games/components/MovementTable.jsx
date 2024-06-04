import React from 'react'
import StyledTable from '../../../components/StyledTable'

const MovementTable = ({movementData, selectedRow, setSelectedRow}) => {
    const columnHeaders = [
        {
            columnName: "Name",
            keyName: ["name"],
            sortby: true,
        },
        {
            columnName: "Players",
            keyName: ["n_players"],
            sortby: true,
        },
        {
            columnName: "Tables",
            keyName: ["n_tables"],
            sortby: true,
        },
        {
            columnName: "Rounds",
            keyName: ["n_rounds"],
            sortby: true,
        },
        {
            columnName: "Type",
            keyName: ["type"],
            sortby: true,
        },
    ];
    
    const ui = [];
    
    const settings = {
        limit: 6,
        minHeight: "16rem"
    }

  return (
    <StyledTable
        tableHeaders={columnHeaders}
        rawTableData={movementData}
        ui={ui}
        settings={settings}
        selectedRow = {selectedRow}
        setSelectedRow={setSelectedRow} 
    />
  )
}

export default MovementTable