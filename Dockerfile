FROM python:3.10.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update \
    && apt-get install -y mariadb-client libmariadb-dev-compat \
    && pip install --no-cache-dir -r requirements.txt
COPY . /code/
