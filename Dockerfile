# deploy with Docker
FROM python:3.9-slim


ADD /src/main.py .

#WORKDIR /app
#COPY . /app

# RUN pip install requests
RUN pip install requests

# pip warnings: running as root-> create user, upgrading pip version

CMD ["python3", "main.py"]