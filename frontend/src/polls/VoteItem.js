import React, { useContext } from 'react'
import { UserContext } from '../users/UserContext.js'


const VoteItem = (props) => {

    const { user } = useContext(UserContext)

    return (
        <>
            <div className="tile">
                <div className="tile-content">
                        <p className="tile-title text-bold">
                            <span className="badge" data-badge={ props.vote.value }>
                                <span className="chip">
                                { props.vote.username === user.username ? 'You' : props.vote.username }
                                </span>
                            </span>
                        </p>
                    <p className="tile-subtitle">
                        { props.vote.comments }
                    </p>
                </div>
            </div>
        </>
    )
}

export default VoteItem;
