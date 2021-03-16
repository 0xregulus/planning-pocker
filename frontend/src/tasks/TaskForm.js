import React, { useState, useContext } from 'react'
import { TaskContext } from './TaskContext.js'
import API from '../Api.js'


const TaskForm = () => {
  const [form, setForm] = useState({
      name: '',
      description: ''
  })

  const { dispatch } = useContext(TaskContext)

  const submit = e => {
    e.preventDefault()
    API.postNewTask(form).then(
        data => {
            dispatch({
                type: 'ADD_TASK',
                payload: data
            })
        }
    ).catch(
        err => {
            console.log(err);
        }
    ).finally(
        () => {
            setForm({
                name: '',
                description: ''
            })
        }
    )
  }

  return (
    <form onSubmit={submit}>
        <div className="panel">
            <div className="panel-header">
                <div className="panel-title">Create new task</div>
            </div>
            <div className="panel-body">
                <div className="form-group">
                    <label className="form-label" htmlFor="input-name">Name</label>
                    <input
                        name="form[name]"
                        value={form.name}
                        onChange={e => setForm({ ...form, name: e.target.value })}
                        className="form-input"
                        type="text"
                        id="input-name"
                        placeholder="Name the task"
                    />
                </div>
                <div className="form-group">
                    <label className="form-label" htmlFor="input-description">Description</label>
                    <textarea
                        name="form[description]"
                        value={form.description}
                        onChange={e => setForm({ ...form, description: e.target.value })}
                        className="form-input"
                        id="input-description"
                        placeholder="Describe the task"
                        rows="3"
                    />
                </div>
            </div>
            <div className="panel-footer">
                <input className="btn btn-primary btn-lg" name="Create" value="Create" type="submit"/>
            </div>
        </div>
    </form>
  )
}

export default TaskForm;
