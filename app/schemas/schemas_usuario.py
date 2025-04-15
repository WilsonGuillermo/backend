# Archivo: usuario.py
# Version 1.0.0 WilsonGuillermo
# Agregamos las clases RolOut y UsuarioOut
# Agregamos un flag para la primera connexion del usuario

from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

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
    nombre_usuario: str
    contrasena: str # Se debe hashear antes de guardarlo en la BD
    nombre: str
    apellido: str
    email: str
    #rol: str
    rol_id: int
    primer_acceso: Optional[bool] = True  # Opcional


class UsuarioResponse(UsuarioBase):
    id_usuario: int
    fecha_creacion_cuenta: datetime
    rol_id: int

    class Config:
        from_attributes = True

class UsuarioOut(UsuarioBase):
    id_usuario: int
    nombre_usuario: str
    nombre: str
    apellido: str
    email: str
    #rol: str
    rol_id: int
    primer_acceso: bool  # NUEVO

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    nombre_usuario: str
    contrasena: str

class LoginResponse(BaseModel):
    id_usuario: int
    access_token: str
    token_type: str
    nombre_usuario: str
    profil: str
    primer_acceso: bool

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

class CambiarContrasenaRequest(BaseModel):
    contrasena: str
