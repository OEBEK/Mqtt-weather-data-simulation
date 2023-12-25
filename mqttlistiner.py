import paho.mqtt.client as mqtt
import json
from Database import DatabaseHandler

def on_connect(client, userdata, flags, rc):
    client.subscribe("Wetterdata")
    return True

def on_message(client, userdata, msg):
    db = DatabaseHandler(host="localhost", user="root", password="", database="wetterdaten")

    weather_data = json.loads(msg.payload.decode('utf-8'))
    temperature = weather_data.get('Temperature', 0.0)
    humidity = weather_data.get('Humidity', 0.0)
    pressure = weather_data.get('Pressure', 0.0)
    altitude = weather_data.get('Altitude', 0.0)
    
    result = db.insert_data(humidity, pressure, altitude, temperature)
    print(result)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883)
client.loop_forever()
print("gespeichert")