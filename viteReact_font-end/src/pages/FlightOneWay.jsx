import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { AiOutlineSwapRight } from "react-icons/ai";
import { PiHandbagSimple, PiAirplaneInFlightDuotone } from "react-icons/pi";

function FlightOneWay() {
    const { passenger, departureAirport, destinationAirport, departureDate } = useParams();

    const [flights, setFlights] = useState([]);
    const [isLoading, setIsLoading] = useState(false); // Added state to manage loading
    const [noFlights, setNoFlights] = useState(false);

    const formatDuration = (durationStr) => {
        // แปลงสตริง duration เป็นตัวเลขในหน่วยนาที
        const [hours, minutes] = durationStr.split(':').map(timeStr => parseInt(timeStr));

        if (isNaN(hours) || isNaN(minutes)) {
            return 'Invalid duration';
        }

        const totalMinutes = hours * 60 + minutes;

        // แปลงจำนวนนาทีเป็นชั่วโมงและนาที
        const formattedHours = Math.floor(totalMinutes / 60);
        const formattedMinutes = totalMinutes % 60;

        // สร้างข้อความในรูปแบบ "1h 0m" หรือ "1h 30m"
        const formattedDuration = `${formattedHours}h ${formattedMinutes}m`;

        return formattedDuration;
    };

    const formatDate = (dateString) => {
        const options = { weekday: 'short', year: 'numeric', month: 'short', day: 'numeric' };
        const formattedDate = new Date(dateString).toLocaleDateString('en-GB', options);
        return formattedDate;
    };



    useEffect(() => {
        setIsLoading(true);
        fetch(`http://127.0.0.1:8000/api/flight/search/one-way/${passenger}/${departureAirport}/${destinationAirport}/${departureDate}/`)
            .then(response => response.json())
            .then(data => {
                // Filter flights based on the specified departure date
                const filteredFlights = data.filter(flight => {
                    // Check if the flight exists on the specified departure date
                    return flight.departure_dates.some(date => Object.keys(date)[0] === departureDate);
                });
                setFlights(filteredFlights);
                if (filteredFlights.length === 0) {
                    setNoFlights(true);
                }
            })
            .catch(error => console.error('Error fetching data:', error))
            .finally(() => setIsLoading(false));
    }, [passenger, departureAirport, destinationAirport, departureDate]);

    return (
        <div className="container flex mx-auto my-28">
            <div className="border w-1/3 p-10 rounded-md shadow-sm h-fit">
                <h1 className="text-2xl text-cs-skye mb-5">Flights</h1>
                <p className="text-lg mb-4">Search one way </p>

                <div className="flex">
                    <div className="flex flex-col gap-5 my-5 me-5">
                        <p className="text-slate-600">Departure Airport</p>
                        <p className="text-slate-600">Destination Airport</p>
                        <p className="text-slate-600">Passenger</p>
                        <p className="text-slate-600">Departure Date</p>
                    </div>

                    <div className="flex flex-col gap-5 my-5">
                        <p className="text-slate-800">{departureAirport}</p>
                        <p className="text-slate-800">{destinationAirport}</p>
                        <p className="text-slate-800">{passenger}</p>
                        <p className="text-slate-800">{formatDate(departureDate)}</p>
                    </div>
                </div>
            </div>

            {/* Flight data */}
            <div className="flex flex-col ms-10 mx-auto w-full">
                <div className="w-full flex justify-between mb-5">
                    <div className="flex">
                        <div className="text-5xl pe-5">
                            <PiAirplaneInFlightDuotone className='text-cs-skye' />
                        </div>
                        <div className="">
                            <p className='mb-3 text-slate-700 text-2xl'>Depart</p>
                            <p className='font-light text-gray-500'>{departureAirport} to {destinationAirport}</p>
                        </div>
                    </div>

                    <div className='flex align-bottom'>
                        <p className=' h-fit text-gray-500 font-light'>{formatDate(departureDate)}</p>
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
                    flights.length > 0 && (
                        <div className='w-full'>
                            {flights.map((flight) => (
                                <div className='transition ease-in-out flex flex-col border rounded p-5 gap-5 mb-5 shadow-sm hover:shadow-md active:shadow-md transform hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:transform-none' key={flight.flight_no}>
                                    <div className="flex gap-5 items-center ">
                                        <img className='w-12 rounded-full border ' src="https://img.freepik.com/free-vector/detailed-travel-logo_23-2148616611.jpg?size=338&ext=jpg&ga=GA1.1.1395880969.1710028800&semt=ais" alt="" />
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
                                            <p className='text-slate-600'>{flight.duration_time && formatDuration(flight.duration_time)}</p>
                                            <p className='text-xs'>Direct</p>
                                        </div>

                                        <div className="m-auto flex-col items-center gap-5">
                                            <PiHandbagSimple className='text-2xl text-slate-600' />
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