from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    contrasena: str
    genero: str
    deporte: str
    edad: int
    nivel: str
    complicacion: str
