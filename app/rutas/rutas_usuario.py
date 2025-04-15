# auth/routes.py — Endpoints FastAPI
# Version 1.0.1 WilsonGuillermo
# Agregamos un flag para la primera connexion del usuario y una nueva ruta para utilisarlo

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bdd.database import get_db

from modelos import modelo_usuario
from schemas import schemas_usuario
from auth.autentificacion import crear_token, hash_password, verificar_password, verificar_token


router = APIRouter()

rutero = APIRouter()

@router.post("/roles", response_model=schemas_usuario.RolOut)
def crear_rol(rol: schemas_usuario.RolCreate, db: Session = Depends(get_db)):
    db_rol = db.query(modelo_usuario.Rol).filter_by(nombre_del_rol=rol.nombre_del_rol).first()
    if db_rol:
        raise HTTPException(status_code=400, detail="El rol ya existe.")
    nuevo_rol = modelo_usuario.Rol(**rol.dict())
    db.add(nuevo_rol)
    db.commit()
    db.refresh(nuevo_rol)
    return nuevo_rol

@router.get("/roles", response_model=list[schemas_usuario.RolOut])
def listar_roles(db: Session = Depends(get_db)):
    return db.query(modelo_usuario.Rol).all()

@router.post("/usuarios", response_model=schemas_usuario.UsuarioOut)
def crear_usuario(usuario: schemas_usuario.UsuarioCreate, db: Session = Depends(get_db)):
    existente = db.query(modelo_usuario.Usuario).filter_by(nombre_usuario=usuario.nombre_usuario).first()
    if existente:
        raise HTTPException(status_code=400, detail="El usuario ya existe.")

    nuevo_usuario = modelo_usuario.Usuario(
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
@router.get("/usuarios", response_model=list[schemas_usuario.UsuarioConRol])
def listar_usuarios(db: Session = Depends(get_db)):
    print("los usuarios sont:", db.query(modelo_usuario.Usuario).all())
    usuarios = db.query(modelo_usuario.Usuario).all()

    usuarios_con_rol = [
        schemas_usuario.UsuarioConRol(
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


@router.get("/verificarCuenta/{login}", response_model=schemas_usuario.UsuarioOut)
def verificar_cuenta(login: str, db: Session = Depends(get_db)):
    #print("El usuario es: $usuario")
    try:
        print("Login recibido:", login)
        usuario = db.query(modelo_usuario.Usuario).filter_by(nombre_usuario = login).first()
    except Exception as e:
        print("Error en la consulta:", e)
        raise HTTPException(status_code=500, detail="Error interno")

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return usuario

# Ruta para recuperar el rol a partir del login/mdp
@router.post("/login", response_model=schemas_usuario.LoginResponse)
def login( request: schemas_usuario.LoginRequest, db: Session = Depends(get_db)):
    try:
        print("Login recibido:", request.nombre_usuario)
        usuario = db.query(modelo_usuario.Usuario).filter(modelo_usuario.Usuario.nombre_usuario == request.nombre_usuario).first()
    except Exception as e:
        print("Error en la consulta:", e)
        raise HTTPException(status_code=500, detail="Error interno")

    print("el usuario es: ", usuario)
    if not usuario or not verificar_password(request.contrasena,usuario.contrasena):
        raise HTTPException(status_code=404, detail="Credentiales incorrectas")

    token = crear_token({"sub": usuario.nombre_usuario})

    print("El id del usuario es: ",usuario.id_usuario)

    return {
        "id_usuario": usuario.id_usuario,
        "access_token": token,
        "token_type": "bearer",
        "nombre_usuario": usuario.nombre_usuario,
        "profil": usuario.profil.nombre_del_rol,
        "primer_acceso": usuario.primer_acceso,
    }

# Ruta para actualizar un usuario
@rutero.put("/{id_usuario}")
def actualizar_usuario(id_usuario: int, datos: schemas_usuario.UsuarioUpdate, db: Session = Depends(get_db)):
    try:
        usuario = db.query(modelo_usuario.Usuario).filter(modelo_usuario.Usuario.id_usuario == id_usuario).first()
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
        rol = db.query(modelo_usuario.Rol).filter(modelo_usuario.Rol.nombre_del_rol == datos.rol).first()
        if not rol:
            raise HTTPException(status_code=404, detail="Rol no válido")
        usuario.rol_id = rol.id_rol

    db.commit()
    db.refresh(usuario)

    return {"mensaje": "Usuario actualizado correctamente"}

# Ruta para eliminar una cuenta
@rutero.delete("/{usuario_id}", response_model=schemas_usuario.UsuarioUpdate)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(modelo_usuario.Usuario).filter(modelo_usuario.Usuario.id_usuario == usuario_id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(usuario)
    db.commit()

    return {"mensaje": "Usuario eliminado correctamente"}

@rutero.put("/{id_usuario}/cambiar_contrasena")
def cambiar_contrasena(
        id_usuario: int,
        datos: schemas_usuario.CambiarContrasenaRequest,
        db: Session = Depends(get_db)):
    print("El id usuario es: ",id_usuario)

    print("El nuevo mdp usuario es: ", datos.contrasena)
    try:
        usuario = db.query(modelo_usuario.Usuario).filter(modelo_usuario.Usuario.id_usuario == id_usuario).first()
    except Exception as e:
        print("Error en la consulta:", e)
        raise HTTPException(status_code=500, detail="Error interno")

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    #usuario.contrasena = get_password_hash(nueva_contrasena)
    print("El id usuario es: ",usuario.id_usuario)
    print("El antiguo mdp usuario es: ",usuario.contrasena)
    print("El nuevo mdp usuario es: ",datos.contrasena)
    if datos.contrasena is not None:
        usuario.contrasena = hash_password(datos.contrasena)

    usuario.primer_acceso = False
    db.commit()
    db.refresh(usuario)
    return {"mensaje": "Contraseña actualizada con éxito"}
    #return JSONResponse( status_code = 200, content = {"mensaje": "Contraseña actualizada con éxito"} )

@rutero.put("/{id_usuario}/cambiar_contrasena_sin_body")
def cambiar_contrasena_sin_body(id_usuario: int, nueva_contrasena: str, db: Session = Depends(get_db)):
    print("El id usuario es: ",id_usuario)

    print("El nuevo mdp usuario es: ",nueva_contrasena)
    try:
        usuario = db.query(modelo_usuario.Usuario).filter(modelo_usuario.Usuario.id_usuario == id_usuario).first()
    except Exception as e:
        print("Error en la consulta:", e)
        raise HTTPException(status_code=500, detail="Error interno")

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    #usuario.contrasena = get_password_hash(nueva_contrasena)
    print("El id usuario es: ",usuario.id_usuario)
    print("El antiguo mdp usuario es: ",usuario.contrasena)
    print("El nuevo mdp usuario es: ",nueva_contrasena)
    if nueva_contrasena is not None:
        usuario.contrasena = hash_password(nueva_contrasena)

    usuario.primer_acceso = False
    db.commit()
    db.refresh(usuario)
    return {"mensaje": "Contraseña actualizada con éxito"}
