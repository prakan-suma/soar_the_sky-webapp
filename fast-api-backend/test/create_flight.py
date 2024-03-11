# สร้างฟังก์ชันสำหรับคำนวณระยะเวลาระหว่างเวลาออกและถึง
def calculate_duration(departure_time, arrival_time):
    departure = datetime.strptime(departure_time, '%H:%M')
    arrival = datetime.strptime(arrival_time, '%H:%M')
    duration = arrival - departure
    return str(duration)

# ข้อมูลเที่ยวบินสำหรับ departure_airport
departure_flights = [
    {"flight_no": "BN101", "departure_time": "06:00", "arrival_time": "07:00"},
    {"flight_no": "BN102", "departure_time": "09:00", "arrival_time": "10:00"},
    {"flight_no": "BN103", "departure_time": "12:00", "arrival_time": "13:00"},
    {"flight_no": "BN104", "departure_time": "15:00", "arrival_time": "16:00"},
    {"flight_no": "BN105", "departure_time": "18:00", "arrival_time": "19:00"}
]

# ข้อมูลเที่ยวบินสำหรับ destination_airport
destination_flights = [
    {"flight_no": "CX101", "departure_time": "08:00", "arrival_time": "09:00"},
    {"flight_no": "CX102", "departure_time": "11:00", "arrival_time": "12:00"},
    {"flight_no": "CX103", "departure_time": "14:00", "arrival_time": "15:00"},
    {"flight_no": "CX104", "departure_time": "16:00", "arrival_time": "18:00"},
    {"flight_no": "CX105", "departure_time": "19:00", "arrival_time": "20:00"}
]

# สร้างข้อมูล JSON
flights_data = {
    "1": [],
    "3": []
}

# เพิ่มข้อมูลเที่ยวบินสำหรับ departure_airport
for flight in departure_flights:
    flight_data = {
        "flight_no": flight["flight_no"],
        "departure_airport": 1,
        "destination_airport": 3,
        "departure_time": flight["departure_time"],
        "arrival_time": flight["arrival_time"],
        "duration_time": calculate_duration(flight["departure_time"], flight["arrival_time"]),
        "airplane": 1,
        "price": random.randint(1000, 1800),
        "departure_date": []
    }
    for i in range(10):
        departure_date = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
        flight_data["departure_date"].append({departure_date: {"flight_seat": []}})
    flights_data["1"].append(flight_data)

# เพิ่มข้อมูลเที่ยวบินสำหรับ destination_airport
for flight in destination_flights:
    flight_data = {
        "flight_no": flight["flight_no"],
        "departure_airport": 3,
        "destination_airport": 1,
        "departure_time": flight["departure_time"],
        "arrival_time": flight["arrival_time"],
        "duration_time": calculate_duration(flight["departure_time"], flight["arrival_time"]),
        "airplane": 1,
        "price": random.randint(1000, 1800),
        "departure_date": []
    }
    for i in range(10):
        departure_date = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
        flight_data["departure_date"].append({departure_date: {"flight_seat": []}})
    flights_data["3"].append(flight_data)
# แปลงข้อมูล JSON เป็น JSON string
json_data = json.dumps(flights_data, indent=4)

# พิมพ์ JSON string
with open('./src/database/flightInstances.json' ,'w') as f:
    f.write(json_data)