# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project code to the working directory
COPY . .

# Set environment variables
ENV DJANGO_SETTINGS_MODULE usergallery.settings

# Expose the port that Django runs on
EXPOSE 8000

# Run the Django migrations
RUN python manage.py migrate

# Install Node.js and package dependencies
# FROM node:14.17.0-alpine3.13
# COPY package.json .
# RUN npm install

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
