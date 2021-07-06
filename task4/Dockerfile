FROM python:3.9.1
RUN apt-get update
ADD src /cvexample
# WORKDIR /cvexample
# RUN apt install -y apparmor apturl
# RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN pip install -r requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir opencv-python
RUN apt-get install ffmpeg libsm6 libxext6  -y
CMD python3 cvexample/main.py
