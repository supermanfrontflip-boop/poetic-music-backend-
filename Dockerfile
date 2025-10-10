FROM python:3.10-slim

WORKDIR /app
COPY . /app

# Install only lightweight dependencies first
RUN pip install --no-cache-dir fastapi uvicorn openai transformers==4.33.0 --extra-index-url https://download.pytorch.org/whl/cpu

# Skip installing full torch GPU
RUN pip install --no-cache-dir torch==2.0.1+cpu

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]