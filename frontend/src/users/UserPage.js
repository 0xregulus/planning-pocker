import React from 'react'
import LoginForm from './UserLogin.js'
import SignupForm from './UserSignup.js'


const UserPage = () => {

    return (
        <div className="columns">
            <div className="column">
                <LoginForm/>
            </div>
            <div className="divider-vert" data-content="OR"></div>
            <div className="column">
                <SignupForm/>
            </div>
        </div>
 );
}

export default UserPage;
