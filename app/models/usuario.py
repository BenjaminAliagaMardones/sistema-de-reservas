from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey,
    CheckConstraint, UniqueConstraint, Index, Boolean, Text, Enum as SAEnum
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base
from enum import Enum

class RolUsuario(Enum):
    ADMIN = "admin"
    PROPIETARIO = "propietario"
    CLIENTE = "cliente"

class Usuario(Base):
    __tablename__ = "usuarios"

    __table_args__ = (
        UniqueConstraint("email", name="uq_usuario_email"),
        UniqueConstraint("username", name="uq_usuario_username"),
        CheckConstraint("char_length(nombre) > 0", name="ck_usuarios_nombre_not_empty"),
        CheckConstraint("edad >= 18", name="ck_usuarios_mayor_edad")
    )

    id = Column(Integer, primary_key=True, index=True)

    #datos personales
    nombre = Column(String(150), nullable=False)
    apellido = Column(String(150), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    username = Column(String(50), nullable=False, index=True)
    telefono = Column(String(20), nullable=True)

    password_hash = Column(String(255), nullable=False)
    
    #rol y permiso
    rol = Column(SAEnum(RolUsuario), nullable=False, default=RolUsuario.CLIENTE)
    is_active = Column(Boolean, default=True, nullable=False)

    # relaciones
    negocio_id = Column(Integer, ForeignKey("negocios.id"), nullable=True)
    negocio = relationship("Negocio", back_populates="propietario")
    reservas = relationship("Reserva", back_populates="cliente")
    
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
    last_login = Column(DateTime(timezone=True), nullable=True)



    