# Archivo: main.py
# Version 1.0.0 WilsonGuillermo

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import modelos, schemas
from database import SessionLocal, engine

app = FastAPI()

# Inicializar Base de Datos
modelos.Base.metadata.create_all(bind=engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📌 Obtener todos los tipos de tienda
@app.get("/tipos_tienda", response_model=List[schemas.TipoTiendaSchema])
def get_tipos_tienda(db: Session = Depends(get_db)):
    return db.query(modelos.TipoTienda).all()

# 📌 Obtener todos los productos base
@app.get("/productos_base", response_model=List[schemas.ProductoBaseSchema])
def get_productos_base(db: Session = Depends(get_db)):
    return db.query(modelos.ProductoBase).all()

# 📌 Obtener todas las variaciones de un producto base
@app.get("/productos/{producto_id}/variaciones", response_model=List[schemas.ProductoVariacionSchema])
def get_variaciones(producto_id: int, db: Session = Depends(get_db)):
    return db.query(modelos.ProductoVariacion).filter(modelos.ProductoVariacion.producto_base_id == producto_id).all()

# 📌 Obtener atributos de una variación
@app.get("/variaciones/{variacion_id}/atributos", response_model=List[schemas.AtributoProductoSchema])
def get_atributos(variacion_id: int, db: Session = Depends(get_db)):
    return db.query(modelos.AtributoProducto).filter(modelos.AtributoProducto.variacion_id == variacion_id).all()

# Ruta para obtener todos los roles
@app.get("/roles/", response_model=list[schemas.RolResponse])
def get_roles(db: Session = Depends(get_db)):
    return db.query(modelos.Rol).all()

# Ruta para crear un rol
@app.post("/roles/", response_model=schemas.RolResponse)
def create_role(rol: schemas.RolCreate, db: Session = Depends(get_db)):
    new_rol = modelos.Rol(**rol.dict())
    db.add(new_rol)
    db.commit()
    db.refresh(new_rol)
    return new_rol

# Ruta para obtener todos los usuarios
@app.get("/usuarios/", response_model=list[schemas.UsuarioResponse])
def get_usuarios(db: Session = Depends(get_db)):
    return db.query(modelos.Usuario).all()

# Ruta para crear un usuario
@app.post("/usuarios/", response_model=schemas.UsuarioResponse)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    # Aquí deberías hashear la contraseña antes de guardarla
    new_usuario = modelos.Usuario(**usuario.dict())
    db.add(new_usuario)
    db.commit()
    db.refresh(new_usuario)
    return new_usuario

