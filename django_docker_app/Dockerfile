# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the  cotainer
WORKDIR /app

# Install dependecies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#Copy all project files into container
COPY . /app/

#Expose Django's default port
EXPOSE 8000

#Default command to run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]