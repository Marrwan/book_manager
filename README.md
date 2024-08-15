# Book Manager

## Overview

Book Manager is a web application that allows you to manage books through a RESTful API. The backend is built using Django and Django REST Framework, while the frontend is powered by React.

## Prerequisites

- Node.js
- Python 3
- Django

## Getting Started

Follow the steps below to set up the project.

### 1. Clone the Repository

```bash
git clone https://github.com/Marrwan/book_manager.git

cd book-manager
```

2. Install Frontend Dependencies
Navigate to the project root and install the necessary Node.js packages:

```bash
npm install
```

3. Start the Frontend Server
```bash
npm start
```
4. Set Up the Backend Environment
Navigate to the backend folder:

```bash
cd bookmanager
```
Create a Python virtual environment:

```bash
python -m venv venv
```
Activate the virtual environment:

```bash
source venv/bin/activate
````
5. Install Backend Dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```
6. Create Migrations and Migrate
Apply the database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```
7. Run the Backend Server
Start the Django development server:

```bash
python manage.py runserver
```
8. Access the Frontend
You can access the frontend at:
```arduino
http://localhost:3000
```
9. API Configuration
If you change the backend port, you will need to modify the API_URL in the bookApi.js file inside the api folder of the frontend app.

10. API Documentation
API documentation is available at:

```bash
http://localhost:8000/api/docs
```

Available Endpoints:

- `GET /api/books/:` List all books.
- `POST /api/books/:` Create a new book.
- `GET /api/books/{id}/:` Get details of a specific book.
- `PUT /api/books/{id}/:` Update a specific book.