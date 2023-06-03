import React, { Fragment, useState } from 'react';
import Button from './Button';

const Sandbox = () => {
  const [inputChannel1, setInputChannel1] = useState('')
  const [inputMessageType, setInputMessageType] = useState('')
  const [inputRepoName, setInputRepoName] = useState('')
  const [inputWork, setInputWork] = useState('')
  const [inputChannel2, setInputChannel2] = useState('')
  const [inputEmail, setInputEmail] = useState('')

  return (<Fragment>
    <h2><span>1. Generate Message:</span></h2>
    channel name: <input type="text" name="channel_name1" onChange={(event) => setInputChannel1(event.target.value)}/>
    <br/>
    <br/>
    message type: <input type="text" name="message_type" onChange={(event) => setInputMessageType(event.target.value)}/>
    <br/>
    <br/>
    repo name: <input type="text" name="repo_name" onChange={(event) => setInputRepoName(event.target.value)}/>
    <br/>
    <br/>
    work: <input type="text" name="work" onChange={(event) => setInputWork(event.target.value)}/>
    <br/>
    <br/>
    <Button onClick={() => {
      console.log(inputChannel1)
      console.log(inputMessageType)
      console.log(inputWork)
      fetch("http://localhost:5000/generate_message", {
        'method':'POST',
        'headers':{
          'Content-Type':'application/json'
        },
        'body':JSON.stringify({'chanel_name': inputChannel1, 'message_type': inputMessageType, 'repo_name': inputRepoName, 'work': inputWork})

      })
          .then(res => res.json())
          .then((data) => {
            console.log(data)
          })
          .catch((error) => {
            console.log(error)
          })
    }}>generate</Button>

    <h2><span>2. Chat History</span></h2>
    channel name: <input type="text" name="channel_name2" onChange={(event) => setInputChannel2(event.target.value)}/>
    <br/>
    <br/>
    email: <input type="text" name="email" onChange={(event) => setInputEmail(event.target.value)}/>
    <br/>
    <br/>
    <Button onClick={() => {
      console.log(inputChannel2)
      console.log(inputEmail)
      fetch("http://localhost:5000/chat_history", {
        'method':'POST',
        'headers':{
          'Content-Type':'application/json'
        },
        'body':JSON.stringify({'channel_name': inputChannel2, 'email': inputEmail})
      })
          .then(res => res.json())
          .then((data) => {
            console.log(data)
          })
          .catch((error) => {
            console.log(error)
          })
    }}>Send</Button>
  </Fragment>)
};

export default Sandbox;