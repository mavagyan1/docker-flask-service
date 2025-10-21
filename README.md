# Dockerized Flask Service 🐳

A small, fun Python Flask web service running inside Docker!  
Each visit returns colorful JSON messages with emojis and fun tips.  
Optionally, visit `/html` to see a vibrant HTML page with random backgrounds and emojis! 🌈

## Features

- Returns **JSON messages** with fun, randomized content 🎉
- Prints **colorful logs** in the terminal for easy monitoring
- Optional `/html` endpoint for a visually exciting page 🖼️
- Lightweight and portable with Docker

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/get-started) installed on your machine


### Pull the image from Docker Hub
Build and run the image locally:
```bash
docker pull maneav/my_flask_service:latest
docker run -d -p 5000:5000 maneav/my_flask_service
# Visit http://localhost:5000 for JSON
# or http://localhost:5000/html for HTML
