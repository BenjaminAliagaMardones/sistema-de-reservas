from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
class ServicioCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=150)
    descripcion: Optional[str] = Field(None, max_length=1000)
    duracion_minutos: int = Field(..., gt=0)
    precio: int = Field(..., ge=0)
    capacidad_maxima: int = Field(default=1, gt=0)



class ServicioUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=150)
    descripcion: Optional[str] = Field(None, max_length=1000)
    duracion_minutos: Optional[int] = Field(None, gt=0)
    precio: Optional[int] = Field(None, ge=0)
    capacidad_maxima: Optional[int] = Field(None, gt=0)

class ServicioResponse(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str]
    duracion_minutos: int
    precio: int
    capacidad_maxima: int
    negocio_id: int
    created_at: datetime

    model_config = {"from_attributes": True}