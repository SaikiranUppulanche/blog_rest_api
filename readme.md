# Blog System Backend (RESTful API)

## Project Description

This project implements a simple blog system backend using Django and Django REST Framework (DRF) with JWT-based user authentication. The backend allows users to register, log in, and perform CRUD operations on blog posts. Users must authenticate using JSON Web Tokens (JWT) to create, update, or delete blog posts.

## Features

- **User Authentication**: Secure registration and login using JWT.
- **Blog Management**: Create, Read, Update, and Delete (CRUD) operations for blog posts.
- **Secure Password Handling**: Passwords are securely stored using hashing techniques.
- **API Endpoints**: Multiple API endpoints for authentication and blog management.
- **Database**: SQLite used as the default database.

## Requirements

- Python 3.x
- Django 4.x
- Django REST Framework
- Simple JWT (for authentication)
- SQLite (or PostgreSQL for production)

## Setup Instructions

Follow the steps below to set up and run the project on your local machine:

### 1. Clone the Repository
```bash
git clone <repository-url>
cd blog_project
```


### 2. Create a Virtual Environment
```bash
python -m venv virtual_env
virtual_env\Scripts\activate 
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
``` bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (optional)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

### The server will run at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## API Documentation

### 1. User Registration
- Endpoint: /api/register/
- Method: POST
- Description: Register a new user.
- Request Body:
```bash
{
  "username": "user1",
  "email": "user@email.com",
  "password": "yourpassword"
}
``` 

### 2. User Login
- Endpoint: /api/login/
- Method: POST
- Description: Log in and retrieve a JWT token.
- Request Body:
```bash
{
  "username": "user1",
  "password": "yourpassword"
}
```
- Response:
```bash
{
  "refresh": "refresh_token",
  "access": "access_token"
}
```

### 3. List Blog Posts
- Endpoint: /api/blogs/
- Method: GET
- Headers: 
```bash
Authorization: Bearer <access_token>
```
- Description: Retrieve a list of all blog posts.
- Authentication Required: Yes (JWT)

- Example Response:

```bash
[
  {
    "id": 1,
    "title": "First Blog",
    "content": "This is the first blog post",
    "author": "user1",
    "timestamp": "2024-10-03T10:25:00Z"
  }
]
```

### 4. Create a Blog Post
- Endpoint: /api/blogs/
- Method: POST
- Headers:
```bash
Authorization: Bearer <access_token>
```
- Description: Create a new blog post.
- Authentication Required: Yes (JWT)

- Request Body:
```bash
{
  "title": "New Blog",
  "content": "This is a new blog post"
}
```

### 5. Retrieve a Specific Blog Post
- Endpoint: /api/blogs/{id}/
- Method: GET
- Headers: 
```bash
Authorization: Bearer <access_token>
```
- Description: Retrieve details of a specific blog post.
- Authentication Required: Yes (JWT)

### 6. Update a Blog Post
- Endpoint: /api/blogs/{id}/
- Method: PUT
- Headers: 
```bash
Authorization: Bearer <access_token>
```
- Description: Update an existing blog post.
- Authentication Required: Yes (JWT)
- Request Body:
```bash
{
  "title": "Updated Blog Title",
  "content": "Updated content"
}
```

### 7. Delete a Blog Post
- Endpoint: /api/blogs/{id}/
- Method: DELETE
- Headers: 
```bash
Authorization: Bearer <access_token>
```
- Description: Delete a blog post.
- Authentication Required: Yes (JWT)
#### Database Schema

##### 1. User
- Fields: username, email, password

##### 2. BlogPost
- Fields:
    - title: Title of the blog post
    - content: Blog post content
    - author: Reference to the User who created the post
    - timestamp: Automatically generated timestamp when the post was created.

#### Security Considerations
- Passwords are securely hashed using Django's User model.
- JWT tokens are used for authentication, with access tokens required to perform CRUD operations on blog posts.
- Ensure secure communication (HTTPS) when deploying in production.

#### Running Unit Tests
- You can run the unit tests using Django’s test runner:
```bash
python manage.py test
```

### Unit tests are provided to validate API functionality, including:

- User registration and login
- Blog post creation and retrieval
- Authentication handling