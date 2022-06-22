# Ejercicio 6-5
rios = {'Nilo': 'Egipto', 'Amazonas': 'Brasil', 'Yangtzé': 'China'}

# Se recorren los pares llave-valor del diccionario de ríos
for rio, pais in rios.items():
    print(f"El {rio} corre a través de {pais}.")

# Se recorren las llaves del diccionario de ríos
print("\nRíos almacenados:")
for rio in rios.keys():
    print(rio)

# Se recorren los valores del diccionario de ríos
print("\nPaíses almacenados:")
for pais in rios.values():
    print(pais)
