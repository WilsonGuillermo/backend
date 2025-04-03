#🔹 Script import_csv.py

import pandas as pd
from sqlalchemy.orm import sessionmaker
from database import engine, SessionLocal
from modelos import TipoTienda, ProductoBase, ProductoVariacion, AtributoProducto

columnas_equivalentes = {
    "Tipo de tienda": "Boutique",
    "Producto de base": "producto_base",
    "Producto variacion precio": "precio",
    "Producto variacion stock": "stock",
    "Atributo variacion nombre": "atributo_nombre",
    "Atributo variacion valor": "atributo_valor"
}

# 1️⃣ Cargar el archivo CSV
csv_file = "productos_tienda.csv"
df = pd.read_csv(csv_file, delimiter=";", encoding="ISO-8859-1")  # Usa ";" como separador

# Limpiar nombres de columnas: eliminar espacios extras y poner en minúsculas
df.columns = [col.strip() for col in df.columns]

# Aplicar las equivalencias
df.rename(columns=columnas_equivalentes, inplace=True)

# Verificar si todas las columnas requeridas están en el CSV
columnas_requeridas = set(columnas_equivalentes.values())
columnas_encontradas = set(df.columns)

if not columnas_requeridas.issubset(columnas_encontradas):
    print("⚠️ ERROR: Faltan columnas en el CSV:", columnas_requeridas - columnas_encontradas)
else:
    print("✅ CSV cargado correctamente con las columnas esperadas.")

# 2️⃣ Iniciar sesión con la base de datos
db = SessionLocal()

# 3️⃣ Procesar cada fila del CSV
for _, row in df.iterrows():
    # ➜ Buscar o crear TipoTienda (Boutique)
    tipo_tienda = db.query(TipoTienda).filter_by(nombre=row["Boutique"]).first()
    if not tipo_tienda:
        tipo_tienda = TipoTienda(nombre=row["Boutique"])
        db.add(tipo_tienda)
        db.commit()
    
    # ➜ Buscar o crear ProductoBase
    producto_base = db.query(ProductoBase).filter_by(nombre=row["producto_base"], tipo_tienda_id=tipo_tienda.id).first()
    if not producto_base:
        producto_base = ProductoBase(
				nombre=row["producto_base"],
				descripcion=row["producto_base"],
				tipo_tienda_id=tipo_tienda.id)
        db.add(producto_base)
        db.commit()
    
    # Crear descripción combinando Producto base + Atributo nombre + Atributo valor
    descripcion_generada = f"{row['producto_base']} - {row['atributo_nombre']}: {row['atributo_valor']}"

    # ➜ Buscar o crear ProductoVariacion (mismo producto pero con diferentes atributos)
    producto_variacion = db.query(ProductoVariacion).filter_by(producto_base_id=producto_base.id, precio=row["precio"]).first()
    if not producto_variacion:
        producto_variacion = ProductoVariacion(
				producto_base_id=producto_base.id, 
				descripcion=descripcion_generada,
				precio=row["precio"], 
				stock=row["stock"]
		            )
        db.add(producto_variacion)
        db.commit()

    # ➜ Agregar AtributoProducto
    atributo = AtributoProducto(variacion_id=producto_variacion.id, nombre=row["atributo_nombre"], valor=row["atributo_valor"])
    db.add(atributo)
    db.commit()

# 4️⃣ Cerrar sesión con la base de datos
db.close()

print("✅ Datos importados con éxito")

