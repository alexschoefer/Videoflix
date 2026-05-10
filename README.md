# 🎬 Videoflix

A modern video streaming backend inspired by Netflix — built with Django REST Framework, Docker, and FFmpeg.

Videoflix is a backend-focused streaming platform that combines scalable API architecture with video processing and media streaming workflows.

The project is built with Django REST Framework and designed to integrate with a separately developed frontend application.

---

## 📚 Table of Contents

- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Features](#-features)
- [Video Streaming Pipeline](#-video-streaming-pipeline)
- [API Endpoints](#-api-endpoints)
- [JWT Authentication](#-jwt-authentication)
- [Security](#-security)
- [Architecture](#-architecture)
- [Docker Setup](#-docker-setup)
- [Getting Started](#getting-started)
- [Environment Variables](#-environment-variables)
- [License](#-license)

---

## 🛠️ Tech Stack

- **Python 3.12**
- **Django 6**
- **Django REST Framework** — RESTful API development
- **PostgreSQL** — Primary database
- **Redis** — Caching & background task broker
- **Django-RQ** — Background job processing
- **FFmpeg** — Video transcoding & HLS generation
- **Docker & Docker Compose** — Containerized deployment

---

## 📁 Project Structure

```bash
Videoflix/
│
├── auth_app/                     # Authentication & user management
├── video_app/                    # Video processing & streaming logic
├── core/                         # Django core configuration
├── media/                        # Uploaded & processed video files
├── static/                       # Static assets
│
├── backend.entrypoint.sh
├── backend.Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── .env.template
```

---

## ✨ Features

- 🔐 User registration & authentication
- 📧 Email account activation
- 🔑 JWT-based authentication & token refresh
- 🔒 Password reset workflow
- 🎥 Video upload & streaming
- ⚡ Automated video processing with FFmpeg
- 📡 REST API powered by Django REST Framework
- 🎞️ HLS video streaming support (480p, 720p, 1080p)
- 🐳 Dockerized development & deployment
- 📂 Modular Django application structure
- ☁️ Production-oriented backend architecture
- 📱 Designed for external frontend integration

---

## 🎞️ Video Streaming Pipeline

Uploaded videos are automatically processed using FFmpeg.

The processing pipeline includes:

1. Video upload
2. FFmpeg transcoding
3. HLS playlist generation
4. Segment creation
5. Stream delivery via API endpoints

Supported streaming format:

- HLS (`.m3u8`)

---

## 📡 API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/register/` | Register a new user |
| GET | `/api/activate/<uidb64>/<token>/` | Activate user account |
| POST | `/api/login/` | User login |
| POST | `/api/logout/` | User logout |
| POST | `/api/token/refresh/` | Refresh JWT token |
| POST | `/api/password_reset/` | Request password reset |
| GET | `/api/password_confirm/<uidb64>/<token>/` | Confirm password reset |

---

### Video Streaming

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/video/` | List all videos |
| GET | `/api/video/<movie_id>/<resolution>/index.m3u8` | HLS manifest |
| GET | `/api/video/<movie_id>/<resolution>/<segment>/` | HLS segment file |

---

## 🔐 JWT Authentication

Videoflix uses JWT-based authentication for secure API access.

### Flow:

1. User registers via `/api/register/`
2. Email verification is required
3. Login returns:
   - Access Token
   - Refresh Token
4. Access token is used for protected endpoints
5. Refresh token is used to obtain a new access token

### Token Usage Example:

```http
Authorization: Bearer <access_token>
```

---

## 🔒 Security

Videoflix implements multiple security layers:

- 🔐 JWT authentication for API access
- 📧 Email verification for new accounts
- 🔁 Secure password reset workflow
- 🌐 CORS configuration for frontend communication
- 🛡️ CSRF protection enabled
- 🔑 Environment-based secret management (`.env`)
- 🚫 No sensitive data stored in source code

---

## 🏗️ Architecture

Videoflix follows a modular backend architecture designed for scalable media streaming workflows.

Core components include:

- Django REST Framework API
- PostgreSQL database
- Redis-based background task queue
- FFmpeg video transcoding pipeline
- HLS streaming generation
- Dockerized development environment

---

## 🐳 Docker Setup

Start all services:

```bash
docker compose up --build
```

Run database migrations:

```bash
docker compose exec backend python manage.py migrate
```

Create superuser:

```bash
docker compose exec backend python manage.py createsuperuser
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/alexschoefer/Videoflix.git
cd Videoflix
```

### 2. Environment Variables

Create a `.env` file based on `.env.template`.

```bash
cp .env.template .env
```

Example configuration:

```env
# (unchanged from your version)
```

---

## ⚙️ Environment Variables

All required environment variables are defined in `.env.template`.

Key categories:

- Django configuration
- Database settings
- Redis configuration
- Email backend
- Frontend integration URLs

---

## 🎯 Project Highlights

- Fully asynchronous video processing pipeline
- Scalable HLS streaming architecture
- Production-ready Docker setup
- Clean modular Django design
- External frontend integration support

---

## 📄 License

This project is licensed under the MIT License — © 2026 Alex Schöfer.