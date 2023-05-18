FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

RUN chmod +x ./src/MainScores.py

CMD [ "./src/MainScores.py" ]
