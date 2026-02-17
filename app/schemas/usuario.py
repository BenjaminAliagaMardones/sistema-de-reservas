from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
from enum import Enum

class RolUsuario(str, Enum):
    ADMIN = "admin"
    PROPIETARIO = "propietario"
    CLIENTE = "cliente"    

class UsuarioCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=150)
    apellido: str = Field(..., min_length=3, max_length=150)
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    telefono: str = Field(None, min_length=7, max_length=20)
    password: str = Field(..., min_length=8, max_length=100)
    rol: RolUsuario = RolUsuario.CLIENTE

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=150)
    apellido: Optional[str] = Field(None, min_length=3, max_length=150)
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    telefono: Optional[str] = Field(None, min_length=7, max_length=20)

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: str
    username: str
    telefono: Optional[str]
    rol: RolUsuario
    negocio_id: Optional[int]
    created_at: datetime

    model_config = {"from_attributes": True}

class CambiarPassword(BaseModel):
    password_actual: str = Field(..., min_length=8, max_length=100)
    password_nuevo: str = Field(..., min_length=8, max_length=100)