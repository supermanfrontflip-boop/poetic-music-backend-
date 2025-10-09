# Use a smaller base image
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn openai transformers torch

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"] 