FROM python:latest

WORKDIR /app

# Upgrade system packages & Install required tools
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y git ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements and install python dependencies first (Fast Caching)
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Start the bot
CMD ["python3", "bot.py"]
