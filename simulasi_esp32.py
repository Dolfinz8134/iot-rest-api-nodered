import paho.mqtt.client as mqtt
import json, time, random
from datetime import datetime

BROKER = "localhost"
TOPIC_SENSOR = "iot/sensor"
TOPIC_KONTROL = "iot/kontrol"

# Gunakan CallbackAPIVersion.VERSION1 jika memakai paho-mqtt versi 2.x
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "ESP32-Simulator")
client.connect(BROKER, 1883, 60)
client.loop_start()

print("ESP32 Simulator berjalan... Ctrl+C untuk stop")

try:
    while True:
        data = {
            "suhu": round(random.uniform(25, 32), 1),
            "kelembaban": round(random.uniform(55, 80), 1),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        client.publish(TOPIC_SENSOR, json.dumps(data))
        print(f"Terkirim ke {TOPIC_SENSOR}: {data}")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nSimulator dihentikan.")
    client.loop_stop()
    client.disconnect()