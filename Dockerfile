# Start with a base Python image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install NLTK data during Docker build
RUN python -m nltk.downloader punkt

# Copy the rest of your application code
COPY . .

# Expose the port Gunicorn will run on
EXPOSE 8000

# Finally, run Gunicorn with the WSGI application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "run:app"]
