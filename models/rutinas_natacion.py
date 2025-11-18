from models.rutina_base import Rutina


RUTINAS_NATACION = [

    # PRINCIPIANTE – GIMNASIO
    Rutina(
        deporte="Natacion",
        nivel="Principiante",
        tipo_sesion="Gimnasio",
        titulo="Fortalecimiento básico para nadadores",
        descripcion="Fortalece espalda, hombros y core.",
        duracion="30 min",
        pasos=[
            "Jalón al pecho: 3x12",
            "Remo sentado: 3x12",
            "Rotadores externos con banda: 3x15",
            "Plancha: 3x25s",
            "Estiramiento de dorsales: 3 min"
        ],
        evitar_flags=["discapacidad_superior"]
    ),

    # PRINCIPIANTE – PISCINA
    Rutina(
        deporte="Natacion",
        nivel="Principiante",
        tipo_sesion="Piscina",
        titulo="Bases del estilo crol",
        descripcion="Aprende flotación, respiración y patada.",
        duracion="40 min",
        pasos=[
            "Flotación ventral: 3 min",
            "Patada con tabla: 4x25m",
            "Respiración bilateral: 3x25m",
            "Crol suave: 4x25m"
        ],
        evitar_flags=["respiratorio"]
    ),

    # INTERMEDIO – GIMNASIO
    Rutina(
        deporte="Natacion",
        nivel="Intermedio",
        tipo_sesion="Gimnasio",
        titulo="Fuerza y estabilidad del tronco",
        descripcion="Mejora velocidad y técnica.",
        duracion="40 min",
        pasos=[
            "Pull-over con mancuerna: 3x12",
            "Remo de pie cuerda: 3x12",
            "Plancha lateral: 3x30s",
            "Elevaciones frontales: 3x12"
        ]
    ),

    # INTERMEDIO – PISCINA
    Rutina(
        deporte="Natacion",
        nivel="Intermedio",
        tipo_sesion="Piscina",
        titulo="Nado continuo moderado",
        descripcion="Coordina brazada + respiración + patada.",
        duracion="45 min",
        pasos=[
            "Crol 50m suave: 2 repeticiones",
            "Crol técnica 25m: 4 repeticiones",
            "Crol ritmo medio 50m: 3 repeticiones",
            "Patada lateral: 4x25m"
        ],
        evitar_flags=["cardiaco"]
    ),

    # AVANZADO – GIMNASIO
    Rutina(
        deporte="Natacion",
        nivel="Avanzado",
        tipo_sesion="Gimnasio",
        titulo="Potencia máxima de brazada",
        descripcion="Ideal para nadadores competitivos.",
        duracion="50 min",
        pasos=[
            "Jalón al pecho pesado: 5x6",
            "Remo curvo pesado: 4x6",
            "Core con polea: 4x15",
            "Rotación explosiva: 4x12"
        ]
    ),

    # AVANZADO – PISCINA
    Rutina(
        deporte="Natacion",
        nivel="Avanzado",
        tipo_sesion="Piscina",
        titulo="Entrenamiento de velocidad",
        descripcion="Máxima velocidad y técnica competitiva.",
        duracion="55 min",
        pasos=[
            "25m velocidad: 6 repeticiones",
            "50m velocidad: 4 repeticiones",
            "Salidas explosivas: 10 repeticiones",
            "Virajes rápidos: 4 rondas"
        ],
        evitar_flags=["cardiaco"]
    ),
]
