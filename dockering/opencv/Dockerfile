FROM debian:latest

WORKDIR /app

COPY 01-abrir_camara.py .

RUN apt update -y && apt upgrade -y && apt install -y python3 && apt install -y python3-opencv

CMD ["python3","01-abrir_camara.py"]

CMD ["tail", "-f", "/dev/null"]
