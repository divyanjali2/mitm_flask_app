# Use a small official Python image
FROM python:3.11-slim

# Install build tools only if needed for dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create and switch to app directory
WORKDIR /app

# Install Python dependencies first (for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose the port Gunicorn will listen on
EXPOSE 8000

# Start Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
