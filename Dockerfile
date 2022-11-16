FROM python:3.10

RUN mkdir /usr/src/bot
WORKDIR /usr/src/bot
COPY . .
COPY requirements.txt ./


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TOKEN="5727015611:AAHt4kqyFU9Sw1xDPC7IktOtoM1fiAQHUcU"

RUN  apt-get update && apt-get install sqlite3

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN /usr/bin/sqlite3 /usr/src/bot/db/anglo_bot.db


# copy project
ENTRYPOINT ["python", "main.py"]
