from app.repositories.negocio import NegocioRepository
from app.schemas.negocio import NegocioCreate, NegocioUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.negocio import Negocio

class NegocioService:
    def __init__(self):
        self.repository = NegocioRepository()

    def crear(self, db: Session, datos: NegocioCreate, propietario_id: int):
        slug = datos.nombre.lower().replace(" ", "-")

        if self.repository.obtener_por_slug(db, slug):
            raise HTTPException(400, "Ya existe un negocio con ese nombre")
        
        negocio = Negocio(
            **datos.model_dump(),
            slug=slug,
            propietario_id=propietario_id
        )
        
        return self.repository.crear(db, negocio)
    
    def obtener_por_id(self, db: Session, id: int):
        negocio = self.repository.obtener_por_id(db, id)

        if not negocio:
            raise HTTPException(404, "El negocio no existe")
        
        return negocio
    
    def obtener_todos(self, db: Session):
        return self.repository.obtener_todos(db)
    
    def actualizar(self, db: Session, id: int, datos: NegocioUpdate):
        negocio = self.obtener_por_id(db, id)

        return self.repository.actualizar(db, id, datos)
    
    def eliminar(self, db: Session, id: int):
        negocio = self.obtener_por_id(db, id)

        return self.repository.eliminar(db, id)