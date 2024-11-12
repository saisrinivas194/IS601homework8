
# IS601 Homework 8 - FastAPI Project

## Description
This repository contains the FastAPI implementation for IS601 Homework 8, which includes a simple FastAPI application with multiple components like routers, services, utilities, and models.

## Repository Structure

### Directories
- **app**: Contains FastAPI application components such as routers, services, and utilities.
- **tests**: Contains test files for the application.
- **utils**: Contains utility functions.
- **qr_codes**: Contains generated QR code images.

### Files
- **Dockerfile**: Docker configuration to containerize the application.
- **.gitignore**: Specifies which files and directories should be ignored by Git.
- **.dockerignore**: Specifies which files should be ignored by Docker.
- **requirements.txt**: Lists dependencies required to run the application.
- **pytest.ini**: Pytest configuration file.
- **main.py**: The entry point of the FastAPI application.
- **production.yml**: GitHub Actions configuration for CI/CD.
- **test.py**: A sample test file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/saisrinivas194/IS601-homework8.git
    cd IS601-homework8
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the FastAPI app locally:

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Running Tests

To run tests using pytest:

```bash
pytest
```

## Docker

To build and run the application in a Docker container:

1. Build the Docker image:

    ```bash
    docker build -t fastapi-app .
    ```

2. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 fastapi-app
    ```

The application will be available at `http://localhost:8000` within the Docker container.

## CI/CD

This project includes a GitHub Actions CI/CD pipeline for automated testing and deployment.
