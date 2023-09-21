# version 1.7 | 22/07/2023
FROM docker.io/oz123/pipenv:3.11-v2023-6-26 AS builder

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

# Pipfile contains requests
ADD Pipfile.lock Pipfile /usr/src/

WORKDIR /usr/src

# Install dependencie
RUN pipenv requirements > requirements.txt

# Copy the application code
COPY . .

# Base image
FROM python:3.11.4-slim-bullseye AS runtime

ENV BORED_API=/home/app/bored_api

# Set the working directory
RUN mkdir -p $BORED_API

WORKDIR $BORED_API

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the application code from the 'builder' stage
COPY --from=builder /usr/src $BORED_API

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Giving the script an executable permissions
RUN chmod +x /home/app/bored_api/entrypoint.sh

# Execute script
ENTRYPOINT ["/home/app/bored_api/entrypoint.sh"]
