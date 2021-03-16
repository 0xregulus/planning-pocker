import React, { useContext } from 'react'
import VoteEmptyList from './VoteEmptyList.js'
import VoteItem from './VoteItem.js'
import { PollContext } from './PollContext'



const VoteList = (props) => {

    const { votes } = useContext(PollContext)

    return (
        <main className="column">

            <section id="votes">
                <div className="panel">
                    <div className="panel-header">
                        <div className="panel-title h6">Votes</div>
                    </div>
                    <div className="panel-body p-2">
                        {
                            votes.length > 0
                                ? votes.map(vote => {return <VoteItem vote={vote} key={vote.updated}/>})
                                : <VoteEmptyList/>
                        }
                    </div>
                </div>

            </section>

        </main>
    );
}

export default VoteList;
