# Ejercicio 7-4

# Este ciclo while se ejecuta permanentemente
while True:
    # Se almacena el topping a agregar en una variable (string)
    topping = input('Ingrese el topping a agregar a su pizza. Escriba "quit" '
                    'para salir. ').lower()
    # Si el usuario ingresa la palabra "quit" se rompe el ciclo
    if topping == 'quit':
        break
    else:
        # Si el usuario ingresa algo distinto a "quit", se imprime el topping
        # y se continúa con la ejecución del programa
        print(f'Se ha agregado {topping} a su pizza!')
