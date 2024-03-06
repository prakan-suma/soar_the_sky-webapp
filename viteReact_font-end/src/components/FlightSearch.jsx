import React, { useEffect, useState } from 'react';
import { PiAirplaneTakeoff } from "react-icons/pi";
import { PiAirplaneLanding } from "react-icons/pi";
import { IoIosArrowForward } from "react-icons/io";
import { FiCalendar } from "react-icons/fi";
import { PiUsersBold } from "react-icons/pi";
import { useHistory } from 'react-router-dom';

const FlightSearch = () => {
    const [tripType, setTripType] = useState('round-trip');
    const [passenger, setPassenger] = useState(1);
    const [departureAirport, setDepartureAirport] = useState('');
    const [destinationAirport, setDestinationAirport] = useState('');
    const [departureDate, setDepartureDate] = useState('');
    const [returnDate, setReturnDate] = useState('');
    const [airports, setAirports] = useState([]);
    const [errorInputs, setErrorInputs] = useState([]);
    const history = useHistory();

    const handleTripTypeChange = (type) => {
        setTripType(type);
    };

    const handleDepartureAirportChange = (event) => {
        setDepartureAirport(event.target.value);
    };

    const handleDestinationAirportChange = (event) => {
        setDestinationAirport(event.target.value);
    };

    const handlePassengerChange = (event) => {
        setPassenger(event.target.value);
    };

    const handleDepartureDateChange = (event) => {
        setDepartureDate(event.target.value);
    };

    const handleReturnDateChange = (event) => {
        setReturnDate(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const inputs = [departureAirport, destinationAirport, departureDate];
        if (tripType === 'round-trip') {
            inputs.push(returnDate);
        }

        // Check if departure and destination airports are the same
        if (departureAirport === destinationAirport) {
            setErrorInputs(['departureAirport', 'destinationAirport']);
            return;
        }

        // Check if departure date is after return date (for round trip)
        if (tripType === 'round-trip' && new Date(departureDate) > new Date(returnDate)) {
            setErrorInputs(['departureDate', 'returnDate']);
            return;
        }

        const errorInputNames = [];
        if (departureAirport === '') errorInputNames.push('departureAirport');
        if (destinationAirport === '') errorInputNames.push('destinationAirport');
        if (departureDate === '') errorInputNames.push('departureDate');
        if (tripType === 'round-trip' && returnDate === '') errorInputNames.push('returnDate');

        setErrorInputs(errorInputNames);

        if (errorInputNames.length > 0) {
            return;
        }

        // Clear error inputs if no errors
        setErrorInputs([]);

        // Redirect or send data based on input validation
        if (tripType === 'one-way') {
            history.push(`/flight/search/${tripType}/${passenger}/${departureAirport}/${destinationAirport}/${departureDate}`);
        } else {
            history.push(`/flight/search/${tripType}/${passenger}/${departureAirport}/${destinationAirport}/${departureDate}/${returnDate}`);
        }
    };

    useEffect(() => {
        // Fetch airport data from the API
        fetch('http://127.0.0.1:8000/api/airport/search/all/')
            .then(response => response.json())
            .then(data => setAirports(data))
            .catch(error => console.error('Error fetching airport data:', error));
    }, []);

    return (
        <section className='mb-60'>

            <div style={{ height: 600 }} className="relative overflow-hidden rounded-3xl">
                <video
                    className="w-full object-cover"
                    autoPlay
                    muted
                    loop
                >
                    <source src="./video/banner.mp4" type="video/mp4" />
                    Your browser does not support the video tag.
                </video>

                <div className="absolute inset-0 bg-gradient-to-b from-transparent to-black opacity-50"></div>
                <div className="absolute inset-0 flex items-center justify-center">
                    <div className="flex flex-col w-1/2 text-center ">

                        <h1 className="text-white text-4xl mb-6">
                            Welcome to SoarTheSkye
                        </h1>
                        <p className='text-slate-100 font-light '>Soar the Skye is a revolutionary new airline that offers a unique and unforgettable travel experience. With our state-of-the-art fleet of aircraft, luxurious amenities, and unparalleled customer service, we are committed to making your journey as enjoyable and stress-free as possible.</p>

                    </div>
                </div>
            </div>
            
            <div id='searchFlight'  className="search-flight w-3/4 overflow-hidden absolute left-1/2 transform -translate-x-1/2 drop-shadow-2xl">
                <div className="bg-cs-skye rounded-tr-2xl rounded-tl-2xl w-fit py-4 px-6 text-white">
                    <p>Search Flights</p>
                </div>

                <form className='' onSubmit={handleSubmit}>
                    <div className='w-fit rounded-2xl rounded-tl-none bg-white py-10 px-6 '>
                        <div className="flex flex-row gap-10 mt-4">
                            <div className="flex gap-3 items-center">
                                <input
                                    type="radio"
                                    id="round-trip"
                                    name="tripType"
                                    className="h-5 w-5"
                                    checked={tripType === 'round-trip'}
                                    onChange={() => handleTripTypeChange('round-trip')}
                                />
                                <label htmlFor="round-trip">Round trip</label>
                            </div>
                            <div className="flex gap-3 items-center">
                                <input
                                    type="radio"
                                    id="one-way"
                                    name="tripType"
                                    className="h-5 w-5"
                                    checked={tripType === 'one-way'}
                                    onChange={() => handleTripTypeChange('one-way')}
                                />
                                <label htmlFor="one-way">One Way</label>
                            </div>
                            <div className="relative">
                                <div className="absolute inset-y-0 start-0 flex items-center ps-4 pointer-events-none">
                                    <PiUsersBold className='text-cs-skye text-2xl' />
                                </div>
                                <select
                                    id="passenger"
                                    className={`border-none focus:border-none text-gray-900 text-sm ps-12 p-4 ${errorInputs.includes('passenger') ? 'border-red-500' : ''}`}
                                    value={passenger}
                                    onChange={handlePassengerChange}
                                >
                                    <option value={1}>1 Passenger</option>
                                    <option value={2}>2 Passenger</option>
                                    <option value={3}>3 Passenger</option>
                                    <option value={4}>4 Passenger</option>
                                </select>
                            </div>
                        </div>

                        <div className="flex mt-10">
                            <section className='flex justify-evenly gap-4 mb-6'>
                                <div className="relative drop-shadow-sm">
                                    <div className='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'>
                                        <PiAirplaneTakeoff className='text-cs-skye text-3xl' />
                                    </div>
                                    <select
                                        id="departureAirport"
                                        className={`w-full overflow-visible bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 ps-12 p-4 ${errorInputs.includes('departureAirport') ? 'border-red-500' : ''}`}
                                        onChange={handleDepartureAirportChange}
                                        value={departureAirport}
                                    >
                                        <option value="">Choose an airport</option>
                                        {airports.map(airport => (
                                            <option key={airport.airport_id} value={airport.airport_code}>
                                                {airport.name} ({airport.airport_code})
                                            </option>
                                        ))}
                                    </select>
                                </div>
                                <div className="border rounded-lg drop-shadow-sm flex items-center  p-2.5 my-2 ">
                                    <IoIosArrowForward />
                                </div>
                                <div className="relative drop-shadow-sm overflow-visible">
                                    <div className='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none' >
                                        <PiAirplaneLanding className='text-cs-skye text-3xl' />
                                    </div>
                                    <select
                                        id="destinationAirport"
                                        className={`w-full bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 ps-12 p-4 ${errorInputs.includes('destinationAirport') ? 'border-red-500' : ''}`}
                                        onChange={handleDestinationAirportChange}
                                        value={destinationAirport}
                                    >
                                        <option value="">Choose an airport</option>
                                        {airports.map(airport => (
                                            <option key={airport.airport_id} value={airport.airport_code}>
                                                {airport.name} ({airport.airport_code})
                                            </option>
                                        ))}
                                    </select>
                                </div>
                                <div className="relative  drop-shadow-sm ms-5">
                                    <div className="absolute inset-y-0 start-0 flex items-center ps-4 pointer-events-none">
                                        <FiCalendar className='text-cs-skye text-2xl' />
                                    </div>
                                    <input
                                        type='date'
                                        className={`bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 w ps-12 p-4 ${errorInputs.includes('departureDate') ? 'border-red-500' : ''}`}
                                        onChange={handleDepartureDateChange}
                                        value={departureDate}
                                    />
                                </div>
                                {tripType === 'round-trip' && (
                                    <div className="relative drop-shadow-sm">
                                        <div className="absolute inset-y-0 start-0 flex items-center ps-4 pointer-events-none">
                                            <FiCalendar className='text-cs-skye text-2xl' />
                                        </div>
                                        <input
                                            type='date'
                                            className={`bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 ps-12 p-4 ${errorInputs.includes('returnDate') ? 'border-red-500' : ''}`}
                                            onChange={handleReturnDateChange}
                                            value={returnDate}
                                        />
                                    </div>
                                )}
                                <button type="submit" className='bg-sky-600 hover:border-sky-600 text-white px-6 rounded-lg'>
                                    Search
                                </button>
                            </section>
                        </div>
                    </div>
                </form>
            </div>
        </section>
    );
};
export default FlightSearch;
