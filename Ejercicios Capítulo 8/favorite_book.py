# Ejercicio 8-2

# Paso 1: Definición de la función que recibe un título de libro y devuelve
# un mensaje por pantalla.
def favorite_book(titulo):
    print(f'Mi libro favorito es "{titulo.strip().title()}".')


# Paso 2: Se llama a la función pasándole un título de libro como parámetro
favorite_book('El resplandor')
