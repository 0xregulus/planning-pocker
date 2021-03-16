import React from 'react'


const TaskEmptyList = () => {
    return (
        <div className="empty">
            <div className="empty-icon">
                <i className="icon icon-time"></i>
            </div>
            <p className="empty-title h5">No tasks yet</p>
            <p className="empty-subtitle">Use the left side form to create tasks.</p>
        </div>
    )
}

export default TaskEmptyList;
