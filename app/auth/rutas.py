# auth/routes.py — Endpoints FastAPI
# Version 1.0.0 WilsonGuillermo

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import modelos, schemas
from auth.seguridad import hash_password
from auth.autentificacion import crear_token
from modelos import Usuario

router = APIRouter(prefix="/auth", tags=["Identificación"])

rutero = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.post("/roles", response_model=schemas.RolOut)
def crear_rol(rol: schemas.RolCreate, db: Session = Depends(get_db)):
    db_rol = db.query(modelos.Rol).filter_by(nombre_del_rol=rol.nombre_del_rol).first()
    if db_rol:
        raise HTTPException(status_code=400, detail="El rol ya existe.")
    nuevo_rol = modelos.Rol(**rol.dict())
    db.add(nuevo_rol)
    db.commit()
    db.refresh(nuevo_rol)
    return nuevo_rol

@router.get("/roles", response_model=list[schemas.RolOut])
def listar_roles(db: Session = Depends(get_db)):
    return db.query(modelos.Rol).all()

@router.post("/usuarios", response_model=schemas.UsuarioOut)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    existente = db.query(modelos.Usuario).filter_by(nombre_usuario=usuario.nombre_usuario).first()
    if existente:
        raise HTTPException(status_code=400, detail="El usuario ya existe.")

    nuevo_usuario = modelos.Usuario(
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        nombre_usuario=usuario.nombre_usuario,
        contrasena=hash_password(usuario.contrasena),
        email=usuario.email,
        fecha_nacimiento=usuario.fecha_nacimiento,
        rol_id=usuario.rol_id
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

# Ruta para obtener todos los usuarios
@router.get("/usuarios", response_model=list[schemas.UsuarioConRol])
def listar_usuarios(db: Session = Depends(get_db)):
    print("los usuarios sont:", db.query(modelos.Usuario).all())
    usuarios = db.query(modelos.Usuario).all()

    usuarios_con_rol = [
        schemas.UsuarioConRol(
            id_usuario = u.id_usuario,
            nombre = u.nombre,
            apellido = u.apellido,
            nombre_usuario = u.nombre_usuario,
            email = u.email,
            fecha_nacimiento = u.fecha_nacimiento,
            rol = u.profil.nombre_del_rol
        )
        for u in usuarios
    ]

    return usuarios_con_rol


@router.get("/verificarCuenta/{login}", response_model=schemas.UsuarioOut)
def verificar_cuenta(login: str, db: Session = Depends(get_db)):
    print("El usuario es: $usuario")
    try:
        print("Login recibido:", login)
        usuario = db.query(modelos.Usuario).filter_by(nombre_usuario = login).first()
    except Exception as e:
        print("Error en la consulta:", e)
        raise HTTPException(status_code=500, detail="Error interno")

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return usuario

# Ruta para recuperar el rol a partir del login/mdp
@router.post("/login", response_model=schemas.LoginResponse)
def login( request: schemas.LoginRequest, db: Session = Depends(get_db)):
    try:
        print("Login recibido:", request.nombre_usuario)
        usuario = db.query(Usuario).filter(Usuario.nombre_usuario == request.nombre_usuario).first()
    except Exception as e:
        print("Error en la consulta:", e)
        raise HTTPException(status_code=500, detail="Error interno")

    print("el usuario es: ", usuario)
    if not usuario or usuario.contrasena != request.contrasena:
        raise HTTPException(status_code=404, detail="Credentiales incorrectas")

    token = crear_token({"sub": usuario.nombre_usuario})

    print("El usuario es: ",usuario)

    return {
        "access_token": token,
        "token_type": "bearer",
        #"usuario": {
            "nombre_usuario": usuario.nombre_usuario,
            "profil": usuario.profil.nombre_del_rol
        #}
    }# Ruta para actualizar un usuario

@rutero.put("/{id_usuario}")
def actualizar_usuario(id_usuario: int, datos: schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    try:
        usuario = db.query(modelos.Usuario).filter(modelos.Usuario.id_usuario == id_usuario).first()
    except Exception as e:
        print("Error en la consulta:", e)
        raise HTTPException(status_code=500, detail="Error interno")

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if datos.nombre is not None:
        usuario.nombre = datos.nombre
    if datos.apellido is not None:
        usuario.apellido = datos.apellido
    if datos.rol is not None:
        rol = db.query(modelos.Rol).filter(modelos.Rol.nombre_del_rol == datos.rol).first()
        if not rol:
            raise HTTPException(status_code=404, detail="Rol no válido")
        usuario.rol_id = rol.id_rol

    db.commit()
    db.refresh(usuario)

    return {"mensaje": "Usuario actualizado correctamente"}

# Ruta para eliminar una cuenta
@rutero.delete("/{usuario_id}", response_model=schemas.UsuarioUpdate)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(modelos.Usuario).filter(modelos.Usuario.id_usuario == usuario_id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(usuario)
    db.commit()

    return {"mensaje": "Usuario eliminado correctamente"}


