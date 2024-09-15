import numpy as np

def calcular_temperatura_promedio(temperaturas):

    # Número de ciudades y semanas
    num_ciudades = temperaturas.shape[0]
    num_semanas = temperaturas.shape[2]

    # Inicializamos un arreglo para almacenar los promedios
    promedios = np.zeros(num_ciudades)

    # Calculamos el promedio de temperaturas para cada ciudad
    for i in range(num_ciudades):
        promedios[i] = np.mean(temperaturas[i, :, :])  # Promedio de todas las semanas y días

    return promedios

# Definimos las ciudades, días de la semana y semanas
ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C']
dias_de_la_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4  # Número de semanas

# Creamos una matriz 3D de temperaturas aleatorias entre 15 y 30 grados
temperaturas = np.random.randint(15, 31, size=(len(ciudades), len(dias_de_la_semana), semanas))

# Mostramos la matriz de temperaturas
print("Matriz de Temperaturas (Ciudades x Días x Semanas):")
print(temperaturas)

# Llamamos a la función para calcular los promedios
promedios = calcular_temperatura_promedio(temperaturas)

# Mostramos los promedios
print("\nPromedio de Temperaturas por Ciudad:")
for i in range(len(ciudades)):
    print(f"{ciudades[i]}: {promedios[i]:.2f} °C")