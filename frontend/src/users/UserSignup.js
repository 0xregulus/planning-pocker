import React, { useState, useContext } from 'react'
import { useHistory } from "react-router-dom";
import API from '../Api.js'
import { UserContext } from './UserContext.js'


const SignupForm = () => {

    const history = useHistory()

    const [form, setForm] = useState({
          username: '',
          password: ''
    })

    const { dispatch } = useContext(UserContext)

    const submit = e => {
        e.preventDefault()
        API.signup(form).then(
            data => {
                dispatch({
                    type: 'SET_USER',
                    payload: data
                })
                history.push('/tasks')
            }
        ).catch(
            err => {
                console.log(err)
            }
        ).finally(
            () => {
                setForm({
                    username: '',
                    password: ''
                })
            }
        )
    }

    return (
        <form onSubmit={submit}>
            <div className="panel">
                <div className="panel-header">
                    <div className="panel-title">Sign up</div>
                </div>
                <div className="panel-body">
                    <div className="form-group">
                        <label className="form-label" htmlFor="input-name">Username</label>
                        <input
                            name="form[username]"
                            value={form.username}
                            onChange={e => setForm({ ...form, username: e.target.value })}
                            className="form-input"
                            type="text"
                            id="input-username-signup"
                            placeholder="Username"
                        />
                    </div>
                    <div className="form-group">
                        <label className="form-label" htmlFor="input-password">Password</label>
                        <input
                            name="form[password]"
                            value={form.password}
                            onChange={e => setForm({ ...form, password: e.target.value })}
                            className="form-input"
                            type="password"
                            id="input-password-signup"
                            placeholder="Password"
                        />
                    </div>
                </div>
                <div className="panel-footer">
                    <input className="btn btn-primary btn-lg" name="Signup" value="Sign up" type="submit"/>
                </div>
            </div>
        </form>
    )
}

export default SignupForm;
