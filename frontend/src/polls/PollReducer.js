export const pollReducer = (state, action) => {
    switch (action.type) {
        case 'SET_VOTES':
            return action.payload;
        case 'ADD_VOTE':
            const index = state.findIndex(vote => vote.username === action.payload.username);
            if (index === -1) {
                state.push(action.payload);
            } else {
                state[index] = action.payload;
            }
            return state
        default:
            return state;
    }
};
