# Ejercicio 8-6
# Función que recibe un nombre de ciudad y un país y devuelve un mensaje
# del tipo ciudad, país.
def city_country(ciudad, pais):
    print(f"{ciudad.title()}, {pais.title()}")


# Se llama tres veces a la función
city_country('Santiago', 'chile')
city_country('Sao Paulo', 'Brasil')
city_country('San Francisco', 'Estados Unidos')
