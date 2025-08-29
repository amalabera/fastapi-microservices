<p align="center">
  <img src="assets/banner.png" alt="FastAPI Microservices" width="800">
</p>

# ⚡ FastAPI Microservices

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)

Scalable backend application built using **FastAPI**, containerized with **Docker**, and ready for deployment on **Kubernetes**.  

---

## 🔑 Highlights
- Modular API endpoints with FastAPI routers  
- Sample **User Service** (demo REST routes)  
- Containerization with Docker  
- Deployment-ready for Kubernetes  

---

## 🛠 Built With
- Python 3.9+  
- FastAPI & Uvicorn  
- Docker / Kubernetes (deployment ready)  

---

## 📦 Getting Started

```bash
 Clone the repository
git clone https://github.com/amalabera/fastapi-microservices.git
cd fastapi-microservices

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload


---
---

## 📸 Demo

### Users Endpoint
Here’s a preview of the `/users/` API response:

![Users API](assets/swagger-users.png)

---

## 🔑 Example Usage

### Using `curl`
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json'





