# Archivo: producto_catalogo.py
# Version 1.0.0 WilsonGuillermo

from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# 📌 Esquema para Tipo de Tienda
class TipoTiendaSchema(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True

# 📌 Esquema para Producto Base
class ProductoBaseSchema(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    tipo_tienda_id: int
    activo: bool

    class Config:
        orm_mode = True

# 📌 Esquema para Producto Variación
class ProductoVariacionSchema(BaseModel):
    id: int
    producto_base_id: int
    descripcion: str # Agregamos la nueva propiedad
    precio: float
    stock: int

    class Config:
        orm_mode = True

# 📌 Esquema para Atributos de Producto
class AtributoProductoSchema(BaseModel):
    id: int
    variacion_id: int
    nombre: str
    valor: str

    class Config:
        orm_mode = True

class AtributoCreate(BaseModel):
    nombre: str
    valor: str

class VariacionCreate(BaseModel):
    descripcion: str
    stock: int
    precio: float
    atributos: List[AtributoCreate]


class ProductoComboCreate(BaseModel):
    nombre: str
    descripcion: Optional[str]
    tipo_tienda_id: int
    activo: Optional[bool] = True
    variaciones: List[VariacionCreate]
