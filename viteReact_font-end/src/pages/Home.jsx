import React from 'react';
import FlightSearch from '../components/FlightSearch';
import PopularCountry from '../components/PopularCountry';

const Home = () => {
    return (
        <div className="container relative mx-auto mt-28 ">

            <FlightSearch />
            
            <section className=''>
                <PopularCountry />
            </section>

        </div >


    );
};

export default Home;
