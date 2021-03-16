import React, { useReducer } from 'react'
import { pollReducer } from './PollReducer.js'


export const PollContext = React.createContext();

const PollContextProvider = props => {
    const [votes, dispatch] = useReducer(pollReducer, []);

    return (
        <PollContext.Provider value={{ votes, dispatch }}>
            {props.children}
        </PollContext.Provider>
    );
};


export default PollContextProvider;
