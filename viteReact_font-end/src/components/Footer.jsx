import React from 'react'

function Footer() {
    return (
        <footer className=' bg-gray-950 w-full text-white'>
            <div className="container mx-auto w-full py-20 flex  justify-between">
                <div className="">
                    <a className='font-bold text-4xl text-cs-skye' href="">SoarTheSkye.</a>
                    <p className='text-sm font-thin'> AIRLINE COMPANY</p>
                </div>

                <div className="content-center flex w-1/3 justify-between ">


                    <div className="">
                        <legend>MENU</legend>
                        <ul className='mt-6 text-sm font-light text-gray-300 flex flex-col gap-4'>
                            <li>Home</li>
                            <li>Flight</li>
                            <li>Booking</li>
                        </ul>
                    </div>

                    <div className="">
                        <legend>Developer</legend>
                        <ul className='mt-6 text-sm font-light text-gray-300 flex flex-col gap-4'>
                            <li>Prakan Suma</li>
                            <li>Pip</li>
                            <li>Pat</li>
                            <li>Link</li>
                        </ul>
                    </div>

                    <div className="">
                        <legend>Contract</legend>
                        <ul className='mt-6 text-sm font-light text-gray-300 flex flex-col gap-4'>
                            <li>+6622-222-2232</li>
                            <li>soartheskye@soartheskye.com</li>
                        </ul>
                    </div>





                </div>
                <div className="">
                    <span className='font-thin'>&copy; soartheskye airline company</span>

                </div>
            </div>
        </footer>
    )
}

export default Footer