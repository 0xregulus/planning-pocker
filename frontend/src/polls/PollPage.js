import React, { useContext } from 'react'
import VoteList from './VoteList.js'
import VoteForm from './VoteForm.js'
import { TaskContext } from '../tasks/TaskContext'
import useSocket from '../WebSocket.js'


const PollPage = (props) => {

    const { tasks } = useContext(TaskContext)
    const task = tasks.find(task => task.token === props.match.params.token)

    const jwt_token = localStorage.getItem('token')

    const [webSocket] = useSocket(`ws://localhost:8000/ws/polls/${task.token}/?token=${jwt_token}`)

    return (
        <>
        <h2 className="mt-2 text-center">#{ task.token } - { task.name }</h2>
        <div className="columns col-oneline">
            <div className="column col-9">
                <p>{ task.description }</p>
            </div>
            <div className="column col-3 float-right">
                Overall score: <span className="label label-rounded label-primary">{ task.score }</span>
            </div>
        </div>
        <div className="columns">
            <aside className="column col-4">
                <VoteForm webSocket={webSocket} task={task}/>
            </aside>

            <VoteList webSocket={webSocket}/>
        </div>
        </>
    );
}

export default PollPage;
