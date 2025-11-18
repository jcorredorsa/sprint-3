import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, db
from models.usuario import Usuario

load_dotenv()

_firebase_initialized = False

def initialize_firebase():
    global _firebase_initialized
    if _firebase_initialized:
        return

    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    db_url = os.getenv("DATABASE_URL")

    if not cred_path:
        raise RuntimeError("Falta GOOGLE_APPLICATION_CREDENTIALS en .env")
    if not db_url:
        raise RuntimeError("Falta DATABASE_URL en .env")

    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred, {"databaseURL": db_url})

    _firebase_initialized = True


def guardar_usuario_en_firebase(usuario: Usuario):
    initialize_firebase()

    ref = db.reference("/Usuarios")

    data = {
        "nombre": usuario.nombre,
        "contrasena": usuario.contrasena,
        "genero": usuario.genero,
        "deporte": usuario.deporte,
        "edad": usuario.edad,
        "nivel": usuario.nivel,
        "complicacion": usuario.complicacion
    }

    ref.child(usuario.nombre).set(data)
    return data


def obtener_usuario_desde_firebase(nombre: str):
    initialize_firebase()
    ref = db.reference("/Usuarios")
    return ref.child(nombre).get()
