# Use a slim Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependencies list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the codebase
COPY . .

# Run Django development server
CMD ["python", "My_Django_Project/manage.py", "runserver", "0.0.0.0:8000"]

# Expose port 8000 for access
EXPOSE 8000