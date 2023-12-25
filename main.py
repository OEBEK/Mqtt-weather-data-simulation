import Mqtt
import random
import time
import json

def generate_weather_data():
    temperature = round(random.uniform(-10, 30), 2)  # Temperature in Celsius
    humidity = round(random.uniform(0, 100), 2)  # Humidity in percentage
    pressure = round(random.uniform(900, 1100), 2)  # Pressure in hPa
    altitude = round(random.uniform(0, 5000), 2)  # Altitude in meters
    battery_percent = round(random.uniform(0, 100), 2)  # Battery percentage

    weather_data = {
        "Temperature": temperature,
        "Humidity": humidity,
        "Pressure": pressure,
        "Altitude": altitude,
    }
    
    json_data = json.dumps(weather_data, indent=2)  

    return json_data
    
weather_data = generate_weather_data()

if __name__ == "__main__":
    client = Mqtt.connect_to_broker()   

    while True:
        weather_data = generate_weather_data()
        
        Mqtt.subscribe_to_topic(client,"Wetterdata")
        Mqtt.publish_message(client,"Wetterdata",weather_data)
        print("gesendet")
        time.sleep(30)