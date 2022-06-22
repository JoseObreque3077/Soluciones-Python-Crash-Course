# Ejercicio 7-10
# Paso 1: Se define un contador de encuestas que comienza en cero y una lista
# de lugares que almacenará las respuestas de las encuestas
contador = 0
lugares = []
# Paso 2: Se realizan 5 encuestas
while True:
    print('------ENCUESTA------')
    lugar = input('¿A que lugar te gustaría ir de vacaciones?: ').strip(
    ).title()
    lugares.append(lugar)
    print('------GRACIAS POR CONTESTAR------\n')
    contador += 1
    if contador == 5:
        break

# Paso 3: Se imprimen las respuestas por consola
print('------RESPUESTAS------')
for lugar in lugares:
    print(lugar)
