# Use a smaller base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install only minimal dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port for Railway
EXPOSE 8080
CMD ["node", "server.js"]

# Start server
CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "8080"]
