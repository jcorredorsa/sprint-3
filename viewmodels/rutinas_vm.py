# viewmodels/rutinas_vm.py

from models.rutinas import RUTINAS
from models.usuario import Usuario
from models.firebase import guardar_usuario_en_firebase, obtener_usuario_desde_firebase


# ---- Traduce el valor del radio de experiencia (a, b, c) a texto ----
def mapear_experiencia(valor):
    if valor == "a":
        return "Principiante"
    if valor == "b":
        return "Intermedio"
    if valor == "c":
        return "Avanzado"
    # Por si en algún momento ya viene en texto
    return valor


# ---- Traduce texto de complicación a flags internos ----
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


# ---- Crea el usuario a partir del formulario de Encuesta ----
def crear_usuario_desde_form(form):

    nombre = form["usuario"]
    contrasena = form["contrasena"]
    genero = form["genero"]
    deporte = form["deporte"]           # Futbol / Baloncesto / Natacion / Tenis
    edad = int(form["edad"])

    experiencia_valor = form["experiencia"]   # a / b / c
    nivel = mapear_experiencia(experiencia_valor)

    complicaciones_si_no = form["complicaciones"]  # "si" o "no"
    tipo_comp = form.get("tipoComplicacion", "")

    if complicaciones_si_no == "si" and tipo_comp:
        complicacion = tipo_comp
    else:
        complicacion = ""

    usuario = Usuario(
        nombre=nombre,
        contrasena=contrasena,
        genero=genero,
        deporte=deporte,
        edad=edad,
        nivel=nivel,
        complicacion=complicacion
    )

    # Guardar en Firebase
    guardar_usuario_en_firebase(usuario)
    return usuario


# ---- Obtiene todas las rutinas válidas para ese usuario ----
def obtener_rutinas_para_usuario(nombre_usuario: str):

    data = obtener_usuario_desde_firebase(nombre_usuario)

    if not data:
        # Si no existe el usuario en Firebase devolvemos algo vacío
        return {
            "deporte": "",
            "nivel": "",
            "complicacion": "",
            "rutinas": []
        }

    deporte = data["deporte"]
    nivel = data["nivel"]                   # Aquí ya viene "Principiante", "Intermedio" o "Avanzado"
    complicacion = data.get("complicacion", "")

    user_flags = obtener_flags(complicacion)

    # 1. Filtrar por deporte
    filtrado = [r for r in RUTINAS if r.deporte == deporte]

    # 2. Filtrar por nivel
    filtrado = [r for r in filtrado if r.nivel == nivel]

    # 3. Filtrar por flags de salud/discapacidad
    def es_valida(rutina):
        for f in user_flags:
            if f in rutina.evitar_flags:
                return False
        return True

    rutinas_finales = [r for r in filtrado if es_valida(r)]

    return {
        "deporte": deporte,
        "nivel": nivel,
        "complicacion": complicacion,
        "rutinas": rutinas_finales
    }
