# Overview

This Django REST framework powers the backend API for the AlizadehWatCh Gallery website. The API provides endpoints for managing gallery content, user authentication, and administrative functions.
# Final Product (React used for Frontend)
![image](https://github.com/user-attachments/assets/355ad7d3-3b73-4f48-8d6e-f745d0a73543)

# Installation and Setup
Option 1: Docker Deployment (Recommended)

# Build and start containers in detached mode
    docker-compose up -d --build

# View running containers
    docker-compose ps

# Stop containers
    docker-compose down

The application will be available at:

    API: http://localhost:8000/api/

    Admin: http://localhost:8000/admin/

# Option 2: Local Development Setup

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  in Linux/Mac
OR
.\venv\Scripts\activate  in Windows

1 - Make sure you have PostgreSQL installed. Otherwise, you will have to change the database in the .env file. In order to do this, you have to change the 'DB_ENGINE' to either postgresql or sqlite according to your preference.

2 – Double-click on the sample_env file in the root directory and it will create the .env file. The purpose of this file is to maintain the safety and security of our secret key and other important settings.

Installation and Usage

    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

At http://localhost:8000/api/, you can see the endpoints and the redoc file, which can be used by tools such as Postman to send requests to the relevant endpoints.
Creating a Superuser

    python manage.py createsuperuser

# API Documentation

Interactive API documentation is available at:

    Swagger UI: http://localhost:8000/api/v1/schema/

    ReDoc: http://localhost:8000/api/v1/schema/redoc/
