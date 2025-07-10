# 1. Build stage: install dependencies
FROM python:3.10-slim-bullseye AS builder
WORKDIR /app

# Install essentials

COPY requirements.txt ./

COPY . .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


# Expose Streamlit port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app/main.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
