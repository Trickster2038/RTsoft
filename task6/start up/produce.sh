#!/bin/bash
echo 'begin sending 1 message per second'
while true
do
  echo "Hello World from Astakhov Sergey!" | /home/kafka/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic TutorialTopic > /dev/null
  sleep 3
done

