# Archivo: schemas.py
# Version 1.1.0 WilsonGuillermo
# Agregamos las clases RolOut y UsuarioOut

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

class RolOut(RolBase):
    id_rol: int
    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    nombre_usuario: str
    email: EmailStr
    fecha_nacimiento: Optional[datetime] = None

class UsuarioCreate(UsuarioBase):
    contrasena: str  # Se debe hashear antes de guardarlo en la BD
    rol_id: int

class UsuarioResponse(UsuarioBase):
    id_usuario: int
    fecha_creacion_cuenta: datetime
    rol_id: int

    class Config:
        from_attributes = True

class UsuarioOut(UsuarioBase):
    nombre_usuario: str
    contrasena: str
    rol_id: int

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    nombre_usuario: str
    contrasena: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    nombre_usuario: str
    profil: str

class UsuarioConRol(BaseModel):
    id_usuario: int
    nombre: str
    apellido: str
    nombre_usuario: str
    email: EmailStr
    fecha_nacimiento: Optional[datetime] = None
    rol: str

    class Config:
        orm_mode = True

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    rol: Optional[str] = None  # Nombre del rol

    class Config:
        orm_mode = True
