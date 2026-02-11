from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from collections.abc import Generator
from sqlalchemy.orm import Session
from app.core.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass


def get_db() -> Generator[Session, None, None]:
    with SessionLocal() as db:
        yield db
