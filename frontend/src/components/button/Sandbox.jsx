import React, { Fragment } from 'react';
import Button from './Button';
//import axios from "axios"

const Sandbox = () => (

  <Fragment>

    <h2><span>1. Generate Message:</span></h2>
    channel name: <input type="text" name="channel_name1" />
    <br/>
    <br/>
    message type: <input type="text" name="message_type" />
    <br/>
    <br/>
    work: <input type="text" name="work" />
    <br/>
    <br/>
    <Button onClick={() => { 
      console.log('!!!!')
      fetch("http://localhost:5000/generate_message", {
        'method':'POST',
        'headers':{
          'Content-Type':'application/json'
        },
        'body':JSON.stringify({'channel_id': '1050570429959507978', 'guild_id': '1001473537451761664', 'message': 'Hello!'})
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
    channel name: <input type="text" name="channel_name2" />
    <br/>
    <br/>
    email: <input type="text" name="email" />
    <br/>
    <br/>
    <Button onClick={() => { 
      console.log('!!!!');
      fetch("http://localhost:5000/chat_history", {
        'method':'POST',
        'headers':{
          'Content-Type':'application/json'
        },
        'body':JSON.stringify({'channel_id': '1050570429959507978', 'guild_id': '1001473537451761664', 'message': 'Hello!'})
      })
      .then(res => res.json())
      .then((data) => {
        console.log(data)
      })
      .catch((error) => {
        console.log(error)
      })
    }}>Send</Button>
  </Fragment>
);

export default Sandbox;