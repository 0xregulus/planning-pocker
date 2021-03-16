export const userReducer = (state, action) => {
    switch (action.type) {
        case 'SET_USER':
            return {
                authenticated: true,
                username: action.payload.username,
                user_id: action.payload.id
            };
        case 'REMOVE_USER':
            return {};
        default:
            return state;
    }
};
