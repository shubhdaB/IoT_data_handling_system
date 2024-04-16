import paho.mqtt.client as mqtt

mqtt_broker = "localhost"
mqtt_port = 1883
mqtt_topic = "iot_data"

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    process_message(payload)

client = mqtt.Client()
client.on_message = on_message
client.connect(mqtt_broker, mqtt_port, 60)
client.subscribe(mqtt_topic)
client.loop_forever()
