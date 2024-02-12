FROM python:3.8-alpine

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "/bin/sh" , "docker-entrypoint.sh" ]
