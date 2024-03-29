# Deploy with Docker

# could change python version later
FROM python:3.9-slim

# defining workspace
WORKDIR /app

# adding non-root for security
RUN adduser loluser
USER loluser

# install the dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# coping the other files
COPY . /app

# run the main file
CMD ["python3", "openleague/main.py"]