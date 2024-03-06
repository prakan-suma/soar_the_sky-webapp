import './App.css';
import 'flowbite';
import React from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import Nav from './components/Nav'
import Footer from './components/Footer';
import Home from './pages/Home';
import FlightOneWay from './pages/FlightOneWay';
import FlightRoundTrip from './pages/FlightRoundTrip';

function App() {
  return (
    <Router>
      <div className=''>
        <Nav />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/flight/search/:tripType/:passenger/:departureAirport/:destinationAirport/:departureDate" component={FlightOneWay} />
          <Route path="/flight/search/:tripType/:passenger/:departureAirport/:destinationAirport/:departureDate/:destinationDate" component={FlightRoundTrip} />
        </Switch>
      </div>
      <Footer/>
    </Router>
  )
}

export default App
