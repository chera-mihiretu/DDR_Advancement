# Use the official Python 3.12 slim Bookworm image as the base
FROM python:3.12-slim-bookworm

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install pip if it's not already installed
RUN apt-get update && apt-get install -y \
    python3-pip \
    build-essential \
    libpq-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN python3 -m pip install --upgrade pip

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install dependencies from requirements.txt into the container's Python environment
RUN pip install -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Collect static files (if you're using Django)
RUN python3 manage.py collectstatic --noinput

# Expose port 8000 to be able to access the app
EXPOSE 8000

# Set the default command to run the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
