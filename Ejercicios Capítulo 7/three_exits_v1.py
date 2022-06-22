# Ejercicio 7-6 (versión 1)
# Se utiliza un test lógico en el ciclo while para detener el programa

topping = ''
while topping != 'quit':
    topping = input('Ingrese el topping a agregar a su pizza. Escriba "quit" '
                    'para salir. ').lower()
    if topping != 'quit':
        print(f'Se ha agregado {topping} a su pizza!')
    else:
        print('Programa finalizado.')
