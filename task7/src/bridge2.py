from kafka import KafkaConsumer
import time
import json

print("kafka -> influx bridge init")

consumer = KafkaConsumer( 
    'cvcoords',
     bootstrap_servers=['localhost:9092'],
     enable_auto_commit=True)

while True:
    time.sleep(0.01)
    for message in consumer:
        message = message.value.decode("utf-8") 
        print(message)