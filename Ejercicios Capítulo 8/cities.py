# Ejercicio 8-5
# Paso 1: Se define la función que recibe una ciudad y un país
# y retorna un mensaje personalizado.
def describe_city(ciudad, pais='Francia'):
    print(f'{ciudad.title()} se encuentra en {pais.title()}\n')


# Paso 2: Llamado a la función (país por defecto)
describe_city(ciudad='París')
# Paso 3: Llamado a la función (sin usar valores por defecto)
describe_city(ciudad='Villarrica', pais='Chile')
describe_city(ciudad='Washington D.C.', pais='Estados Unidos')
