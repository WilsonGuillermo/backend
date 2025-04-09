# Archivo: main.py
# Version 1.1.0 WilsonGuillermo
# Externalisacion de get_db()

#from fastapi import APIRouter, FastAPI, Depends, HTTPException
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import modelos, schemas
from database import engine, get_db
from auth import rutas as auth_rutas

app = FastAPI()

#app = APIRouter(tags=["Referencial Tienda"])

# Inicializar Base de Datos
modelos.Base.metadata.create_all(bind=engine)

app.include_router(auth_rutas.router)
app.include_router(auth_rutas.rutero)

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






