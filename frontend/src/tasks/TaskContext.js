import React, { useReducer } from 'react'
import { taskReducer } from './TaskReducer.js'


export const TaskContext = React.createContext();

const TaskContextProvider = props => {
    const [tasks, dispatch] = useReducer(taskReducer, []);

    return (
        <TaskContext.Provider value={{ tasks, dispatch }}>
            {props.children}
        </TaskContext.Provider>
    );
};


export default TaskContextProvider;
