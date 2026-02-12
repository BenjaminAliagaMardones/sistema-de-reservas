from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey,
    CheckConstraint, UniqueConstraint, Index, Boolean, Text
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class Negocio(Base):
    __tablename__ = "negocios"

    __table_args__ = UniqueConstraint("slug", name="uq_negocio_slug"),
    CheckConstraint("char_lenght(nombre) > 0", name="ck_negocios_nombre_not_empty")

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    slug = Column(String(150), nullable=False, unique=False)
    email = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=False)
    direccion = Column(String(255), nullable=False)
    delet_at = Column(DateTime(timezone=True), nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
    