from models.rutina_base import Rutina
from models.usuario import Usuario
from models.firebase import guardar_usuario_en_firebase, obtener_usuario_desde_firebase
from models.rutinas_futbol import RUTINAS_FUTBOL
from models.rutinas_baloncesto import RUTINAS_BALONCESTO
from models.rutinas_natacion import RUTINAS_NATACION
from models.rutinas_tenis import RUTINAS_TENIS
from static.img.imagenes_ejercicios import IMAGENES_EJERCICIOS, GIF_POR_DEFECTO

# Unificar todas las rutinas
TODAS_LAS_RUTINAS = (
    RUTINAS_FUTBOL +
    RUTINAS_BALONCESTO +
    RUTINAS_NATACION +
    RUTINAS_TENIS
)


def mapear_experiencia(valor):
    if valor == "a":
        return "Principiante"
    if valor == "b":
        return "Intermedio"
    if valor == "c":
        return "Avanzado"
    return valor

def obtener_flags(complicacion):
    c = (complicacion or "").lower()
    flags = []
    if "inferior" in c or "motriz" in c:
        flags.append("discapacidad_inferior")
    if "superior" in c:
        flags.append("discapacidad_superior")
    if "cardio" in c:
        flags.append("cardiaco")
    if "respira" in c or "asma" in c:
        flags.append("respiratorio")
    if "lesion" in c or "articular" in c:
        flags.append("lesion_articular")
    return flags

def crear_usuario_desde_form(form):
    nombre = form["usuario"]
    contrasena = form["contrasena"]
    genero = form["genero"]
    deporte = form["deporte"]
    edad_str = form.get("edad", "").strip()
    try:
        edad = int(edad_str)
    except (ValueError, TypeError):
        edad = 0
    nivel = mapear_experiencia(form["experiencia"])
    complicacion = form.get("tipoComplicacion", "") if form["complicaciones"] == "si" else ""

    usuario = Usuario(
        nombre=nombre,
        contrasena=contrasena,
        genero=genero,
        deporte=deporte,
        edad=edad,
        nivel=nivel,
        complicacion=complicacion
    )
    guardar_usuario_en_firebase(usuario)
    return usuario

def asignar_gif_a_pasos(rutina: Rutina):
    nuevos_pasos = []

    for paso in rutina.pasos:
        if isinstance(paso, dict):
            nombre = paso.get("nombre", "").strip()
            detalle = paso.get("detalle", "").strip()
        else:
            # Separar nombre y detalle si es un string plano tipo "Ejercicio: 3x12"
            if ":" in paso:
                nombre, detalle = map(str.strip, paso.split(":", 1))
            else:
                nombre = paso.strip()
                detalle = ""

        clave_encontrada = None
        paso_lower = nombre.lower()

        for clave in IMAGENES_EJERCICIOS.keys():
            if clave in paso_lower:
                clave_encontrada = clave
                break

        gif = IMAGENES_EJERCICIOS.get(clave_encontrada, GIF_POR_DEFECTO)

        nuevos_pasos.append({
            "nombre": nombre,
            "detalle": detalle,
            "gif": gif
        })

    rutina.pasos = nuevos_pasos
    return rutina


def asignar_imagen_a_rutina(rutina: Rutina):
    texto = (rutina.titulo + " " + " ".join(p['nombre'] for p in rutina.pasos)).lower()
    for clave, archivo in IMAGENES_EJERCICIOS.items():
        if clave in texto:
            rutina.imagen = archivo
            return rutina
    rutina.imagen = GIF_POR_DEFECTO
    return rutina

def obtener_rutinas_para_usuario(nombre_usuario: str):
    data = obtener_usuario_desde_firebase(nombre_usuario)
    if not data:
        return {"deporte": "", "nivel": "", "complicacion": "", "rutinas": []}

    deporte = data["deporte"]
    nivel = data["nivel"]
    complicacion = data.get("complicacion", "")
    user_flags = obtener_flags(complicacion)

    rutinas_usuario = [
        r for r in TODAS_LAS_RUTINAS
        if r.deporte == deporte and r.nivel == nivel and all(f not in r.evitar_flags for f in user_flags)
    ]

    rutinas_con_imagen = [
        asignar_imagen_a_rutina(asignar_gif_a_pasos(r)) for r in rutinas_usuario
    ]

    return {
        "deporte": deporte,
        "nivel": nivel,
        "complicacion": complicacion,
        "rutinas": rutinas_con_imagen
    }
