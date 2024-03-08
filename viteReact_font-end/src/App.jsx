import './App.css';
import 'flowbite';
import React from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import Nav from './components/Nav'
import Footer from './components/Footer';
import Home from './pages/Home';
import FlightOneWay from './pages/FlightOneWay';
import FlightRoundTrip from './pages/FlightRoundTrip';
import SignUp from './pages/SignUp';
import Login from './pages/Login';


function App() {
  return (
    <Router>
      <div className=''>
        <Nav />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/flight/search/one-way/:passenger/:departureAirport/:destinationAirport/:departureDate" component={FlightOneWay} />
          <Route path="/flight/search/round-trip/:passenger/:departureAirport/:destinationAirport/:departureDate/:returnDate" component={FlightRoundTrip} />
          <Route path="/register" component={SignUp} />
          <Route path="/login" component={Login} />
        </Switch>
      </div>
      <Footer/>
    </Router>
  )
}

export default App
