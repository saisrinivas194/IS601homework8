# Use official Python runtime as a parent image
FROM python:3.12-bullseye

# Set the working directory in the container
WORKDIR /myapp

# Copy the current directory contents into the container at /myapp
COPY . /myapp/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install pytest for testing
RUN pip install pytest

# Expose the port the app will run on (default FastAPI port)
EXPOSE 8000

# Command to run FastAPI app when container starts
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Optionally, default command to run tests if needed (commented out)
# CMD ["pytest"]
