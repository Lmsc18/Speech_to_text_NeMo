FROM ubuntu:latest

WORKDIR /stt
RUN apt-get update && apt-get install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
run pip install python-multipart
RUN apt-get update && apt-get install -y libsndfile1 ffmpeg
RUN pip install Cython
RUN pip install nemo-asr
RUN pip install --upgrade nemo_toolkit[asr] 
RUN pip3 install -r requirements.txt
ADD ./ /stt

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]