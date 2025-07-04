# Pixsync

A full-stack project for image processing, deep learning, and GenAI workflows.

---

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Development Workflow](#development-workflow)
- [Adding Dependencies](#adding-dependencies)
- [Environment Variables](#environment-variables)
- [Common Issues](#common-issues)
- [License](#license)

---

## Features
- **Backend:** FastAPI (Python 3.12, Poetry), ready for image processing, deep learning, and GenAI tasks.
- **Frontend:** React (Node.js), served via Docker and Nginx.
- **Dockerized:** Easy orchestration with Docker Compose.
- **Makefile:** One-command startup.

---

## Project Structure
```
backend/
  src/
    main.py
    ...
  Dockerfile
  pyproject.toml
  poetry.lock
frontend/
  src/
    App.js
    index.js
  public/
    index.html
  Dockerfile
  package.json
  .env
Makefile
docker-compose.yml
.gitignore
README.md
```

---

## Prerequisites
- [Docker](https://www.docker.com/get-started) (with Docker Compose)
- [Make](https://www.gnu.org/software/make/) (usually pre-installed on macOS/Linux)
- (Optional) [Poetry](https://python-poetry.org/) for local backend development
- (Optional) [Node.js](https://nodejs.org/) for local frontend development

---

## Setup Instructions
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/pixsync.git
   cd pixsync
   ```

2. **(Optional) Configure environment variables:**
   - Edit `frontend/.env` and `backend/.env` as needed.

3. **Build and run everything with Docker Compose:**
   ```sh
   make run-pixsync
   ```

---

## Running the Application
- **Backend:** [http://localhost:3030](http://localhost:3030)
- **Frontend:** [http://localhost:3031](http://localhost:3031)

---

## Development Workflow

### Backend (Python/FastAPI)
- **Install Poetry dependencies locally:**
  ```sh
  cd backend
  poetry install
  ```
- **Run backend locally:**
  ```sh
  poetry run uvicorn src.main:app --host 0.0.0.0 --port 3030
  ```
- **Add a new Python package:**
  ```sh
  poetry add <package-name>
  poetry lock
  cd ..
  make run-pixsync  # To rebuild Docker image
  ```

### Frontend (React)
- **Install Node dependencies locally:**
  ```sh
  cd frontend
  npm install
  ```
- **Run frontend locally:**
  ```sh
  npm start
  ```
- **Add a new JS package:**
  ```sh
  npm install <package-name>
  cd ..
  make run-pixsync  # To rebuild Docker image
  ```

---

## Adding Dependencies
- **Python (backend):** Use Poetry (`poetry add <package>`) and rebuild Docker.
- **JavaScript (frontend):** Use npm (`npm install <package>`) and rebuild Docker.

---

## Environment Variables
- **Frontend:**
  - `frontend/.env` (e.g., `PORT=3031`)
- **Backend:**
  - Add a `backend/.env` if needed for secrets, API keys, etc.

---

## Common Issues
- **Docker build is slow:** First build downloads large images and dependencies. Subsequent builds are faster.
- **Dependency errors:** If you change `pyproject.toml`, always run `poetry lock` before rebuilding Docker.
- **Missing files:** Ensure required files like `src/index.js` (frontend) and `src/main.py` (backend) exist.
- **node_modules in git:** Never commit `node_modules/`. It's excluded by `.gitignore`.

---

## License
MIT (or your license here)
