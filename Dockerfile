FROM python:3.7

RUN adduser --disabled-password flask_app

WORKDIR /home/flask_app

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY models models
COPY preprocess preprocess
COPY templates templates
COPY flask_app.py boot.sh libs.py ./
RUN chmod +x boot.sh

ENV FLASK_APP flask_app.py

RUN chown -R flask_app:flask_app ./
USER flask_app

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]