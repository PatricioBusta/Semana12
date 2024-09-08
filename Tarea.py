# Definición de la matriz 3D que contiene las temperaturas diarias
# 3 ciudades, 7 días de la semana, 2 semanas
temperaturas = [
    [  # Ciudad 1
        [20, 22, 19, 21, 18, 20, 23],  # Semana 1 (Lunes-Domingo)
        [21, 19, 20, 22, 23, 24, 22]  # Semana 2
    ],
    [  # Ciudad 2
        [30, 32, 31, 29, 28, 30, 31],  # Semana 1
        [29, 28, 30, 32, 33, 31, 30]  # Semana 2
    ],
    [  # Ciudad 3
        [15, 16, 17, 16, 18, 17, 19],  # Semana 1
        [17, 18, 19, 20, 19, 21, 22]  # Semana 2
    ]
]

# Días de la semana
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in range(len(temperaturas)):
    print(f"\nCiudad {ciudad + 1}:")

    for semana in range(len(temperaturas[ciudad])):
        suma_temperaturas = 0
        dias = len(temperaturas[ciudad][semana])

        # Sumar las temperaturas de todos los días de la semana
        for dia in range(dias):
            suma_temperaturas += temperaturas[ciudad][semana][dia]

        # Calcular el promedio
        promedio = suma_temperaturas / dias
        print(f"  Semana {semana + 1}: Promedio de temperatura = {promedio:.2f}°C")
