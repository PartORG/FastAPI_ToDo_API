# FastAPI_ToDo_API

A simple, yet powerful API built with FastAPI to manage your daily tasks efficiently. With its intuitive design and robust features, this project aims to provide a seamless experience for developers looking to integrate task management into their applications.

## Table of Contents
1. [Features](#features)
2. [How It Works](#how-it-works)
3. [Technology Stack](#technology-stack)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [Quick Start](#quick-start)
8. [Usage](#usage)
9. [Project Structure](#project-structure)
10. [Development](#development)
11. [Testing](#testing)
12. [Limitations](#limitations)
13. [License](#license)

## Features
### Task Management
- **Create Tasks**: Easily add new tasks with a simple API endpoint.
- **Update Tasks**: Modify existing tasks to reflect changes in status or details.
- **Delete Tasks**: Remove completed or unnecessary tasks from your list.

### User Authentication
- **User Registration**: Securely register new users with email and password.
- **Login/Logout**: Manage user sessions for secure access to task management features.

### Role-Based Access Control (RBAC)
- **Admin Panel**: Provide an admin interface to manage users, roles, and permissions.

## How It Works
FastAPI_ToDo_API leverages FastAPI's modern Python framework to create a high-performance API. The application is structured into several key components:

1. **Routers**: Define the endpoints for task management, authentication, and user management.
2. **Models**: Represent the data structure of tasks and users using Pydantic models.
3. **Database**: Manage database operations using SQLAlchemy with Alembic for migrations.

## Technology Stack
| Technology | Purpose |
|------------|---------|
| Python     | The primary programming language. |
| FastAPI    | A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. |
| SQLAlchemy | An SQL toolkit and Object-Relational Mapping (ORM) system for Python. |
| Alembic      | Database migration tool for SQLAlchemy applications. |
| Pydantic     | Data validation and settings management using Python type annotations. |
| pytest       | A mature full-featured Python testing tool. |

## Requirements
To run FastAPI_ToDo_API, you need the following:

- Python 3.7 or higher
- pip (Python package installer)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/PartORG/FastAPI_ToDo_API.git
   cd FastAPI_ToDo_API
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```sh
   alembic upgrade head
   ```

5. Run the application:
   ```sh
   uvicorn todo_app.main:app --reload
   ```

## Configuration
The application can be configured using environment variables. The following variables are commonly used:

- `DATABASE_URL`: The URL of the database (e.g., `sqlite:///testdb.db`).
- `SECRET_KEY`: A secret key for JWT authentication.

These variables can be set in a `.env` file or directly in your operating system's environment variables.

## Quick Start
Here’s how you can quickly get started with FastAPI_ToDo_API:

1. **Create a new task**:
   ```sh
   curl -X POST "http://127.0.0.1:8000/todos" -H "Content-Type: application/json" -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
   ```

2. **List all tasks**:
   ```sh
   curl -X GET "http://127.0.0.1:8000/todos"
   ```

3. **Update a task**:
   ```sh
   curl -X PUT "http://127.0.0.1:8000/todos/1" -H "Content-Type: application/json" -d '{"title": "Buy groceries", "description": "Milk, eggs, bread", "completed": true}'
   ```

4. **Delete a task**:
   ```sh
   curl -X DELETE "http://127.0.0.1:8000/todos/1"
   ```

## Usage
To interact with the API, you can use tools like `curl`, Postman, or any other HTTP client.

### Example Commands
- **Create a new task**:
  ```sh
  curl -X POST "http://127.0.0.1:8000/todos" -H "Content-Type: application/json" -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
  ```

- **List all tasks**:
  ```sh
  curl -X GET "http://127.0.0.1:8000/todos"
  ```

## Project Structure
```
FastAPI_ToDo_API/
├── books.py
├── testdb.db
├── todo_app/
│   ├── __init__.py
│   ├── alembic.ini
│   ├── alembic/
│   │   ├── README
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions/
│   │       └── 790af12feaff_create_phone_number_for_user_column.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── auth.py
│   │   ├── todos.py
│   │   └── users.py
│   └── test/
│       ├── __init__.py
│       ├── test_admin.py
│       ├── test_auth.py
│       ├── test_example.py
│       ├── test_main.py
│       ├── test_todos.py
│       ├── test_user.py
│       └── utils.py
```

## Development
FastAPI_ToDo_API is designed for easy development and testing. The project includes a comprehensive set of tests using `pytest`. To run the tests, simply execute:

```sh
pytest
```

## Testing
The application comes with a suite of tests to ensure functionality. You can run these tests using `pytest`:

```sh
pytest
```

## Limitations
- **Database**: The current implementation uses SQLite for simplicity. For production environments, consider using more robust databases like PostgreSQL or MySQL.
- **Authentication**: Basic JWT authentication is implemented. For a production system, consider integrating with OAuth2 or other secure authentication mechanisms.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.