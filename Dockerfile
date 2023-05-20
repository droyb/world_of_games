WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8777

RUN chmod +x src/MainScores.py

COPY Scores.txt /Scores.txt

CMD [ "python", "/app/src/MainScores.py" ]
