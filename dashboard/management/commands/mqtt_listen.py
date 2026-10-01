import json
import os

import paho.mqtt.client as mqtt
from django.core.management.base import BaseCommand, CommandError

from dashboard.models import SensorReading


class Command(BaseCommand):
    help = "Écoute le broker MQTT et enregistre chaque message reçu en base."

    def handle(self, *args, **options):
        broker = os.getenv('MQTT_BROKER')
        port = int(os.getenv('MQTT_PORT', 1883))
        username = os.getenv('MQTT_USERNAME')
        password = os.getenv('MQTT_PASSWORD')
        self.topic = os.getenv('MQTT_TOPIC', '#')

        if not broker:
            raise CommandError("MQTT_BROKER n'est pas défini dans le .env")

        client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        if username:
            client.username_pw_set(username, password)
        client.on_connect = self.on_connect
        client.on_disconnect = self.on_disconnect
        client.on_message = self.on_message

        self.stdout.write(f"Connexion à {broker}:{port}...")
        client.connect(broker, port, keepalive=60)

        try:
            client.loop_forever()
        except KeyboardInterrupt:
            client.disconnect()
            self.stdout.write("Arrêt de l'écoute MQTT.")

    def on_connect(self, client, userdata, flags, reason_code, properties):
        if reason_code.is_failure:
            self.stderr.write(f"Échec de connexion : {reason_code}")
            return
        self.stdout.write(self.style.SUCCESS("Connecté à Mosquitto avec succès"))
        # Subscribing here means we re-subscribe automatically after a reconnect
        client.subscribe(self.topic)
        self.stdout.write(f"Abonné à « {self.topic} »")

    def on_disconnect(self, client, userdata, flags, reason_code, properties):
        self.stderr.write(f"Déconnecté : {reason_code}")

    def on_message(self, client, userdata, msg):
        # Zigbee2MQTT internal topics (logs, health, device list...), not sensor data
        if '/bridge/' in msg.topic or msg.topic.endswith('/availability'):
            return

        raw = msg.payload.decode(errors='replace')
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            data = None
        if not isinstance(data, dict):
            data = {'value': raw}

        try:
            SensorReading.objects.create(topic=msg.topic, data=data)
        except Exception as exc:
            # A DB error must not kill the listener
            self.stderr.write(f"Erreur d'enregistrement [{msg.topic}] : {exc}")
            return
        self.stdout.write(f"[{msg.topic}] {data}")
