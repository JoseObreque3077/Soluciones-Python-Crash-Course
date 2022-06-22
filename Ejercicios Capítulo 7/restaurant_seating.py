# Ejercicio 7-2
# Se almacena la respuesta como String
num_personas = input('¿Cuantas personas son en su grupo para cenar?')
# Se transforma el valor en String a un entero
num_personas = int(num_personas)
# Se utiliza el valor entero para hacer la consulta lógica
if num_personas>8:
    print('Deberán esperar a que se desocupe una mesa')
else:
    print('Adelante, su mesa está lista')
