# Archivo: main.py
# Version 1.1.0 WilsonGuillermo
# Externalisacion de get_db()

#from fastapi import APIRouter, FastAPI, Depends, HTTPException
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

import modelos #,  schemas, rutas, auth, bdd
from bdd.database import engine #, get_db
#from bdd import database.engine as engine
#from bdd import database.get_db as get_db
#from bdd database import engine, get_db
from rutas.rutas_usuario import router, rutero
from rutas.rutas_producto import producto, objeto

app = FastAPI()

#app = APIRouter(tags=["Referencial Tienda"])

# Inicializar Base de Datos
modelos.Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/usuarios", tags=["Identificación de los usuarios"])
app.include_router(rutero, prefix="/usuarios", tags=["Gestion de los usuarios"])
app.include_router(producto, prefix="/productos", tags=["Gestion de los productos"])
app.include_router(objeto, prefix="/productos", tags=["Administracion de los productos"])








