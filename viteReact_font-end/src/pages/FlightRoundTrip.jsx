import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { AiOutlineSwapRight } from "react-icons/ai";
import { PiHandbagSimple, PiAirplaneInFlightDuotone } from "react-icons/pi";

function FlightRoundTrip() {
    const { passenger, departureAirport, destinationAirport, departureDate, returnDate } = useParams();

    const [flights, setFlights] = useState({ departure_flights: [], return_flights: [] }); // Initialize flights as an object with departure_flights and return_flights
    const [isLoading, setIsLoading] = useState(false); // Added state to manage loading
    const [noFlights, setNoFlights] = useState(false); // State to track if no flights are available

    useEffect(() => {
        setIsLoading(true); // Set loading to true while fetching data
        fetch(`http://127.0.0.1:8000/api/flight/search/round-trip/${passenger}/${departureAirport}/${destinationAirport}/${departureDate}/${returnDate}/`)
            .then(response => response.json())
            .then(data => {
                setFlights(data);
                if (data.departure_flights.length === 0 && data.return_flights.length === 0) {
                    setNoFlights(true); // Set noFlights to true if there are no flights
                }
            })
            .catch(error => console.error('Error fetching data:', error))
            .finally(() => setIsLoading(false));
    }, [passenger, departureAirport, destinationAirport, departureDate, returnDate]); // Update on parameter changes

    return (
        <div className="container flex mx-auto my-28">
            <div className="border w-1/3 p-10 rounded-md shadow-sm h-fit">
                <h1 className="text-2xl text-cs-skye mb-5">Flights</h1>
                <p className="text-lg mb-4">Search round trip </p>

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
            <div className="flex flex-col ms-10 mx-auto w-full">
                <div className="w-full flex mb-5">
                    <div className="text-5xl pe-5">
                        <PiAirplaneInFlightDuotone className='text-cs-skye' />
                    </div>
                    <div className="">
                        <p className='mb-3 text-slate-700 text-2xl'>Depart</p>
                        <p className='font-light text-gray-500'>{departureAirport} to {destinationAirport}</p>
                    </div>
                </div>
                {isLoading ? (
                    // Display loading indicator while fetching data
                    <p>Fetching flights...</p>
                ) : noFlights ? (
                    // Display message if no flights are available
                    <div className="rounded-lg bg-yellow-100 border-l-4 border-yellow-300 text-yellow-500 p-4" role="alert">
                        <p class="font-bold">Be Warned</p>
                        <p>We're sorry, but we couldn't find the depart flight.</p>
                    </div>
                ) : (
                    flights.departure_flights.length > 0 && (
                        <div className='w-full'>
                        {flights.departure_flights.map((flight) => (
                            <div className='transition ease-in-out flex flex-col border rounded p-5 gap-5 mb-5 shadow-sm hover:shadow-md active:shadow-md transform hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:transform-none' key={flight.flight_no}>
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
                                        <PiHandbagSimple className='text-2xl text-slate-600' />
                                        <p className='text-xs'>7 kg.</p>
                                    </div>

                                    <div className="text-center">
                                        <p><span className='text-cs-skye text-2xl'>฿ {flight.price.toLocaleString() }</span> /pax</p>
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
                <div className="w-full flex mt-10 mb-5">
                    <div className="text-5xl pe-5">
                        <PiAirplaneInFlightDuotone className='text-cs-skye' />
                    </div>
                    <div className="">
                        <p className='mb-3 text-slate-700 text-2xl'>Return</p>
                        <p className='font-light text-gray-500'>{destinationAirport} to {departureAirport}</p>
                    </div>
                </div>
                {isLoading ? (
                    // Display loading indicator while fetching data
                    <p>Fetching flights...</p>
                ) : noFlights ? (
                    // Display message if no flights are available
                    <div className="rounded-lg bg-yellow-100 border-l-4 border-yellow-300 text-yellow-500 p-4" role="alert">
                        <p class="font-bold">Be Warned</p>
                        <p>We're sorry, but we couldn't find the return flight.</p>
                    </div>

                ) : (
                    flights.return_flights.length > 0 && (
                        <div className='w-full'>
                            {flights.return_flights.map((flight) => (
                                <div className='transition ease-in-out flex flex-col border rounded p-5 gap-5 mb-5 shadow-sm hover:shadow-md active:shadow-md transform hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:transform-none' key={flight.flight_no}>
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
                                            <PiHandbagSimple className='text-2xl text-slate-600' />
                                            <p className='text-xs'>7 kg.</p>
                                        </div>

                                        <div className="text-center">
                                            <p><span className='text-cs-skye text-2xl'>฿ {flight.price.toLocaleString() }</span> /pax</p>
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

export default FlightRoundTrip;
