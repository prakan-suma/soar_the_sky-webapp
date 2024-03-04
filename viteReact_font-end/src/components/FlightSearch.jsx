import React, { useState } from 'react';
import { PiAirplaneTakeoff } from "react-icons/pi";
import { PiAirplaneLanding } from "react-icons/pi";
import { IoIosArrowForward } from "react-icons/io";
import { FiCalendar } from "react-icons/fi";
import { PiUsersBold } from "react-icons/pi";

const FlightSearch = () => {
    const [tripType, setTripType] = useState('round-trip');
    const [departureAirport, setDepartureAirport] = useState('');
    const [destinationAirport, setDestinationAirport] = useState('');
    const [departureDate, setDepartureDate] = useState('');
    const [returnDate, setReturnDate] = useState('');

    const handleTripTypeChange = (type) => {
        setTripType(type);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        if (tripType === 'one-way') {
            window.location.href = `/api/flight/search/one-way/${departureAirport}/${destinationAirport}/${departureDate}`;
        } else {
            window.location.href = `/api/flight/search/one-way/${departureAirport}/${destinationAirport}/${departureDate}/${returnDate}`;
        }
    };


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
            <div className="search-flight absolute left-1/2 transform -translate-x-1/2">
                <div className="bg-cs-skye rounded-tr-2xl rounded-tl-2xl w-fit py-4 px-6 text-white">
                    <p>Search Flights</p>
                </div>

                <form className='' onSubmit={handleSubmit}>
                    <div className='w-fit rounded-2xl rounded-tl-none bg-white py-10 px-6 drop-shadow-2xl'>
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

                            {/* Passenger */}
                            <div class="relative">
                                {/* icon  */}
                                <div class="absolute inset-y-0 start-0 flex items-center ps-4 pointer-events-none">
                                    <PiUsersBold className='text-cs-skye text-2xl' />
                                </div>

                                <select id="countries" class="border-none focus:border-none text-gray-900 text-sm ps-12 p-4 ">
                                    <option selected>1 Passenger</option>
                                    <option value="2">2 Passenger</option>
                                    <option value="3">3 Passenger</option>
                                    <option value="4">4 Passenger</option>
                                </select>

                            </div>

                        </div>

                        {/* select section */}
                        <div className="flex mt-10">
                            <section className='flex gap-4 mb-6'>

                                {/* origin airport */}
                                <div class="relative drop-shadow-sm">
                                    {/* icon  */}
                                    <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                                        <PiAirplaneTakeoff className='text-cs-skye text-3xl' />
                                    </div>

                                    <select id="countries" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 ps-12 p-4 ">
                                        <option selected>Choose an airport</option>
                                        <option value="BKK">BKK</option>
                                        <option value="DMK">DMK</option>
                                        <option value="UBT">UBT</option>
                                    </select>
                                </div>

                                {/* arrow to icon */}
                                <div className="border rounded-lg drop-shadow-sm flex items-center  p-2.5 my-2 ">
                                    <IoIosArrowForward />
                                </div>

                                {/* destination airport */}
                                <div class="relative w-full drop-shadow-sm">
                                    {/* icon  */}
                                    <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                                        <PiAirplaneLanding className='text-cs-skye text-3xl' />
                                    </div>

                                    <select id="countries" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 ps-12 p-4 ">
                                        <option selected>Choose an airport</option>
                                        <option value="BKK">BKK</option>
                                        <option value="DMK">DMK</option>
                                        <option value="UBT">UBT</option>
                                    </select>

                                </div>

                                {/* departure date */}
                                <div class="relative  drop-shadow-sm ms-5">
                                    {/* icon  */}
                                    <div class="absolute inset-y-0 start-0 flex items-center ps-4 pointer-events-none">
                                        <FiCalendar className='text-cs-skye text-2xl' />
                                    </div>

                                    <input
                                        type='date'
                                        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full ps-12 p-4"
                                    />
                                </div>

                                {/* return date  */}
                                {tripType === 'round-trip' && (
                                    <div class="relative w-full drop-shadow-sm">
                                        {/* icon  */}
                                        <div class="absolute inset-y-0 start-0 flex items-center ps-4 pointer-events-none">
                                            <FiCalendar className='text-cs-skye text-2xl' />
                                        </div>

                                        <input
                                            type='date'
                                            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full ps-12 p-4"
                                        />
                                    </div>
                                )}

                                <button type="submit" className=' bg-sky-600  hover:border-sky-600 text-white px-6 rounded-lg'>
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
