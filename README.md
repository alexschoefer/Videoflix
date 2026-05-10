# 🎬 Videoflix

A modern video streaming backend inspired by Netflix — built with Django REST Framework, Docker, and FFmpeg.

Videoflix is a backend-focused streaming platform that combines scalable API architecture with video processing and media streaming workflows.

The project is built with Django REST Framework and designed to integrate with a separately developed frontend application.

---

## 📚 Table of Contents

- [Tech Stack](#-tech-stack)
- [Features](#-features)
- [API Endpoints](#-api-endpoints)
- [Architecture](#-architecture)
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

## ✨ Features

- 🔐 User registration & authentication
- 📧 Email account activation
- 🔑 JWT-based authentication & token refresh
- 🔒 Password reset workflow
- 🎥 Video upload & streaming
- ⚡ Automated video processing with FFmpeg
- 📡 REST API powered by Django REST Framework
- 🎞️ HLS video streaming support
- 🐳 Dockerized development & deployment
- 📂 Modular Django application structure
- ☁️ Production-oriented backend architecture
- 📱 Designed for external frontend integration

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

## 📄 License

This project is licensed under the MIT License — © 2026 Alex Schöfer.