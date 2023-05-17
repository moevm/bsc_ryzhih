import React, { Fragment } from 'react';
import Button from '../../components/button/Button';
import './registration.css';


const Registration = () => 
    {
        return(
        <Fragment>
            <h1 className="title"><span>Страница аутентификации</span></h1>
            <Button onClick={() => {
                window.localStorage.setItem("login", '123')
            }}>Войти через github</Button>
        </Fragment>
        )
    }

export default Registration;
