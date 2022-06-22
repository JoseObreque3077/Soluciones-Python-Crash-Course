# Ejercicio 7-6 (versión 2)
# Se utiliza un flag en el ciclo while para detener el programa

activo = True
while activo:
    topping = input('Ingrese el topping a agregar a su pizza. Escriba "quit" '
                    'para salir. ').lower()
    if topping != 'quit':
        print(f'Se ha agregado {topping} a su pizza!')
    else:
        print('Programa finalizado.')
        activo = False
