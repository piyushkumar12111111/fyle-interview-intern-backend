# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=core/server.py
ENV FLASK_ENV=production

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app

# Expose port 5000
EXPOSE 5000

# Run database migrations externally if needed
# CMD ["flask", "db", "upgrade", "-d", "core/migrations/"]

# Start the application
CMD ["bash", "run.sh"]
