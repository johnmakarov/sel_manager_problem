FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest", "-s", "-vv"]
