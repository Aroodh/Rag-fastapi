from fastapi import FastAPI

from app.core.database import Base, engine
import app.models

from app.routers.auth import router as auth_router
from app.routers.documents import router as document_router

app = FastAPI(
    title="RAG Backend",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(document_router)


@app.get("/")
def home():
    return {
        "message": "RAG Backend Running Successfully"
    }   