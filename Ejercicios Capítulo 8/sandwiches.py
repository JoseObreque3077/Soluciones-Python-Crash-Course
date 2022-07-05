# Ejercicio 8-12
# Definición de función que recibe un número arbitrario de ingredientes para
# "crear" un sandwich (como parámetros de entrada).
def crear_sandwich(*ingredientes):
    for ingrediente in ingredientes:
        print(ingrediente.title())


print('Sandwich 1:')
crear_sandwich('tocino', 'carne de vacuno', 'lechuga', 'tomate')
print('\nSandwich 2:')
crear_sandwich('peperoni', 'chucrut', 'mayonesa')
print('\nSandwich 3:')
crear_sandwich('pollo', 'salsa teriyaki', 'lechuga')
