FROM alpine:3.4
RUN apk update 
# RUN apk add py3-pip
RUN apk --no-cache --update-cache add python python-dev py-pip
RUN pip install --upgrade pip
RUN pip install --no-cache-dir opencv-python
ADD src /etc/exercise1
CMD python3 main.py
