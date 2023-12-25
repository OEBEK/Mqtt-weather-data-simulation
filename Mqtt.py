import paho.mqtt.client as mqtt


def connect_to_broker():
    client = mqtt.Client()
 
    try:
        client.connect("localhost", 1883)
    except Exception as e:
        print("Verbindung fehlgeschlagen:", e)
        return None
    return client


def subscribe_to_topic(client, topic):
    client.subscribe(topic)

def publish_message(client, topic, message):
    client.publish(topic, message)

def disconnect_from_broker(client):
    client.disconnect()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    subscribe_to_topic(client, "Wetterdata")  # Replace with the topic you want to subscribe to

def on_message(client, userdata, msg):
    print("Received message on topic {}: {}".format(msg.topic, msg.payload.decode()))

def start_mqtt_listener(client):
    if client:
        client.on_connect = on_connect
        client.on_message = on_message
        client.loop_forever()

