from fastapi import FastAPI
from app.core.config import settings
from app.db.database import engine, Base

# Crear tablas (temporal, luego usar Alembic)
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)


@app.get("/")
async def root():
    """Endpoint de prueba"""
    return {
        "message": "Bienvenido al Sistema de Reservas",
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT
    }
