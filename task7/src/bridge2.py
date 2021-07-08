from kafka import KafkaConsumer
import time

print("kafka -> influx bridge init")

consumer = KafkaConsumer( 
    'cvcoords',
     bootstrap_servers=['localhost:9092'],
     enable_auto_commit=True,
     group_id='my-group')

while True:
    time.sleep(0.01)
    for message in consumer:
        message = message.value
        print(str(message))