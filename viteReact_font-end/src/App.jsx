import Nav from './components/Nav'
import React from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import Home from './pages/Home';
import Register from './pages/Register';
import './App.css';
import 'flowbite';
import Footer from './components/Footer';

function App() {
  return (
    <Router>
      <div className=''>
        <Nav />
        <Switch>
          <Route exact path="/" component={Home} />
        </Switch>
      </div>
      <Footer/>
    </Router>
  )
}

export default App
