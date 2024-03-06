import React from 'react'
import { useParams } from 'react-router-dom';

function FlightRoundTrip() {
    const {tripType,passenger,departureAirport,destinationAirport,departureDate,destinationDate } = useParams();

    
    return (
        <div className="container relative mx-auto mt-28 ">

        </div >
    )
}

export default FlightRoundTrip