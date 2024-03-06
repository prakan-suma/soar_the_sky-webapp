import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { AiOutlineSwapRight } from "react-icons/ai";
import { PiHandbagSimple } from "react-icons/pi";

function FlightOneWay() {
    const { tripType, passenger, departureAirport, destinationAirport, departureDate } = useParams();

    const [flights, setFlights] = useState([]);
    const [isLoading, setIsLoading] = useState(false); // Added state to manage loading

    useEffect(() => {
        setIsLoading(true); // Set loading to true while fetching data
        fetch(`http://127.0.0.1:8000/api/flight/search/${tripType}/${passenger}/${departureAirport}/${destinationAirport}/${departureDate}/`)
            .then(response => response.json())
            .then(data => { setFlights(data) })
            .catch(error => console.error('Error fetching data:', error))
            .finally(() => setIsLoading(false));
    }, [tripType, passenger, departureAirport, destinationAirport, departureDate]); // Update on parameter changes

    return (
        <div className="container flex mx-auto my-28">
            <div className="border w-1/4 p-10 rounded-md shadow-sm">
                <h1 className="text-2xl text-cs-skye mb-5">Flights</h1>
                <p className="text-lg mb-4">search {tripType}</p>

                <div className="flex">
                    <div className="flex flex-col gap-5 my-5 me-5">
                        <p className="text-slate-600">Departure Airport</p>
                        <p className="text-slate-600">Destination Airport</p>
                        <p className="text-slate-600">Passenger</p>
                        <p className="text-slate-600">Departure Date</p>
                    </div>

                    <div className="flex flex-col gap-5 my-5">
                        <p className="text-slate-80000">{departureAirport}</p>
                        <p className="text-slate-80000">{destinationAirport}</p>
                        <p className="text-slate-80000">{passenger}</p>
                        <p className="text-slate-80000">{departureDate}</p>
                    </div>
                </div>
            </div>

            {/* Flight data */}
            <div className="flex flex-row  ms-10 mx-auto w-full ">
                {isLoading ? (
                    // Display loading indicator while fetching data
                    <p>Fetching flights...</p>
                ) : (
                    flights.length > 0 && (
                        <div className='w-full '>
                            {flights.map((flight) => (
                                <div className='flex flex-col border rounded p-5 gap-5 mb-5 shadow-sm' key={flight.flight_no}>
                                    <div className="flex gap-5 items-center ">
                                        <img className='w-12 rounded-full border' src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2kLv_uFO-rcIgyolahZ-4WOsrAhqg5T_Kow&usqp=CAU" alt="" />
                                        <p className='font-light'>Soar The Skye Airline</p>
                                    </div>

                                    <div className="flex text-slate-500 gap-10 items-center">
                                        <div className="">
                                            <p className='text-2xl text-slate-600 mb-2'>{flight.departure_time}</p>
                                            <p>{flight.departure_airport.airport_code}</p>
                                        </div>

                                        <div className="m-auto">
                                            <AiOutlineSwapRight className='text-2xl text-slate-400' />
                                        </div>

                                        <div className="">
                                            <p className='text-2xl text-slate-600 mb-2'>{flight.arrival_time}</p>
                                            <p>{flight.destination_airport.airport_code}</p>
                                        </div>

                                        <div className="m-auto">
                                            <p className='text-slate-600'>{flight.duration_time} minute</p>
                                            <p className='text-xs'>Direct</p>
                                        </div>

                                        <div className="m-auto flex-col items-center gap-5">
                                            <PiHandbagSimple className='text-2xl text-slate-600'/>
                                            <p className='text-xs'>7 kg.</p>
                                        </div>

                                        <div className="text-center">
                                            <p><span className='text-cs-skye text-2xl'>฿ {flight.price.toLocaleString()}</span> /pax</p>
                                        </div>

                                        <div className="">
                                            <button className='m-auto py-3 px-6 rounded-lg border bg-cs-skye text-white text-base'>Select</button>
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    )
                )}
            </div>
        </div>
    );
}

export default FlightOneWay;
