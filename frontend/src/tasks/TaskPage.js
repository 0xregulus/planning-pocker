import React from 'react'
import TaskList from './TaskList.js'
import TaskForm from './TaskForm.js'


const TaskPage = () => {

  return (
        <div className="columns">
            <aside className="column col-4">
                <TaskForm/>
            </aside>

            <TaskList/>

        </div>
 );
}

export default TaskPage;
