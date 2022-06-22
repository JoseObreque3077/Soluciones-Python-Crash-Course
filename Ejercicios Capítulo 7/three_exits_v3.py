# Ejercicio 7-6 (versión 3)
# Se utiliza la sentencia "break"para romper el ciclo y detener el programa

while True:
    topping = input('Ingrese el topping a agregar a su pizza. Escriba "quit" '
                    'para salir. ').lower()
    if topping == 'quit':
        break
    else:
        print(f'Se ha agregado {topping} a su pizza!')
