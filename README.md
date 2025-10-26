# tutedude_devops_docker

# Express (frontend) + Flask (backend) with Docker


## What is included
- Frontend: Node.js + Express serving a form (`/`) that posts JSON to the Flask backend.
- Backend: Flask app with `/submit` that accepts the data and returns JSON.
- Dockerfiles for frontend and backend and a `docker-compose.yml` that brings them up on the same network.


## Quick local dev
- Start backend locally: `cd backend && python app.py` (port 5000)
- Start frontend locally: `cd frontend && npm install && npm start` (port 3000)


## Docker Compose
1. Edit `docker-compose.yml` and replace `YOUR_DOCKERHUB_USERNAME` with your Docker Hub username (optional if you only build locally).
2. Build and run:
```bash
docker-compose up --build
