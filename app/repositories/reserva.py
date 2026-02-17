from sqlalchemy.orm import Session
from app.models.reserva import Reserva
from app.schemas.reserva import ReservaCreate, ReservaUpdateEstado
from datetime import datetime, timezone

class ReservaRepository:

    def crear(self, db: Session, datos: ReservaCreate):
        
        reserva = Reserva(**datos.model_dump())

        db.add(reserva)
        db.commit()
        db.refresh(reserva)

        return reserva
    
    def obtener_por_id(self, db: Session, id: int):

        reserva = db.query(Reserva).filter(Reserva.id == id).first()
        return reserva
    
    def obtener_todos(self, db: Session):
        reservas = db.query(Reserva).all()
        return reservas
    
    def actualizar_estado(self, db:Session, id: int, datos: ReservaUpdateEstado):
        reserva = db.query(Reserva).filter(Reserva.id == id).first()

        for campo, valor in datos.model_dump(exclude_unset=True).items():
            setattr(reserva, campo, valor)

        db.commit()
        db.refresh(reserva)
        return reserva
    
    def obtener_por_negocio(self, db: Session, negocio_id: int):
        reserva = db.query(Reserva).filter(Reserva.negocio_id == negocio_id).all()
        return reserva
    
    def obtener_por_cliente(self, db: Session, cliente_id: int):
        reserva = db.query(Reserva).filter(Reserva.cliente_id == cliente_id). all()
        return reserva



        