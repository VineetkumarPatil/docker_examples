
# Using official python runtime base image
FROM python:3.7-alpine

# Set the application directory
RUN mkdir -p /flask_app/app
WORKDIR /flask_app/app

# Copy our code from the current folder to /app inside the container
COPY . /flask_app/app

# Install our requirements.txt
RUN pip install -r requirements.txt

EXPOSE 20001

# Define our command to be run when launching the container
CMD ["gunicorn", "driver:app", "-b", "0.0.0.0:20001", "--workers", "4", "--keep-alive", "0"]

