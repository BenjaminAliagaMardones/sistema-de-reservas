from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class NegocioCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=150)
    email: EmailStr
    telefono: str = Field(..., min_length=7, max_length=20)
    direccion: str = Field(..., min_length=10, max_length=255)

class NegocioUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=150)
    email: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, min_length=7, max_length=20)
    direccion: Optional[str] = Field(None, min_length=10, max_length=255)

class NegocioResponse(BaseModel):
    id: int
    nombre: str
    slug: str
    email: str
    telefono: str
    direccion: str
    propietario_id: int
    created_at: datetime

    model_config = {"from_attributes": True}
