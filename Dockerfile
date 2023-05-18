FROM python:3.6

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

RUN chmod +x ./src/MainScores.py

CMD [ "./src/MainScores.py" ]
