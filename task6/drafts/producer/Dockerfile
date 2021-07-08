FROM ubuntu
RUN mkdir ~/Downloads 
RUN apt-get update -y 
RUN apt-get install curl -y
RUN curl "https://downloads.apache.org/kafka/2.6.2/kafka_2.13-2.6.2.tgz" -o ~/Downloads/kafka.tgz
RUN mkdir ~/kafka && cd ~/kafka && tar -xvzf ~/Downloads/kafka.tgz --strip 1
COPY zookeeper.service /etc/systemd/system/ 
COPY kafka.service /etc/systemd/system/ 
ENTRYPOINT systemctl kafka restart && bash
