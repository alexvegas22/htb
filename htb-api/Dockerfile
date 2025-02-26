# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY requirements.txt .

# Set environment variables for Redis
ENV REDIS_HOST=redis://redis-htb-service
ENV REDIS_PORT=6379

# Create a virtual environment and install dependencies
RUN python -m venv .venv && \
    . .venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port that the app will run on
EXPOSE 5000

# Command to run the application
CMD ["sh", "-c", ". .venv/bin/activate && gunicorn -w 4 -b 0.0.0.0:5000 app.app:app"]
