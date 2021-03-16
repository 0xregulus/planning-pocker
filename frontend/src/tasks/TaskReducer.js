export const taskReducer = (state, action) => {
    switch (action.type) {
        case 'SET_TASKS':
            return action.payload;
        case 'ADD_TASK':
            return [
                ...state,
                action.paylod
            ];
        default:
            return state;
    }
};
