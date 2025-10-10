# Use the official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source files
COPY . .

# Expose port (Railway sets PORT dynamically)
EXPOSE 8000

# Run the app (expand environment variable properly)
CMD exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}