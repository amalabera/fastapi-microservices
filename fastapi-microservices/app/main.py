from fastapi import FastAPI
from app.routers import users

app = FastAPI(title="FastAPI Microservices Demo")

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "FastAPI microservices are running 🚀"}