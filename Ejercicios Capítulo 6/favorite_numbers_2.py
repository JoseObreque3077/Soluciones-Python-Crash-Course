# Ejercicio 6-10
datos = {'Javier': [7, 11, 17],
         'Liliana': [32, 5, 1],
         'Constanza': [11, 9],
         'Gabriel': [5, 69],
         'José': [7, 21, 32, 44]}
for nombre, numeros in datos.items():
    print(f'Nombre: {nombre}')
    print('Sus números favoritos son:')
    for numero in numeros:
        print(numero)
    print('')
