# Nginx Reverse Proxy

This repository contains a multi-service project (compose-based) with backend, frontend, and proxy components. It's organized for local development and deployment with Docker Compose.

Overview

- Backend: services in the `backend/` directory
- Frontend: client application in the `frontend/` directory
- Proxy: reverse proxy or gateway in the `proxy/` directory
- Docker Compose: `compose.yaml` config to run the services together

Quick start

1. Install Docker and Docker Compose.
2. From the repository root run:

```bash
docker compose -f compose.yaml up --build
```

3. Visit the frontend or API endpoints as configured in `compose.yaml`.

Development

- To work on the frontend or backend individually, see the respective README or start scripts inside `frontend/` and `backend/`.

Notes for visitors

- This repo is primarily a service composition repository. If you're a recruiter or client: it contains a working example of a small microservices stack that demonstrates local orchestration and deployment.
- No sensitive credentials are stored here in the repository; check `compose.yaml` and environment files for runtime configuration.

License

See project owner for license details.
