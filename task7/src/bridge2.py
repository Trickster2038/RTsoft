from kafka import KafkaConsumer
from influxdb import InfluxDBClient
import time
import json

print("kafka -> influx bridge init")

consumer = KafkaConsumer( 
    'cvcoords',
     bootstrap_servers=['localhost:9092'],
     enable_auto_commit=True)

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('cvdata')
client.switch_database('cvdata')
fl = client.query('Delete FROM cv_measurement WHERE time > 0')

# for x in fl:
#     print('x')

# print('Reset table: ' + str(fl))

print("kafka consumer loop init")

while True:
    time.sleep(0.01)
    for message in consumer:
        message = message.value.decode("utf-8") 
        msg_json = json.loads(message)
        json_body = [
        {
        "measurement": "cv_measurement",
        "fields":{
            "x": msg_json['x corrected'],
            "y": msg_json['y corrected']
            }
        }
         ]

        print(json_body)
        flag = client.write_points(json_body)
        print(flag)

        # print(msg_json['x'])