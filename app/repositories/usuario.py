from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate
from datetime import datetime, timezone

class UsuarioRepository:
    def crear(self, db: Session, datos: UsuarioCreate):
        usuario = Usuario(**datos.model_dump())

        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    
    def obtener_por_id(self, db: Session, id: int):
        usuario = db.query(Usuario).filter(Usuario.id == id).first()
        return usuario
    
    def obtener_todos(self, db: Session):
        usuarios = db.query(Usuario).all()
        return usuarios
    
    def actualizar(self, db:Session, id: int, datos: UsuarioUpdate):
        usuario = db.query(Usuario).filter(Usuario.id == id).first()

        for campo, valor in datos.model_dump(exclude_unset=True).items():
            setattr(usuario, campo, valor)
        
        db.commit()
        db.refresh(usuario)
        
        return usuario
    
    def eliminar(self, db: Session, id: int):
        usuario = db.query(Usuario).filter(Usuario.id == id).first()
        usuario.deleted_at = datetime.now(timezone.utc)
        db.commit()

    def obtener_por_email(self, db: Session, email: str):
        usuario = db.query(Usuario).filter(Usuario.email == email).first()
        return usuario
    
    def obtener_por_username(self, db: Session, username: str):
        usuario = db.query(Usuario).filter(Usuario.username == username).first()
        return usuario
    
