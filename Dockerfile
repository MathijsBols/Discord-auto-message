# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir requests logger

# Set environment variable for config file location (default to /app/config.json)
ENV CONFIG_PATH=/app/config.json

# Run the Python script when the container launches
CMD ["python", "./message.py"]
