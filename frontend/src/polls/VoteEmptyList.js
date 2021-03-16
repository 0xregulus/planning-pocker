import React from 'react'


const VoteEmptyList = () => {
    return (
        <div className="empty">
            <div className="empty-icon">
                <i className="icon icon-mail"></i>
            </div>
            <p className="empty-title h5">No votes yet</p>
            <p className="empty-subtitle">Use the left side form to vote.</p>
        </div>
    )
}

export default VoteEmptyList;
