# FastAPI_ToDo_API

A simple, yet powerful ToDo API built with FastAPI. This project provides a robust backend for managing tasks and users, making it an ideal starting point for developers looking to learn or build upon.

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)] [![License](https://img.shields.io/github/license/PartORG/FastAPI_ToDo_API)] [![Tests](https://img.shields.io/github/actions/workflow/status/PartORG/FastAPI_ToDo_API/tests.yml?branch=main)] [![Framework](https://img.shields.io/badge/framework-FastAPI-green.svg)]

## Introduction

FastAPI_ToDo_API is a simple yet comprehensive ToDo API built using the FastAPI framework. It includes models, routers for different functionalities (admin, auth, todos, users), and tests for various components. This project serves as an excellent starting point for developers looking to learn or build upon.

The primary workflow of this project involves setting up the database, running migrations, and starting the API server. The main advantages of this project include its simplicity, robustness, and ease of use.

## Features

### Simple API Written in FastAPI

- **What it does:** Provides a simple ToDo API with functionalities for managing tasks and users.
- **Why it exists:** To serve as an educational tool and a starting point for building more complex applications.
- **Why it is useful:** Ideal for developers looking to learn or build upon.

## How It Works

The project follows a typical FastAPI workflow, including setting up the database, running migrations, and starting the API server. Below is a high-level overview of the architecture:

```plaintext
+-------------------+
|    Database       |
+---------+---------+
          |
          v
+---------+---------+
|   Migrations  |
+---------+---------+
          |
          v
+---------+---------+
|     FastAPI     |
+---------+---------+
          |
          v
+---------+---------+
|   Routers     |
| (admin, auth, todos, users) |
+-------------------+
```

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.x | The programming language used for development. |
| FastAPI    | A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. |
| SQLAlchemy | An SQL toolkit and Object-Relational Mapping (ORM) system for Python. |
| Alembic    | Database migration tool for SQLAlchemy. |
| Pytest     | A mature full-featured Python testing tool. |

## Requirements

To run this project, you will need:

- Python 3.x
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

4. Run migrations:
   ```sh
   alembic upgrade head
   ```

5. Start the API server:
   ```sh
   uvicorn todo_app.main:app --reload
   ```

## Configuration

The project uses environment variables for configuration. Below are some of the observed environment variables:

- `DATABASE_URL`: The URL of the database.
- `SECRET_KEY`: A secret key used for authentication.

## Quick Start

Here is a realistic example of how to use the API:

1. **Create a new task:**
   ```sh
   curl -X POST "http://127.0.0.1:8000/todos/" -H "Content-Type: application/json" -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
   ```

2. **Get all tasks:**
   ```sh
   curl -X GET "http://127.0.0.1:8000/todos/"
   ```

3. **Authenticate a user:**
   ```sh
   curl -X POST "http://127.0.0.1:8000/auth/login" -H "Content-Type: application/json" -d '{"username": "user", "password": "pass"}'
   ```

## Usage

Below are some actual commands, entry points, and examples discovered in the repository:

- **Run migrations:**
  ```sh
  alembic upgrade head
  ```

- **Start the API server:**
  ```sh
  uvicorn todo_app.main:app --reload
  ```

## Project Structure

```plaintext
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

The development workflow involves setting up the database, running migrations, and starting the API server. The project uses FastAPI's built-in support for testing with Pytest.

## Testing

This project includes tests for various components:

- **Admin functionality**
- **Authentication**
- **Todos**
- **Users**

To run the tests:
```sh
pytest
```

## Limitations

- This is a simple example and may not cover all edge cases.
- The database schema is basic and can be extended as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.