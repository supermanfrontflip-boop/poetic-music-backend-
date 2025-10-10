FROM python:3.10

WORKDIR /app
COPY . /app

# install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir fastapi uvicorn openai
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir transformers==4.33.0

# expose port 8080 for Railway
EXPOSE 8080

# start the app
CMD ["python", "main.py"]