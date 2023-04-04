FROM python:3.8.16

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Download and install the missing package from another source
RUN pip install -U pip setuptools wheel

RUN python -m nltk.downloader stopwords

RUN python -m spacy download en_core_web_sm

RUN python -m spacy download es_core_news_sm

RUN python -m nltk.downloader punkt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["python", "app.py"]

#docker run -d -p 8000:8000 flask-nlp-app to see the app


