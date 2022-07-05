# Ejercicio 8-14

# Función que almacena marca, modelo e info adicional de un auto, en un
# diccionario. La info adicional se ingresa como par llave-valor en los
# parámetros de entrada.

def perfil_auto(marca, modelo, **info_auto):
    info_auto['marca'] = marca
    info_auto['modelo'] = modelo
    return info_auto


auto = perfil_auto(marca='Ford',
                   modelo='Ranger',
                   color='negro',
                   combustible='petróleo')
print(auto)
