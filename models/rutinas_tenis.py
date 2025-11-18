from models.rutina_base import Rutina


RUTINAS_TENIS = [

    # PRINCIPIANTE – GIMNASIO
    Rutina(
        deporte="Tenis",
        nivel="Principiante",
        tipo_sesion="Gimnasio",
        titulo="Fuerza básica del tren superior",
        descripcion="Fortalece hombros, brazo y core.",
        duracion="35 min",
        pasos=[
            "Press de pecho: 3x12",
            "Remo con mancuerna: 3x12",
            "Rotadores con banda: 3x15",
            "Plancha lateral: 3x20s",
            "Trabajo de muñeca: 3x12"
        ],
        evitar_flags=["discapacidad_superior"]
    ),

    # PRINCIPIANTE – AIRE LIBRE
    Rutina(
        deporte="Tenis",
        nivel="Principiante",
        tipo_sesion="Aire libre",
        titulo="Golpes básicos",
        descripcion="Coordinación y técnica inicial.",
        duracion="40 min",
        pasos=[
            "Derecha sin bola: 20 reps",
            "Revés sin bola: 20 reps",
            "Derecha suave: 15 reps",
            "Mini rally suave: 5 min"
        ]
    ),

    # INTERMEDIO – GIMNASIO
    Rutina(
        deporte="Tenis",
        nivel="Intermedio",
        tipo_sesion="Gimnasio",
        titulo="Fuerza explosiva",
        descripcion="Incrementa potencia en golpes.",
        duracion="45 min",
        pasos=[
            "Press militar: 4x10",
            "Remo barra T: 4x8",
            "Rotación con polea: 4x10 por lado",
            "Abdominales: 3x20"
        ]
    ),

    # INTERMEDIO – AIRE LIBRE
    Rutina(
        deporte="Tenis",
        nivel="Intermedio",
        tipo_sesion="Aire libre",
        titulo="Movilidad avanzada",
        descripcion="Golpes en movimiento y velocidad.",
        duracion="45 min",
        pasos=[
            "Steps laterales: 3 rondas",
            "Forehand en movimiento: 20 reps",
            "Backhand en movimiento: 20 reps",
            "Peloteo medio fondo: 8 min"
        ]
    ),

    # AVANZADO – GIMNASIO
    Rutina(
        deporte="Tenis",
        nivel="Avanzado",
        tipo_sesion="Gimnasio",
        titulo="Rotación explosiva competitiva",
        descripcion="Fuerza pesada para jugadores avanzados.",
        duracion="50 min",
        pasos=[
            "Sentadilla pesada: 5x5",
            "Peso muerto: 4x6",
            "Rotación explosiva balón medicinal: 4x12",
            "Press militar pesado: 4x6"
        ],
        evitar_flags=["lesion_articular"]
    ),

    # AVANZADO – AIRE LIBRE
    Rutina(
        deporte="Tenis",
        nivel="Avanzado",
        tipo_sesion="Aire libre",
        titulo="Simulación competitiva",
        descripcion="El mismo ritmo que un partido real.",
        duracion="55 min",
        pasos=[
            "Peloteo intenso: 6 min",
            "Derecha de ataque: 15 reps",
            "Revés cruzado: 15 reps",
            "Subida a la red + volea: 15 reps",
            "Simulación tie-break: 10 min"
        ]
    ),
]
