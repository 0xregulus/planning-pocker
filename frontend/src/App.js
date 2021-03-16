import React from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import UserPage from './users/UserPage.js'
import PollPage from './polls/PollPage.js'
import TaskPage from './tasks/TaskPage.js'
import TaskContextProvider from './tasks/TaskContext'
import UserContextProvider from './users/UserContext'
import PollContextProvider from './polls/PollContext'


const App = () => {

    return (
        <div className="App">
            <h1 className="mt-2 text-center">Collaborative Planning App</h1>
                <UserContextProvider>
                    <TaskContextProvider>
                        <PollContextProvider>
                            <Router>
                                <Switch>
                                    <Route exact path="/" component={UserPage}/>
                                    <Route exact path="/tasks" component={TaskPage}/>
                                    <Route exact path="/polls/:token" component={PollPage}/>
                                </Switch>
                            </Router>
                        </PollContextProvider>
                    </TaskContextProvider>
                </UserContextProvider>
            </div>
    );
}

export default App;
