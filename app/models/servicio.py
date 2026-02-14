from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey,
    CheckConstraint, UniqueConstraint, Text, Boolean, Index
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class Servicio(Base):
    __tablename__ = "servicios"

    __table_args__ = (
        UniqueConstraint("nombre", "negocio_id", name="uq_servicio_nombre_negocio"),
        CheckConstraint("duracion_minutos > 0", name="ck_servicio_duracion_positiva"),
        CheckConstraint("precio >= 0", name="ck_servicio_precio_no_negativo"),
        CheckConstraint("capacidad_maxima > 0", name="ck_servicios_capacidad_positiva"),
        Index("ix_servicios_negocio_activo", "negocio_id", "is_active")
    )
    id = Column(Integer, primary_key=True, index=True)

    #informacion basica
    nombre = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=True)

    #configuracion
    duracion_minutos = Column(Integer, nullable=False)
    precio = Column(Integer, nullable=False)
    capacidad_maxima = Column(Integer, nullable=False, default=1)
    is_active = Column(Boolean, default=True, nullable=False)

    #realcion con negocio
    negocio_id = Column(Integer, ForeignKey("negocios.id"), nullable=False, index=True)
    negocio = relationship("Negocio", back_populates="servicios")

    #relacion con reservas
    reservas = relationship("Reserva", back_populates="servicio")

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