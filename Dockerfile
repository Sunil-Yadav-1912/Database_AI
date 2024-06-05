# Use the official Python image from the Docker Hub with version 3.11.7
FROM python:3.11.7-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 5000

# Specify the command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
