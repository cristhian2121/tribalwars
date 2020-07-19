FROM python:3.6.10

WORKDIR /app

COPY . .

RUN pip install selenium

CMD [ "python", "./main.py" ]