FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt /app
COPY api/ /app/api

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]
