FROM ubuntu
COPY src etc/cvexample
RUN apt-get update
# RUN apt-get install -y python3-opencv
# RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt install libgl1-mesa-glx -y
RUN apt install python3-pip -y
RUN pip install opencv-python
CMD python3 etc/cvexample/main.py
