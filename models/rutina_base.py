# models/rutina_base.py
from dataclasses import dataclass, field
from typing import List

@dataclass
class Rutina:
    deporte: str
    nivel: str
    tipo_sesion: str
    titulo: str
    descripcion: str
    duracion: str
    pasos: List[str]
    evitar_flags: List[str] = field(default_factory=list)
