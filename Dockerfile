FROM python:3.11-slim

WORKDIR /app

# Install fastmcp
RUN pip install --no-cache-dir fastmcp

# Copy the server file
COPY server.py .

# Ensure unbuffered output for stdio (IMPORTANT for MCP)
ENV PYTHONUNBUFFERED=1

# Run the server
CMD ["python", "server.py"]