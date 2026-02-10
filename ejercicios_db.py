"""
Base de datos de ejercicios
Cada ejercicio tiene:
- nombre: nombre del ejercicio
- categoria: tren_superior, tren_inferior, core, push, pull
- musculos: músculos principales trabajados
- equipamiento: qué necesitas
- series: sugerencia de series
- reps: sugerencia de repeticiones
- imagen_url: URL de imagen demostrativa
"""

EJERCICIOS_CORE = [
    {
        "nombre": "Deadbug con Pesa",
        "series": 2,
        "reps": "12 (6 por lado)",
        "musculos": ["core", "estabilización"],
        "equipamiento": "mancuerna",
        "imagen_url": "https://images.squarespace-cdn.com/content/v1/5ffcea9416aee143500ea103/1638667309343-DDMZXBHGBP4X4P3T3X0L/Weighted+Dead+Bug.jpg"
    },
    {
        "nombre": "Sit-ups con Pesa (Copa)",
        "series": 1,
        "reps": "15",
        "musculos": ["abdominales", "core"],
        "equipamiento": "disco o mancuerna",
        "imagen_url": "https://i.pinimg.com/originals/cb/30/00/cb3000c5e2e5e1b7f5fdc6e7d0b2b3a5.jpg"
    },
    {
        "nombre": "Plank Pull-Through",
        "series": 2,
        "reps": "12 (6 por lado)",
        "musculos": ["core", "oblicuos", "estabilización"],
        "equipamiento": "mancuerna",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/09/plank-pull-through.gif"
    },
    {
        "nombre": "Halo (Kettlebell o Mancuerna)",
        "series": 2,
        "reps": "10 (5 por lado)",
        "musculos": ["core", "hombros", "movilidad"],
        "equipamiento": "kettlebell o mancuerna",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/10/kettlebell-halo.gif"
    },
    {
        "nombre": "Toe Touches (Toque de pies)",
        "series": 1,
        "reps": "15-20",
        "musculos": ["abdominales superiores"],
        "equipamiento": "ninguno",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/toe-touch-crunch.gif"
    },
    {
        "nombre": "Russian Twists (Giros rusos)",
        "series": 1,
        "reps": "20 (10 por lado)",
        "musculos": ["oblicuos", "core"],
        "equipamiento": "disco o mancuerna",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/russian-twist.gif"
    }
]

EJERCICIOS_PUSH = [
    # PECHO
    {
        "nombre": "Press de Banca con Barra",
        "categoria": "push",
        "musculos": ["pecho", "tríceps", "hombros"],
        "equipamiento": "barra y banco",
        "series": 3,
        "reps": "8-10",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/barbell-bench-press.gif"
    },
    {
        "nombre": "Press de Banca con Mancuernas",
        "categoria": "push",
        "musculos": ["pecho", "tríceps", "estabilización"],
        "equipamiento": "mancuernas y banco",
        "series": 3,
        "reps": "10-12",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2021/10/dumbbell-bench-press.gif"
    },
    {
        "nombre": "Aperturas con Mancuernas",
        "categoria": "push",
        "musculos": ["pecho"],
        "equipamiento": "mancuernas y banco",
        "series": 3,
        "reps": "12-15",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/09/dumbbell-chest-fly.gif"
    },
    {
        "nombre": "Flexiones (Push-ups)",
        "categoria": "push",
        "musculos": ["pecho", "tríceps", "core"],
        "equipamiento": "ninguno",
        "series": 3,
        "reps": "10-15",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2021/06/push-up.gif"
    },
    # TRÍCEPS
    {
        "nombre": "Press Francés con Barra",
        "categoria": "push",
        "musculos": ["tríceps"],
        "equipamiento": "barra y banco",
        "series": 3,
        "reps": "10-12",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/barbell-skull-crusher.gif"
    },
    {
        "nombre": "Extensiones de Tríceps en Polea",
        "categoria": "push",
        "musculos": ["tríceps"],
        "equipamiento": "polea",
        "series": 3,
        "reps": "12-15",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/cable-tricep-pushdown.gif"
    },
    {
        "nombre": "Fondos en Banco (Dips)",
        "categoria": "push",
        "musculos": ["tríceps", "pecho", "hombros"],
        "equipamiento": "banco",
        "series": 3,
        "reps": "10-12",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/bench-dip.gif"
    },
    # HOMBROS
    {
        "nombre": "Press Militar con Mancuernas",
        "categoria": "push",
        "musculos": ["hombros", "tríceps"],
        "equipamiento": "mancuernas",
        "series": 3,
        "reps": "10-12",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2021/06/dumbbell-shoulder-press.gif"
    },
    {
        "nombre": "Elevaciones Laterales",
        "categoria": "push",
        "musculos": ["hombros laterales"],
        "equipamiento": "mancuernas",
        "series": 3,
        "reps": "12-15",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2021/06/dumbbell-lateral-raise.gif"
    },
    {
        "nombre": "Elevaciones Frontales",
        "categoria": "push",
        "musculos": ["hombros frontales"],
        "equipamiento": "mancuernas o disco",
        "series": 3,
        "reps": "12-15",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/dumbbell-front-raise.gif"
    }
]

EJERCICIOS_PULL = [
    # ESPALDA
    {
        "nombre": "Dominadas (Pull-ups)",
        "categoria": "pull",
        "musculos": ["espalda dorsal", "bíceps"],
        "equipamiento": "barra de dominadas",
        "series": 3,
        "reps": "6-10",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2021/10/pull-up.gif"
    },
    {
        "nombre": "Remo con Barra",
        "categoria": "pull",
        "musculos": ["espalda media", "bíceps"],
        "equipamiento": "barra",
        "series": 3,
        "reps": "8-10",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/03/barbell-bent-over-row.gif"
    },
    {
        "nombre": "Remo con Mancuerna (1 brazo)",
        "categoria": "pull",
        "musculos": ["espalda", "bíceps"],
        "equipamiento": "mancuerna y banco",
        "series": 3,
        "reps": "10-12 por lado",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/09/one-arm-dumbbell-row.gif"
    },
    {
        "nombre": "Jalón al Pecho (Lat Pulldown)",
        "categoria": "pull",
        "musculos": ["espalda dorsal", "bíceps"],
        "equipamiento": "máquina de poleas",
        "series": 3,
        "reps": "10-12",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2021/10/lat-pulldown.gif"
    },
    {
        "nombre": "Remo en Máquina",
        "categoria": "pull",
        "musculos": ["espalda media", "trapecios"],
        "equipamiento": "máquina de remo",
        "series": 3,
        "reps": "10-12",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/cable-seated-row.gif"
    },
    {
        "nombre": "Face Pulls (Polea)",
        "categoria": "pull",
        "musculos": ["hombros posteriores", "trapecios"],
        "equipamiento": "polea",
        "series": 3,
        "reps": "15-20",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/cable-face-pull.gif"
    },
    # BÍCEPS
    {
        "nombre": "Curl con Barra",
        "categoria": "pull",
        "musculos": ["bíceps"],
        "equipamiento": "barra",
        "series": 3,
        "reps": "10-12",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2021/06/barbell-curl.gif"
    },
    {
        "nombre": "Curl con Mancuernas",
        "categoria": "pull",
        "musculos": ["bíceps"],
        "equipamiento": "mancuernas",
        "series": 3,
        "reps": "10-12",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/10/dumbbell-curl.gif"
    },
    {
        "nombre": "Curl Martillo",
        "categoria": "pull",
        "musculos": ["bíceps", "antebrazos"],
        "equipamiento": "mancuernas",
        "series": 3,
        "reps": "10-12",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/10/hammer-curl.gif"
    },
    {
        "nombre": "Curl en Polea",
        "categoria": "pull",
        "musculos": ["bíceps"],
        "equipamiento": "polea",
        "series": 3,
        "reps": "12-15",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/03/cable-curl.gif"
    }
]

EJERCICIOS_PIERNAS = [
    {
        "nombre": "Sentadillas con Barra",
        "categoria": "tren_inferior",
        "musculos": ["cuádriceps", "glúteos", "core"],
        "equipamiento": "barra",
        "series": 4,
        "reps": "8-10",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2021/10/barbell-squat.gif"
    },
    {
        "nombre": "Prensa de Piernas",
        "categoria": "tren_inferior",
        "musculos": ["cuádriceps", "glúteos"],
        "equipamiento": "máquina de prensa",
        "series": 3,
        "reps": "10-12",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/leg-press.gif"
    },
    {
        "nombre": "Peso Muerto Rumano",
        "categoria": "tren_inferior",
        "musculos": ["isquiotibiales", "glúteos", "espalda baja"],
        "equipamiento": "barra o mancuernas",
        "series": 3,
        "reps": "8-10",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/barbell-romanian-deadlift.gif"
    },
    {
        "nombre": "Zancadas con Mancuernas",
        "categoria": "tren_inferior",
        "musculos": ["cuádriceps", "glúteos", "equilibrio"],
        "equipamiento": "mancuernas",
        "series": 3,
        "reps": "10-12 por pierna",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/dumbbell-lunge.gif"
    },
    {
        "nombre": "Extensiones de Cuádriceps",
        "categoria": "tren_inferior",
        "musculos": ["cuádriceps"],
        "equipamiento": "máquina",
        "series": 3,
        "reps": "12-15",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/leg-extension.gif"
    },
    {
        "nombre": "Curl de Isquiotibiales",
        "categoria": "tren_inferior",
        "musculos": ["isquiotibiales"],
        "equipamiento": "máquina",
        "series": 3,
        "reps": "12-15",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/leg-curl.gif"
    },
    {
        "nombre": "Elevaciones de Gemelos",
        "categoria": "tren_inferior",
        "musculos": ["gemelos"],
        "equipamiento": "máquina o mancuernas",
        "series": 3,
        "reps": "15-20",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/calf-raise.gif"
    },
    {
        "nombre": "Sentadilla Búlgara",
        "categoria": "tren_inferior",
        "musculos": ["cuádriceps", "glúteos", "equilibrio"],
        "equipamiento": "mancuernas y banco",
        "series": 3,
        "reps": "10-12 por pierna",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/bulgarian-split-squat.gif"
    },
    {
        "nombre": "Hip Thrust (Puente de glúteos)",
        "categoria": "tren_inferior",
        "musculos": ["glúteos", "isquiotibiales"],
        "equipamiento": "barra y banco",
        "series": 3,
        "reps": "10-12",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/02/barbell-hip-thrust.gif"
    }
]

# Ejercicios de movilidad/calentamiento
EJERCICIOS_MOVILIDAD = [
    {
        "nombre": "Rotaciones de Hombros",
        "musculos": ["hombros", "movilidad"],
        "series": 2,
        "reps": "10 por dirección",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2022/11/shoulder-circles.gif"
    },
    {
        "nombre": "Cat-Cow (Gato-Vaca)",
        "musculos": ["columna", "movilidad"],
        "series": 2,
        "reps": "10-12",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2023/05/cat-cow-stretch.gif"
    },
    {
        "nombre": "World's Greatest Stretch",
        "musculos": ["cadera", "hombros", "movilidad"],
        "series": 2,
        "reps": "5 por lado",
        "imagen_url": "https://www.inspireusafoundation.org/wp-content/uploads/2023/05/worlds-greatest-stretch.gif"
    }
]
