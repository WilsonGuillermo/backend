# Aquí definimos las tablas de la gestion de los usuarios de la base de datos:
# Version 1.0.0 WilsonGuillermo
# Agregamos un flag para la primera connexion del usuario

from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.orm import relationship

from bdd.database import Base
from datetime import datetime

class Rol(Base):
    __tablename__ = "roles"

    id_rol = Column(Integer, primary_key=True, index=True)
    nombre_del_rol = Column(String(50), unique=True, nullable=False)
    derechos = Column(String(255), nullable=True)

    usuarios = relationship("Usuario", back_populates="profil")

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    nombre_usuario = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)  # Debe estar hasheada
    email = Column(String(255), unique=True, nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=True)
    fecha_creacion_cuenta = Column(DateTime, default=datetime.utcnow)
    primer_acceso = Column(Boolean, default=True)  # NUEVO

    rol_id = Column(Integer, ForeignKey("roles.id_rol"))
    profil = relationship("Rol", back_populates="usuarios")
