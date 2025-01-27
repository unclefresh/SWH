FROM python:3.9-buster

# Install curl
RUN apt-get update && apt-get install -y curl

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Run the application with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "--timeout", "120", "app:app"]
