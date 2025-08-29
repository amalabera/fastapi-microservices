from fastapi import FastAPI
from app.routers import users

app = FastAPI(
    title="FastAPI Microservices",
    docs_url="/docs",       # Swagger UI
    redoc_url="/redoc"      # ReDoc UI
)

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "FastAPI microservices are running 🚀"}
