# Start with a base Python image
FROM python:3.9-slim

# By default, listen on port 8000
EXPOSE 8000/tcp

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY run.py .

# Specify the command to run on container start
CMD [ "python", "run.py" ]

