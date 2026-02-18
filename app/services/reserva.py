from app.repositories.reserva import ReservaRepository
from app.schemas.reserva import ReservaCreate, ReservaUpdateEstado
from sqlalchemy.orm import Session
from fastapi import HTTPException


class ReservaService:
    def __init__(self):
        self.repository = ReservaRepository()

    def crear(self, db: Session, datos: ReservaCreate):
        # Validar que el cliente no tenga otra reserva en la misma fecha y hora
        reservas_cliente = self.repository.obtener_por_cliente(db, datos.cliente_id)
        if any(
            r.fecha == datos.fecha and r.hora_inicio == datos.hora_inicio
            for r in reservas_cliente
        ):
            raise HTTPException(
                400,
                "El cliente ya tiene una reserva en esa fecha y hora",
            )

        # Validar que el negocio no tenga otra reserva en la misma fecha y hora
        reservas_negocio = self.repository.obtener_por_negocio(db, datos.negocio_id)
        if any(
            r.fecha == datos.fecha and r.hora_inicio == datos.hora_inicio
            for r in reservas_negocio
        ):
            raise HTTPException(
                400,
                "El negocio ya tiene una reserva en esa fecha y hora",
            )

        # Aquí usamos el repositorio tal como está definido (recibe ReservaCreate)
        return self.repository.crear(db, datos)

    def obtener_por_id(self, db: Session, id: int):
        reserva = self.repository.obtener_por_id(db, id)

        if not reserva:
            raise HTTPException(404, "La reserva no existe")

        return reserva

    def obtener_todos(self, db: Session):
        return self.repository.obtener_todos(db)

    def actualizar_estado(self, db: Session, id: int, datos: ReservaUpdateEstado):
        # Asegura que existe o lanza 404
        self.obtener_por_id(db, id)
        return self.repository.actualizar_estado(db, id, datos)

    def eliminar(self, db: Session, id: int):
        # Asegura que existe o lanza 404
        self.obtener_por_id(db, id)
        return self.repository.eliminar(db, id)