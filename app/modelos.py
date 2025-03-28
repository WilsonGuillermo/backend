# Aquí definimos las tablas de la base de datos:
# Version 1.0.0 WilsonGuillermo

from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# 📌 Tipo de tienda (Ej: Ropa, Supermercado, Ferretería, etc.)
class TipoTienda(Base):
    __tablename__ = "tipo_tienda"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)

# 📌 Productos base (Ej: "Camiseta", "Martillo", "Arroz")
class ProductoBase(Base):
    __tablename__ = "producto_base"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(500), nullable=True)
    tipo_tienda_id = Column(Integer, ForeignKey("tipo_tienda.id"))

    tipo_tienda = relationship("TipoTienda")
    variaciones = relationship("ProductoVariacion", back_populates="producto_base")

# 📌 Variaciones de productos (Ej: "Camiseta Azul - Talla M")
class ProductoVariacion(Base):
    __tablename__ = "producto_variacion"

    id = Column(Integer, primary_key=True, index=True)
    producto_base_id = Column(Integer, ForeignKey("producto_base.id"))
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    producto_base = relationship("ProductoBase", back_populates="variaciones")
    atributos = relationship("AtributoProducto", back_populates="variacion")

# 📌 Atributos de producto (Ej: talla, color, material)
class AtributoProducto(Base):
    __tablename__ = "atributo_producto"

    id = Column(Integer, primary_key=True, index=True)
    variacion_id = Column(Integer, ForeignKey("producto_variacion.id"))
    nombre = Column(String(100), nullable=False)
    valor = Column(String(100), nullable=False)

    variacion = relationship("ProductoVariacion", back_populates="atributos")

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

    rol = Column(String(50), ForeignKey("roles.nombre_del_rol"))
    profil = relationship("Rol", back_populates="usuarios")
