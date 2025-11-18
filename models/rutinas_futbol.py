from models.rutina_base import Rutina


RUTINAS_FUTBOL = [
    # PRINCIPIANTE – GIMNASIO
    Rutina(
        deporte="Futbol",
        nivel="Principiante",
        tipo_sesion="Gimnasio",
        titulo="Fuerza básica para fútbol",
        descripcion="Ideal para comenzar a fortalecer piernas.",
        duracion="30 min",
        pasos=[
            "Caminadora suave: 5 min",
            "Sentadilla guiada: 3x12",
            "Prensa de piernas: 3x10",
            "Elevación de gemelos: 3x15",
            "Curl femoral: 3x12",
            "Plancha: 3x30s",
            "Estiramientos: 5 min"
        ],
        evitar_flags=["discapacidad_inferior"]
    ),

    # PRINCIPIANTE – AIRE LIBRE
    Rutina(
        deporte="Futbol",
        nivel="Principiante",
        tipo_sesion="Aire libre",
        titulo="Técnica básica y resistencia suave",
        descripcion="Control de balón y trote suave.",
        duracion="35 min",
        pasos=[
            "Trote suave: 8 min",
            "Conducción recta: 10 repeticiones",
            "Pases simples: 20",
            "Cambios suaves de dirección: 3 series",
            "Estiramiento final: 5 min"
        ]
    ),

    # INTERMEDIO – GIMNASIO
    Rutina(
        deporte="Futbol",
        nivel="Intermedio",
        tipo_sesion="Gimnasio",
        titulo="Potencia y fuerza funcional",
        descripcion="Mejora fuerza y aceleración.",
        duracion="40 min",
        pasos=[
            "Bicicleta: 5 min",
            "Sentadilla con barra: 4x8",
            "Peso muerto rumano: 3x10",
            "Zancadas: 3x12",
            "Saltos al cajón: 3x10",
            "Abdominales con rueda: 3x12"
        ],
        evitar_flags=["cardiaco"]
    ),

    # INTERMEDIO – AIRE LIBRE
    Rutina(
        deporte="Futbol",
        nivel="Intermedio",
        tipo_sesion="Aire libre",
        titulo="Velocidad y técnica avanzada",
        descripcion="Ejercicios de aceleración y precisión.",
        duracion="45 min",
        pasos=[
            "Progresiones de velocidad",
            "Sprints 20m: 6 reps",
            "Zig-zag entre conos: 3 series",
            "Pases largos: 20 reps",
            "Tiros a portería: 15"
        ]
    ),

    # AVANZADO – GIMNASIO
    Rutina(
        deporte="Futbol",
        nivel="Avanzado",
        tipo_sesion="Gimnasio",
        titulo="Explosividad máxima",
        descripcion="Fuerza avanzada para competición.",
        duracion="50 min",
        pasos=[
            "Sentadilla pesada: 5x5",
            "Peso muerto pesado: 4x6",
            "Pliometría avanzada: 4x10",
            "Sprints inclinados: 6 rondas",
            "Core avanzado: 4 rondas"
        ],
        evitar_flags=["cardiaco"]
    ),

    # AVANZADO – AIRE LIBRE
    Rutina(
        deporte="Futbol",
        nivel="Avanzado",
        tipo_sesion="Aire libre",
        titulo="Alta intensidad competitiva",
        descripcion="Simulación de juego real.",
        duracion="55 min",
        pasos=[
            "Trote medio: 5 min",
            "Sprints 30m: 10",
            "3 vs 3 reducido: 10 min",
            "Rondos: 5 min",
            "Tiros potentes: 20 reps"
        ]
    ),
]
