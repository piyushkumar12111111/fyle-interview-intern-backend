FROM python:3.8-slim

# Set the working directory  
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Set environment variables for Flask
ENV FLASK_APP=core/server.py
ENV FLASK_ENV=production

# Ensure run.sh has execute permissions
RUN chmod +x /app/run.sh
RUN chmod +x /app/run_tests.sh  # Add this line to ensure the test script has execute permissions

# Expose the port Flask will run on
EXPOSE 5000

# Run the script to start the application
CMD ["chmod", "+x", "bash", "run.sh"]
