import React, { useReducer } from 'react'
import { userReducer } from './UserReducer.js'


export const UserContext = React.createContext({
    user: {
        authenticated: false,
        username: '',
        user_id: null
    }
});

const UserContextProvider = props => {
    const [user, dispatch] = useReducer(userReducer, []);

    return (
        <UserContext.Provider value={{ user, dispatch }}>
            {props.children}
        </UserContext.Provider>
    );
};


export default UserContextProvider;
