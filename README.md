
# Task Tracker Web Application

This is a full-stack task tracking application built with Django (backend) and React (frontend).

## Features

- Create, update, delete, and mark tasks as complete
- List all tasks
- Use REST API to interact between frontend and backend

## Technology Stack

- Backend: Django, Django REST Framework, SQLite
- Frontend: React, Axios
- Others: Bootstrap, Vite

## Setup Instructions

### Backend (Django)
1. Create a virtual environment:
   ```bash
   pipenv shell
     # On Windows
   ```

2. Install dependencies:
   ```bash
   pipenv install django djangorestframework
   ```

3. Run the Django project:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

### Frontend (React)
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React app:
   ```bash
   npm start
   ```

Make sure the backend is running on `http://localhost:8000` and frontend on `http://localhost:3000