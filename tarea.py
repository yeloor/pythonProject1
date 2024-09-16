def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante el período de tiempo especificado.

    :param temperaturas: Lista de diccionarios con temperaturas. Cada diccionario representa una semana y tiene
                         claves que son nombres de ciudades y valores que son listas de temperaturas diarias.
                         Ejemplo:
                         [
                             {'Ciudad1': [20, 22, 21, 23, 22, 24, 25], 'Ciudad2': [15, 16, 15, 17, 16, 18, 19], ...},
                             {'Ciudad1': [21, 23, 22, 24, 25, 26, 27], 'Ciudad2': [16, 17, 16, 18, 19, 20, 21], ...},
                             ...
                         ]
    :return: Diccionario con el promedio de temperatura para cada ciudad.
    """
    # Inicializamos un diccionario para almacenar las sumas y conteos
    suma_temperaturas = {}
    conteo_temperaturas = {}

    # Iteramos sobre cada semana en los datos
    for semana in temperaturas:
        for ciudad, temps in semana.items():
            if ciudad not in suma_temperaturas:
                suma_temperaturas[ciudad] = 0
                conteo_temperaturas[ciudad] = 0

            suma_temperaturas[ciudad] += sum(temps)
            conteo_temperaturas[ciudad] += len(temps)

    # Calculamos el promedio para cada ciudad
    promedio_temperaturas = {ciudad: suma / conteo_temperaturas[ciudad]
                             for ciudad, suma in suma_temperaturas.items()}

    return promedio_temperaturas


# Ejemplo de uso:
datos_temperaturas = [
    {'Ciudad1': [20, 22, 21, 23, 22, 24, 25], 'Ciudad2': [15, 16, 15, 17, 16, 18, 19]},
    {'Ciudad1': [21, 23, 22, 24, 25, 26, 27], 'Ciudad2': [16, 17, 16, 18, 19, 20, 21]},
    {'Ciudad1': [22, 24, 23, 25, 26, 27, 28], 'Ciudad2': [17, 18, 17, 19, 20, 21, 22]},
    {'Ciudad1': [23, 25, 24, 26, 27, 28, 29], 'Ciudad2': [18, 19, 18, 20, 21, 22, 23]}
]

resultado = calcular_temperatura_promedio(datos_temperaturas)
print(resultado)
