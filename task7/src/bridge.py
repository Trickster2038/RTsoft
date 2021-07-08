import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import time

mqtt_broker = "localhost"
mqtt_client = mqtt.Client("BridgeMQTT2Kafka")
mqtt_client.connect(mqtt_broker)

kafka_client = KafkaClient(hosts="localhost:9092")
kafka_topic = kafka_client.topics['cvcoords']
kafka_producer = kafka_topic.get_sync_producer()

def on_message(client, userdata, message):
    msg_payload = str(message.payload)
    print("Received MQTT message: ", msg_payload)
    kafka_producer.produce(msg_payload.encode('ascii'))
    print("KAFKA: Just published " + msg_payload + "cvcoords")

mqtt_client.subscribe("cvtrack")
mqtt_client.on_message = on_message

print("MQQT loop init")
mqtt_client.loop_forever()


# time.sleep(1)
# mqtt_client.loop_end()