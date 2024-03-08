import React, { useState, useEffect } from 'react';

export default function Nav() {
    const [scrollPosition, setScrollPosition] = useState(0);

    useEffect(() => {
        function handleScroll() {
            setScrollPosition(window.scrollY); 
        }
        window.addEventListener('scroll', handleScroll);
        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, []);

    return (
        <>
            <nav style={{ backgroundColor: scrollPosition > 0 ? '#ffffff' : 'transparent' , transition: 'background-color 0.3s ease-in-out'}} className="fixed w-full top-0 shadow-md z-50">
                <div className="container mx-auto">
                    <div className="flex justify-between py-4 text-lg items-center font-semibold text-zinc-800">
                        <div>
                            <a className="font-bold text-3xl text-cs-skye" href="/">SoarTheSkye.</a>
                        </div>
                        <ul className="flex gap-20">
                            <li><a href="/">Home</a></li>
                            <li><a href="#searchFlight">Flights</a></li>
                            <li><a href="/">Booking</a></li>
                        </ul>
                        <div className="flex items-center gap-8">
                            <a href="/login">Login</a>
                            <a href='/register' class="text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 rounded-lg px-5 py-2 text-center ">Sign Up</a>
                        </div>
                    </div>
                </div>
            </nav>
        </>
    );
}
