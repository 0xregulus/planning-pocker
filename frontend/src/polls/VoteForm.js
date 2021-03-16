import React, { useState, useContext } from 'react'
import { UserContext } from '../users/UserContext.js'


const VoteForm = (props) => {

    const { user } = useContext(UserContext)

    const [form, setForm] = useState({
        user: user.user_id,
        task: props.task.id,
        value: '',
        comments: ''
    })

    const submit = e => {
        e.preventDefault()
        props.webSocket.send(JSON.stringify(form))
        setForm({
            user: user.user_id,
            task: props.task.id,
            value: '',
            comments: ''
        })
    }

    return (
        <form onSubmit={submit}>
            <div className="panel">
                <div className="panel-header">
                    <div className="panel-title">How complex is this tasks?</div>
                </div>
                <div className="panel-body">
                    <div className="form-group">
                        <select
                            name="form[value]"
                            value={form.value}
                            onChange={e => setForm({ ...form, value: e.target.value })}
                            className="form-select"
                            id="input-value"
                        >
                            <option>Choose your vote</option>
                            <option value="?">?</option>
                            <option value="1/2">1/2</option>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="5">5</option>
                            <option value="8">8</option>
                            <option value="13">13</option>
                        </select>
                    </div>
                    <div className="form-group">
                        <label className="form-label" htmlFor="input-comments">Comments</label>
                        <textarea
                            name="form[comments]"
                            value={form.comments}
                            onChange={e => setForm({ ...form, comments: e.target.value })}
                            className="form-input"
                            id="input-comments"
                            placeholder="Comment about you vote"
                            rows="3"
                        />
                    </div>
                </div>
                <div className="panel-footer">
                    <input className="btn btn-primary btn-lg" name="Vote" value="Vote" type="submit"/>
                </div>
            </div>
        </form>
    )
}

export default VoteForm;
