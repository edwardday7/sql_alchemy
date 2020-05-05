FROM python:3.6-slim

ADD app.py /app

WORKDIR /

RUN pip3 install flask gunicorn flask-sqlalchemy pymysql

CMD exec gunicorn -b :$PORT -w 1 app:app