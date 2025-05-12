# Use python version 3
FROM python:3.9.6

# Set working directory in the container
WORKDIR /app

#copy everything from current folder into the container
COPY  . .

# Install dependencies
RUN pip install -r requirements.txt

# Which port to use
EXPOSE 3500

# Start the app
CMD ["python", "app.py"]
