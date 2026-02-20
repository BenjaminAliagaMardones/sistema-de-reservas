from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey,
    CheckConstraint, UniqueConstraint, Date, Time
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base
from enum import Enum

class EstadoReserva(str, Enum):
    PENDIENTE = "pendiente"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"
    RECHAZADA = "rechazada"
    COMPLETADA = "completada"
    NO_SHOW = "no_show"

class Reserva(Base):
    __tablename__ = "reservas"

    __table_args__ = (

        UniqueConstraint(
            "cliente_id", "fecha", "hora_inicio",
            name="uq_reserca_cliente_fecha_hora"
        ),

        UniqueConstraint(
            "servicio_id", "fecha", "hora_inicio",
            name="uq_reserva_servicio_fecha_hora"
        ),

        CheckConstraint("hora_fin > hora_inicio", name="ck_reserva_hora_fin_mayor")
    )

    id = Column(Integer, primary_key=True, index=True)

    fecha = Column(Date, nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)

    notas_cliente = Column(Text, nullable=True)
    notas_negocio = Column(Text, nullable=True)
    motivo_cancelacion = Column(Text, nullable=True)


    estado = Column(
        String(20),
        nullable=False,
        default=EstadoReserva.PENDIENTE.value
    )

    #relacion con cliente
    cliente_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    cliente = relationship("Usuario", back_populates="reservas")

    #relacion con servicio
    servicio_id = Column(Integer, ForeignKey("servicios.id"), nullable=False )
    servicio = relationship("Servicio", back_populates="reservas")

    #realcion con negocio
    negocio_id = Column(Integer, ForeignKey("negocios.id"), nullable=False)
    negocio = relationship("Negocio", back_populates="reservas")

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