FROM python
COPY . .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /app
WORKDIR /app
COPY . .
CMD python src/MainScores.py
