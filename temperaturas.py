ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2

temperaturas = [
    [   # Quito
        [15, 16],
        [17, 18],
        [16, 17],
        [18, 19],
        [19, 20],
        [14, 15],
        [13, 14]
    ],
    [   # Guayaquil
        [27, 28],
        [29, 30],
        [28, 29],
        [30, 31],
        [31, 32],
        [26, 27],
        [25, 26]
    ],
    [   # Cuenca
        [12, 13],
        [14, 15],
        [13, 14],
        [15, 16],
        [16, 17],
        [11, 12],
        [10, 11]
    ]
]

for i in range(len(ciudades)):
    print(f"\nCiudad: {ciudades[i]}")
    for s in range(semanas):
        suma = 0
        for d in range(len(dias)):
            suma += temperaturas[i][d][s]
        promedio = suma / len(dias)
        print(f"  Semana {s+1}: Promedio de temperatura = {promedio:.2f}°C")
