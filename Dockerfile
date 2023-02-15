FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN apt-get update && apt install awscli -y && pip install -r requirements.txt && apt-get install -y poppler-utils && apt install tesseract-ocr -y && apt-get install python3-opencv -y

CMD ["python3", "app.py"]