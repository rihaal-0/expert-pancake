# Use official Python image
FROM python:3.10-slim

# Install FFmpeg and other dependencies
RUN apt update && apt install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot code
COPY main.py .

# Use environment variables from .env
ENV PYTHONUNBUFFERED=1

# Start the bot
CMD ["python", "main.py"]
