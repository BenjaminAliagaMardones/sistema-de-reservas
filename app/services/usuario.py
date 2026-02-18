from app.repositories.usuario import UsuarioRepository
from app.schemas.usuario import UsuarioCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.usuario import Usuario
from passlib.context import CryptContext



class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()
        self.pwd_context = CryptContext(schemes=["bcrypt"])

    def crear(self, db: Session, datos: UsuarioCreate):

        if self.repository.obtener_por_email(db, datos.email):
            raise HTTPException(400, "El email ya esta en uso")
        
        if self.repository.obtener_por_username(db, datos.username):
            raise HTTPException(400, "El username ya esta en uso")


        datos_dict = datos.model_dump(exclude={"password"})

        usuario = Usuario(
            **datos_dict,
            password_hash = self.pwd_context.hash(datos.password)
        )

        return self.repository.crear(db, usuario)
    
    def obtener_por_id(self, db:Session, id: int):
        usuario = self.repository.obtener_por_id(db, id)

        if not usuario:
            raise HTTPException(404, "El usuario no existe")
        
        return usuario
    
    def obtener_todos(self, db:Session):
        
        return self.repository.obtener_todos(db)
    
    def actualizar(self, db: Session, id: int, datos):
        usuario = self.obtener_por_id(db, id)

        return self.repository.actualizar(db, id, datos)
    
    def eliminar(self, db: Session, id: int):
        usuario = self.obtener_por_id(db, id)

        return self.repository.eliminar(db, id)