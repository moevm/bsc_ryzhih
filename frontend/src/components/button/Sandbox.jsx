import React, { Fragment } from 'react';
import Button from './Button';
//import axios from "axios"

const Sandbox = () => (

  <Fragment>

    <h2><span>1. Post request:</span></h2>
    <Button onClick={() => { 
      console.log('!!!!')
      fetch("http://localhost:5000/hello", {
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
    }}>Post</Button>

    <h2><span>2. Get request:</span></h2>
    <Button onClick={() => { 
      console.log('!!!!');
      fetch("http://localhost:5000/members")
      .then(res => res.json())
      .then((data) => {
        console.log(data)
      })
      .catch((err) => {
        console.log(err)
      })
      }}>Get</Button>

    <h2><span>3. Get request:</span></h2>
    <Button onClick={() => { 
      console.log('!!!!');
      fetch("http://localhost:5000/members")
      .then(res => res.json())
      .then((data) => {
        console.log(data)
      })
      .catch((err) => {
        console.log(err)
      })
      }}>Get</Button>

  </Fragment>
);

export default Sandbox;