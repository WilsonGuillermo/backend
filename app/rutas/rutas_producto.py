# auth/routes.py — Endpoints FastAPI
# Version 1.0.1 WilsonGuillermo
# Agregamos un flag para la primera connexion del usuario y una nueva ruta para utilisarlo

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bdd.database import get_db

from modelos import modelo_producto
from schemas import schemas_producto

producto = APIRouter()

objeto = APIRouter()

# 📌 Obtener todos los tipos de tienda
@producto.get("/tipos_tienda", response_model=list[schemas_producto.TipoTiendaSchema])
def get_tipos_tienda(db: Session = Depends(get_db)):
    return db.query(modelo_producto.TipoTienda).all()

# 📌 Obtener todos los productos base
@producto.get("/productos_base", response_model=list[schemas_producto.ProductoBaseSchema])
def get_productos_base(db: Session = Depends(get_db)):
    return db.query(modelo_producto.ProductoBase).all()

# 📌 Obtener todas las variaciones de un producto base
@producto.get("/productos/{producto_id}/variaciones", response_model=list[schemas_producto.ProductoVariacionSchema])
def get_variaciones(producto_id: int, db: Session = Depends(get_db)):
    return db.query(modelo_producto.ProductoVariacion).filter(modelo_producto.ProductoVariacion.producto_base_id == producto_id).all()

# 📌 Obtener atributos de una variación
@producto.get("/variaciones/{variacion_id}/atributos", response_model=list[schemas_producto.AtributoProductoSchema])
def get_atributos(variacion_id: int, db: Session = Depends(get_db)):
    return db.query(modelo_producto.AtributoProducto).filter(modelo_producto.AtributoProducto.variacion_id == variacion_id).all()

@objeto.post("/productos/completo")
def crear_producto_completo(
        producto_data: schemas_producto.ProductoComboCreate,
        db: Session = Depends(get_db)
    ):
        nuevo_producto = modelo_producto.ProductoBase(
            nombre=producto_data.nombre,
            descripcion=producto_data.descripcion,
            tipo_tienda_id=producto_data.tipo_tienda_id,
            activo=producto_data.activo,
        )

        print("nuevo producto:", nuevo_producto)

        for variedad in producto_data.variaciones:
            nueva_variedad = modelo_producto.ProductoVariacion(
                descripcion=variedad.descripcion,
                stock=variedad.stock,
                precio=variedad.precio,
            )
            print("nueva variedad:", nueva_variedad)
            for atributo in variedad.atributos:
                nuevo_atributo = modelo_producto.AtributoProducto(
                    nombre=atributo.nombre,
                    valor=atributo.valor,
                )

                print("nuevo atributo:", nuevo_atributo)

                nueva_variedad.atributos.append(nuevo_atributo)

            nuevo_producto.variaciones.append(nueva_variedad)

        db.add(nuevo_producto)
        db.commit()
        db.refresh(nuevo_producto)

        return {"mensaje": "Producto creado exitosamente", "producto_id": nuevo_producto.id}


