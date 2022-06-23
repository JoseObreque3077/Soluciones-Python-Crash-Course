# Ejercicio 8-3

# Paso 1: Definir la función que recibe detalles de una polera y retorna
# un mensaje informando sobre la información recibida
def make_shirt(talla, mensaje):
    print(f'Talla de la polera: {talla}')
    print(f'Mensaje a imprimir: {mensaje}\n')


# Paso 2: Llamada a la función usando argumentos posicionales
make_shirt('S', 'I LOVE PYTHON')
# Paso 3: Llamada a la función usando argumentos palabra clave
make_shirt(talla='XL', mensaje='HOLA MUNDO')
