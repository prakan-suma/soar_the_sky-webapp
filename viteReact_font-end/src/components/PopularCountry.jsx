import React from 'react'

function PopularCountry() {
    return (
        <div className='w-full mt-72'>
            <div className="w-3/4 mx-auto">
                <h1 className='text-center text-3xl font-bold text-gray-700' >Popular Country</h1>

                <div className="flex gap-10">
                    {/* img Card */}
                    <div style={{ height: 500 }} className="relative w-1/3 bg-gray-300 rounded-xl overflow-hidden my-12 hover:-translate-y-6 transition-all">
                        <img
                            className="absolute inset-0 w-full h-full object-cover object-center"
                            src="https://images.pexels.com/photos/1031698/pexels-photo-1031698.jpeg?auto=compress&cs=tinysrgb&w=600"
                            alt="placeholder"
                        />
                        <div className="absolute inset-0 bg-gradient-to-b from-sky-600 to-black opacity-50"></div>
                        <div className="absolute p-4 text-gray-50 text-center  m-auto top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                            <h2 className="text-lg font-bold shadow-md">Bangkok</h2>
                            <p className="text-sm shadow-md">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                        </div>
                    </div>

                    {/* img Card */}
                    <div style={{ height: 500 }} className="relative w-1/3 bg-gray-300 rounded-xl overflow-hidden my-12 hover:-translate-y-6 transition-all">
                        <img
                            className="absolute inset-0 w-full h-full object-cover object-center"
                            src="https://images.pexels.com/photos/16963635/pexels-photo-16963635.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
                            alt="placeholder"
                        />
                        <div className="absolute inset-0 bg-gradient-to-b from-sky-600 to-black opacity-50"></div>
                        <div className="absolute p-4 text-gray-50 text-center  m-auto top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                            <h2 className="text-lg font-bold shadow-md">chiang mai</h2>
                            <p className="text-sm shadow-md">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                        </div>
                    </div>
                    
                    {/* img Card */}
                    <div style={{ height: 500 }} className="relative w-1/3 bg-gray-300 rounded-xl overflow-hidden my-12 hover:-translate-y-6 transition-all">
                        <img
                            className="absolute inset-0 w-full h-full object-cover object-center"
                            src="https://thailandinsider.com/wp-content/uploads/2019/03/shutterstock_544824664-1024x683.jpg"
                            alt="placeholder"
                        />
                        <div className="absolute inset-0 bg-gradient-to-b from-sky-600 to-black opacity-50"></div>
                        <div className="absolute p-4 text-gray-50 text-center  m-auto top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                            <h2 className="text-lg font-bold shadow-md">Ubon ratchathani</h2>
                            <p className="text-sm shadow-md">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default PopularCountry