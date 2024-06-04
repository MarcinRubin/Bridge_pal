const STATEMAPPER = {
    normal: "desc",
    desc: "asc",
    asc: "normal",
};

export const tableReducer = (state, action) => {
    switch (action.type) {
        case "SELECT_ROW":
            return { ...state, selectedRow: action.data.selectedRow };

        case "SET_FILTER":
            const newFilters = state.filters.map((item) =>
                action.data.columnName === item.columnName
                    ? { ...item, ...action.data }
                    : item
            );
            const newSlice = {start: 0, end: state.slice.limit, limit: state.slice.limit}
            return { ...state, filters: newFilters, slice: newSlice };

        case "CLEAR_FILTERS_BUT":
            const newFilters2 = state.filters.map((item) =>
                action.data.columnName === item.columnName
                    ? item
                    : { ...item, value: "" }
            );
            return { ...state, filters: newFilters2 };

        case "CHANGE_SORT_STATE":
            const newSortState = state.sorts.map((item) =>
                action.data.columnName === item.columnName
                    ? { ...item, state: STATEMAPPER[item.state] }
                    : { ...item, state: "normal" }
            );
            return {...state, sorts: newSortState}

        case "SET_SLICE":
            return {...state, slice: action.data}

        default:
            return state;
    }
};
