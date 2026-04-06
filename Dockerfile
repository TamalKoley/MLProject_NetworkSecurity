FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app .
COPY Final_Models ./Final_Models/
COPY networksecurity ./networksecurity/

EXPOSE 10222

CMD [ "python", "app.py" ]