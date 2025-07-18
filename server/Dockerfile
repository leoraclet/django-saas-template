# This Dockerfile is designed for a multi-stage build
# of a Django application with a Svelte + Vite frontend.
#
# Stage 1: Build the Svelte + Vite app
# - Uses the official Node.js LTS image to build the frontend.
# - Installs dependencies and builds the frontend assets.
#
# Final Image
# - Uses the official Python 3.12.4 slim image as the base.
# - Sets environment variables to optimize Python behavior.
# - Installs system dependencies and Python packages from requirements.txt.
# - Creates necessary directories for static files, media, and logs.
# - Copies entrypoint and start scripts, ensuring they are executable.
# - Sets the entrypoint to the entrypoint.sh script for container execution.

# Stage 2: Build the Svelte + Vite app
FROM node:lts AS build-svelte

WORKDIR /app

COPY --from=parent ./frontend/package*.json .

RUN npm install

COPY --from=parent ./frontend .

RUN npm run build

#####################################################
# Runtime stage for serving the django application
#####################################################

# Pull official base image
FROM python:3.12.4-slim-bullseye

# Set work directory and user
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/app

# Copy frontend build
COPY --from=build-svelte /app/dist ${APP_HOME}/frontend/

# Install system dependencies
RUN apt-get update && apt-get install -y netcat
RUN apt-get autoremove --purge && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY --from=parent ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Create diretories
RUN mkdir -p ${APP_HOME}/staticfiles
RUN mkdir -p ${APP_HOME}/media
RUN mkdir -p ${APP_HOME}/logs

# Copy entrypoint.sh and make it executable
COPY entrypoint.sh entrypoint.sh
RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

# Copy start scripts and make them executable
COPY --from=parent docker/start-django /start-django
RUN sed -i 's/\r$//g' /start-django
RUN chmod +x /start-django

COPY --from=parent docker/start-celery-beat /start-celery-beat
RUN sed -i 's/\r$//g' /start-celery-beat
RUN chmod +x /start-celery-beat

COPY --from=parent docker/start-celery-worker /start-celery-worker
RUN sed -i 's/\r$//g' /start-celery-worker
RUN chmod +x /start-celery-worker

COPY --from=parent docker/start-celery-flower /start-celery-flower
RUN sed -i 's/\r$//g' /start-celery-flower
RUN chmod +x /start-celery-flower

# Run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
