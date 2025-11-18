from models.rutina_base import Rutina


RUTINAS_BALONCESTO = [
    # PRINCIPIANTE – GIMNASIO
    Rutina(
        deporte="Baloncesto",
        nivel="Principiante",
        tipo_sesion="Gimnasio",
        titulo="Fuerza básica para baloncesto",
        descripcion="Primeros pasos de fuerza para salto y bote.",
        duracion="30 min",
        pasos=[
            "Caminadora: 5 min",
            "Prensa: 3x12",
            "Extensión cuádriceps: 3x12",
            "Press militar: 3x10",
            "Remo sentado: 3x12"
        ]
    ),

    # PRINCIPIANTE – AIRE LIBRE
    Rutina(
        deporte="Baloncesto",
        nivel="Principiante",
        tipo_sesion="Aire libre",
        titulo="Fundamentos de bote",
        descripcion="Coordinación básica y tiro suave.",
        duracion="35 min",
        pasos=[
            "Bote mano dominante: 2 min",
            "Bote no dominante: 2 min",
            "Entradas: 10 por lado",
            "Tiros cortos: 20"
        ]
    ),

    # INTERMEDIO – GIMNASIO
    Rutina(
        deporte="Baloncesto",
        nivel="Intermedio",
        tipo_sesion="Gimnasio",
        titulo="Potencia de salto",
        descripcion="Fuerza + pliometría.",
        duracion="40 min",
        pasos=[
            "Sentadilla: 4x8",
            "Saltos verticales: 3x10",
            "Zancadas laterales: 3x12",
            "Press militar: 3x10"
        ]
    ),

    # INTERMEDIO – AIRE LIBRE
    Rutina(
        deporte="Baloncesto",
        nivel="Intermedio",
        tipo_sesion="Aire libre",
        titulo="Desplazamientos avanzados",
        descripcion="Agilidad y tiros en movimiento.",
        duracion="45 min",
        pasos=[
            "Desplazamientos laterales: 3 rondas",
            "Tiros en suspensión: 25",
            "1 vs 1 suave: 5-7 min"
        ]
    ),

    # AVANZADO – GIMNASIO
    Rutina(
        deporte="Baloncesto",
        nivel="Avanzado",
        tipo_sesion="Gimnasio",
        titulo="Explosividad profesional",
        descripcion="Salto y fuerza máxima.",
        duracion="50 min",
        pasos=[
            "Sentadilla pesada: 5x5",
            "Pliometría avanzada: 4x10",
            "Press militar pesado: 4x6"
        ]
    ),

    # AVANZADO – AIRE LIBRE
    Rutina(
        deporte="Baloncesto",
        nivel="Avanzado",
        tipo_sesion="Aire libre",
        titulo="Simulación de juego real",
        descripcion="Alta intensidad ofensiva y defensiva.",
        duracion="55 min",
        pasos=[
            "Bote explosivo",
            "Tiros en movimiento: 25",
            "Partido reducido: 8-10 min"
        ]
    ),
]
