# Ejercicio 4-13

# tupla: similar a una lista, pero inmutable
menu = ("pizza", "lasagna", "cannoli", "spaghetti", "ravioli")
print("Menú Original:")
for comida in menu:
    print(comida.title())
# Como los elementos de una tupla no pueden ser modificados,
# entonces toda la tupla debe ser sustituida para realizar cambios
menu = ("pizza", "lasagna", "gnocci", "fetuccini", "ravioli")
print("\nCambios en el menú:")
for comida in menu:
    print(comida.title())
