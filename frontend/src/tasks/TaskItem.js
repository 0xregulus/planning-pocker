import React from 'react'
import { Link } from 'react-router-dom'


const TaskItem = (props) => {
    return (
        <>
            <div className="tile p-2">
                <div className="tile-content">
                        <p className="tile-title text-bold">
                            <Link to={{
                                pathname: `/polls/${props.task.token}`
                            }}>#{ props.task.token }</Link> - { props.task.name } -
                            Score: <span className="label label-rounded label-primary">{ props.task.score }</span>
                          </p>
                      <p className="tile-subtitle">
                        { props.task.description }
                        <span className="float-right"><i>{ props.task.updated }</i></span>
                      </p>
                  </div>
            </div>
        </>
    )
}

export default TaskItem;
