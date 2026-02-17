from sqlalchemy.orm import Session
from app.models.negocio import Negocio
from app.schemas.negocio import NegocioCreate, NegocioUpdate
from datetime import datetime, timezone

class NegocioRepository:
    def crear(self, db: Session, datos: NegocioCreate):
        negocio = Negocio(**datos.model_dump())

        db.add(negocio)
        db.commit()
        db.refresh(negocio)
        return negocio
    
    def obtener_por_id(self, db: Session, id: int):
        negocio = db.query(Negocio).filter(Negocio.id == id).first()
        return negocio
    
    def obtener_todos(self, db: Session):
        negocios = db.query(Negocio).all()
        return negocios
    
    def actualizar(self, db: Session, id: int, datos: NegocioUpdate):
        negocio = db.query(Negocio).filter(Negocio.id == id).first()

        for campo, valor in datos.model_dump(exclude_unset=True).items():
            setattr(negocio, campo, valor)

        db.commit()
        db.refresh(negocio)
        return negocio

    def eliminar(self, db:Session, id: int):
        negocio = db.query(Negocio).filter(Negocio.id == id).first()
        negocio.deleted_at = datetime.now(timezone.utc)
        db.commit()