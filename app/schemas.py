# Archivo: schemas.py
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

class RolBase(BaseModel):
    nombre_del_rol: str
    derechos: Optional[str] = None

class RolCreate(RolBase):
    pass

class RolResponse(RolBase):
    id_rol: int
    nombre_del_rol: str

    class Config:
        from_attributes = True

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    nombre_usuario: str
    email: EmailStr
    fecha_nacimiento: Optional[datetime] = None

class UsuarioCreate(UsuarioBase):
    contrasena: str  # Se debe hashear antes de guardarlo en la BD
    rol: str

class UsuarioResponse(UsuarioBase):
    id_usuario: int
    fecha_creacion_cuenta: datetime
    rol: str  # Para devolver el rol del usuario solamente

    class Config:
        from_attributes = True

