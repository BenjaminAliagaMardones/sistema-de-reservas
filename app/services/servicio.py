from app.repositories.servicio import ServicioRepository
from app.schemas.servicio import ServicioCreate, ServicioUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.servicio import Servicio

class ServicioService:
    def __init__(self):
        self.repository = ServicioRepository()

    def crear(self, db: Session, datos: ServicioCreate):
     
          servicios_negocio = self.repository.obtener_por_negocio(db, datos.negocio_id)
          if any(servicio.nombre == datos.nombre for servicio in servicios_negocio):
               raise HTTPException(400, "El servicio ya existe")
          
          return self.repository.crear(db, datos)
    
    def obtener_por_id(self, db: Session, id: int):
         servicio = self.repository.obtener_por_id(db, id)

         if not servicio:
              raise HTTPException(404, "el servicio no existe")
         
         return servicio
    
    def obtener_todos(self, db: Session):
          return self.repository.obtener_todos(db)
    
    def actualizar(self, db: Session, id: int, datos: ServicioUpdate):
          self.obtener_por_id(db, id)

          return self.repository.actualizar(db, id, datos)
    
    def eliminar(self, db: Session, id: int):
          self.obtener_por_id(db, id)

          return self.repository.eliminar(db, id)