FROM python:3.11.3-slim-bullseye

WORKDIR /src

RUN pip3 install --upgrade pip

COPY ../back/requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

RUN apt-get update

COPY ../back .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--forwarded-allow-ips", "'*'"]