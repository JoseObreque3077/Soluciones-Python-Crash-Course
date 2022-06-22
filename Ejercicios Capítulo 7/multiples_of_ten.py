# Ejercicio 7-3
# Se almacena la respuesta por teclado como String
numero = input('Ingrese un número entero: ')
# Se transforma el valor almacenado a entero
numero = int(numero)
# Se usa el módulo para saber si el número entero es múltiplo de 10 o no
if numero % 10 == 0:
    print(f'{numero} es múltiplo de 10')
else:
    print(f'{numero} no es múltiplo de 10')
