import React, { useEffect, useContext } from 'react'
import TaskEmptyList from './TaskEmptyList.js'
import TaskItem from './TaskItem.js'
import { TaskContext } from './TaskContext'
import API from '../Api.js'


const TasksList = () => {
  const { tasks, dispatch } = useContext(TaskContext)

  useEffect(() => {
        API.fetchTaskList().then(
            data => {
                dispatch({
                    type: 'SET_TASKS',
                    payload: data
                })
            }
        ).catch(
            err => {
                console.log(err);
            }
        )
  }, []);

  return (
    <main className="column">

        <section id="tasks">
            <div className="panel">
                <div className="panel-header">
                    <div className="panel-title h6">Tasks</div>
                </div>
                <div className="panel-body p-2">
                    {
                        tasks.length > 0
                            ? tasks.map(task => {return <TaskItem task={task} key={task.token}/>})
                            : <TaskEmptyList/>
                    }
                </div>
            </div>

        </section>

    </main>
 );
}

export default TasksList;
