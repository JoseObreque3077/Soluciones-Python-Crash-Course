# Ejercicio 7-5
while True:
    edad = input('Ingrese su edad. Al terminar, escriba "quit" para salir. ')
    if edad.lower() == 'quit':
        break
    edad = int(edad)
    if edad < 3:
        print('Entrada gratuita.')
    elif 3 <= edad <= 12:
        print('Su entrada cuesta $10.')
    else:
        print('Su entrada cuesta $15.')
