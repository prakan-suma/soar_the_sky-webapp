from flask import Flask, jsonify, Response
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

data_list = [
    {
        "balance": "$3,946.45",
        "picture": "http://placehold.it/32x32",
        "age": 23,
        "name": "Bird Ramsey",
        "gender": "male",
        "company": "NIMON",
        "email": "birdramsey@nimon.com"
    },
    {
        "balance": "$2,345.67",
        "picture": "http://placehold.it/32x32",
        "age": 30,
        "name": "Alice Johnson",
        "gender": "female",
        "company": "ABC Company",
        "email": "alicejohnson@example.com"
    },
    # ข้อมูลผู้ใช้เพิ่มเติม ...
]

flight_list = [
    {
        "id": 1,
        "departure_station": "BKK",
        "takeoff": "09:00 AM",
        "destination_station": "UDP",
        "landing": "10:15 AM",
        "direct": "1h 15m",
        "price": "2,234"
    },
    {
        "id": 2,
        "departure_station": "CNX",
        "takeoff": "10:30 AM",
        "destination_station": "HKT",
        "landing": "12:45 PM",
        "direct": "2h 15m",
        "price": "3,567"
    },
    # ข้อมูลเที่ยวบินเพิ่มเติม ...
]

@app.route('/')
def home():
    return "Welcome to flask back-end";
    

# SSE endpoint for flight data
@app.route('/api/flight_all_sse')
def api_get_flight_sse():
    def generate():
        while True:
            for flight in flight_list:
                yield 'data: {}\n\n'.format(jsonify(flight))
                time.sleep(1)  # ส่งข้อมูลทุก 1 วินาที

    return Response(generate(), content_type='text/event-stream')

# run back-end
if __name__ == '__main__':
    app.run(debug=True)