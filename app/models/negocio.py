from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey,
    CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class Negocio(Base):
    __tablename__ = "negocios"

    __table_args__ = (
        UniqueConstraint("slug", name="uq_negocio_slug"),
        CheckConstraint("char_length(nombre) > 0", name="ck_negocios_nombre_not_empty")
    )

    id = Column(Integer, primary_key=True, index=True)
    
    nombre = Column(String(150), nullable=False)
    slug = Column(String(150), nullable=False, unique=False)
    email = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=False)
    direccion = Column(String(255), nullable=False)

    #relacion con propietario
    propietario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False, index=True)
    propietario = relationship("Usuario", back_populates="negocio")

    #relacion con servicio
    servicios = relationship("Servicio", back_populates="negocio")
    
    #relacion con reserva
    reservas = relationship("Reserva", back_populates="negocio")
    #soft delete
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    #timestamps
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
    