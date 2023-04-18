FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y

RUN pip install -r requirements.txt

RUN pip install protobuf==3.20.0

CMD ["python", "app.py"]