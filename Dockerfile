FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir fastapi uvicorn

EXPOSE 8080

CMD ["python", "main.py"]