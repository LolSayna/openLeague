# Deploy with Docker

# could change python version later
FROM python:3.9-slim

# put everything exect dockerignore into the app folder
WORKDIR /app
COPY . /app

# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# run the main file
CMD ["python3", "src/main.py"]