# pull official base image
FROM python:3.12-slim

# set work directory
WORKDIR /src/project/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# Install Poetry and dependencies
RUN pip install --upgrade pip
RUN pip install django psycopg2-binary strawberry-graphql-django 
COPY pyproject.toml poetry.lock /src/project/
RUN pip install --no-cache-dir poetry \
    && poetry install --no-root --no-dev

# Copy project files
COPY . /src/project/

# Run the application (you can adjust the command as needed)
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
