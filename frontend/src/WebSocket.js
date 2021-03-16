import { useEffect, useRef, useContext } from 'react'
import { PollContext } from './polls/PollContext'


const useSocket = (url) => {

    const { current: webSocket } = useRef(new WebSocket(url))
    const { dispatch } = useContext(PollContext)

    useEffect(() => {
        webSocket.onopen = () => {console.log('Connected')}
        webSocket.onclose = () => {console.log('Disconnected')}
        webSocket.onmessage = (message) => {
            const data = JSON.parse(message.data)
            console.log(data);
            if (data.type === 'connect') {
                dispatch({
                    type: 'SET_VOTES',
                    payload: data.payload
                })
            } else if (data.type === 'new_vote') {
                dispatch({
                    type: 'ADD_VOTE',
                    payload: data.payload
                })
            }
        }
        return () => webSocket.close()
    }, [webSocket])

    return [webSocket]
};

export default useSocket;
