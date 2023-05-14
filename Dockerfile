FROM python:3.10-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8777

ENTRYPOINT [ "python" ]

CMD [ "src/main_scores.py" ]