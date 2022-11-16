FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN apt-get update && \
    apt-get install -y zlib1g-dev && \
    rm -rf /var/lib/apt/lists/* 

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]