FROM czentye/opencv-video-minimal
# RUN apt-get update
# WORKDIR /cvexample
# RUN apt install -y apparmor apturl
# RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN pip install -r requirements.txt
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir opencv-python
# RUN apt-get install ffmpeg -y
# RUN apt-get install libsm6 -y
# RUN apt-get install libxext6  -y
ADD src /cvexample
CMD python3 cvexample/main.py
