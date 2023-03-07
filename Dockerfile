

FROM python:3.10.8



WORKDIR /app

COPY requirements.txt .


RUN apt-get update && apt-get install -y libmysqlclient-dev && pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8080

CMD [ "python", "app.py" ]
