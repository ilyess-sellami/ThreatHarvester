# -------------------------------
# Threat Harvester Dockerfile
# -------------------------------

# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and app files
COPY requirements.txt .
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose the app port
EXPOSE 8000

# Ensure .env is copied
# It should be in the same folder as Dockerfile or mounted as a volume

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
