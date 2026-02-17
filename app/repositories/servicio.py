from sqlalchemy.orm import Session
from app.models.servicio import Servicio
from app.schemas.servicio import ServicioCreate, ServicioUpdate
from datetime import datetime, timezone

class ServicioRepository:
    
    def crear(self, db: Session, datos: ServicioCreate):
        servicio = Servicio(**datos.model_dump())

        db.add(servicio)
        db.commit()
        db.refresh(servicio)

        return servicio
    
    def obtener_por_id(self, db: Session, id: int):
        servicio = db.query(Servicio).filter(Servicio.id == id).first()

        return servicio
    
    def obtener_todos(self, db:Session):
        servicios = db.query(Servicio).all()

        return servicios
    
    def actualizar(self, db: Session, id: int, datos: ServicioUpdate):
        servicio = db.query(Servicio).filter(Servicio.id == id).first()
        
        for campo, valor in datos.model_dump(exclude_unset=True).items():
            setattr(servicio, campo, valor)

        db.commit()
        db.refresh(servicio)

        return servicio
    
    def eliminar(self, db: Session, id: int):
        servicio = db.query(Servicio).filter(Servicio.id == id).first()

        servicio.deleted_at = datetime.now(timezone.utc)

        db.commit()

    def obtener_por_negocio(self, db: Session, negocio_id: int):
        servicios = db.query(Servicio).filter(Servicio.negocio_id == negocio_id).all()

        return servicios