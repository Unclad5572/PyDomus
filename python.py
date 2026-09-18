import logging
import paho.mqtt.client as mqtt

logging.basicConfig(level=logging.DEBUG)

BROKER = "141.94.106.107"
PORT = 1883
#If you have set a username and password for your Mosquitto broker, replace "admin" and "password" with your actual credentials.
USERNAME = "admin"
PASSWORD = "password"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Échec de connexion : {reason_code}")
    else:
        print("Connecté à Mosquitto avec succès")
        client.subscribe("#")

def on_disconnect(client, userdata, flags, reason_code, properties):
    print(f"Déconnecté : {reason_code}")

def on_subscribe(client, userdata, mid, reason_code_list, properties):
    print(f"Abonnement : {reason_code_list}")

def on_message(client, userdata, msg):
    print(f"[{msg.topic}] {msg.payload.decode(errors='replace')}")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.enable_logger()
client.username_pw_set(USERNAME, PASSWORD)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect(BROKER, PORT, keepalive=60)
client.loop_forever()