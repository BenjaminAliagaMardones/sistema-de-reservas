from pydantic import BaseModel
from typing import Optional
from datetime import time, date, datetime
from enum import Enum

class EstadoReserva(str, Enum):
    PENDIENTE = "pendiente"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"
    RECHAZADA = "rechazada"
    COMPLETADA = "completada"
    NO_SHOW = "no_show"

class ReservaCreate(BaseModel):
    fecha: date
    hora_inicio: time
    servicio_id: int
    negocio_id: int
    notas_cliente: Optional[str] = None

class ReservaUpdateEstado(BaseModel):
    estado: EstadoReserva
    motivo_cancelacion: Optional[str] = None
    notas_negocio: Optional[str] = None

class ReservaResponse(BaseModel):
    id: int
    fecha: date
    hora_inicio: time
    hora_fin: time
    estado: str
    cliente_id: int
    negocio_id: int
    servicio_id: int
    created_at: datetime

    model_config = {"from_attributes": True}