# Ejercicio 8-4

# Paso 1: Definir la función que recibe detalles de una polera y retorna
# un mensaje informando sobre la información recibida
def make_shirt(talla='L', mensaje='I love Python'):
    print(f'Talla de la polera: {talla}')
    print(f'Mensaje a imprimir: {mensaje}\n')


# Paso 2: Llamada a la función usando argumentos posicionales
# (Valor por defecto para la talla y el mensaje)
make_shirt()
# Paso 3: Llamada a la función usando argumentos posicionales
# (Talla M y mensaje por defecto)
make_shirt(talla='M')
# Paso 4: Llamada a la función usando argumentos posicionales
# (Talla y mensaje definidos por el usuario)
make_shirt(talla='S', mensaje='Les traigo paz')
