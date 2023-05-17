import React, { Fragment, useEffect, useState, useTransition } from 'react';
import './home.css';


const Home = () => 
{
  const [auth, setAuth] = useState(window.localStorage.getItem("login"))
  useEffect(() => {
    if (!auth) window.location.href = "/registration"
  }, [auth])
  return(
  <Fragment>
    <h1 className="title"><span>Начальная страница ETU_Bot</span></h1>
    <p>Здесь будет находиться основная информация о боте.</p>
  </Fragment>
  )
}

export default Home;
