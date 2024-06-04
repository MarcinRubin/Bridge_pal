export const gameReducer = (state, action) => {
    switch (action.type) {
        case "TEST":
            console.log("test");
            console.log(action.dane);
            return state
        case "SCORE_INPUT":
            const dataIds = action.updatedScores.map(item => item.id);
            const scores = state.scores.map(item => dataIds.includes(item.id) ? action.updatedScores.find(item2 => item2.id === item.id) : item);
            return {...state, scores: scores}
        default:
            return state;
    }
};
