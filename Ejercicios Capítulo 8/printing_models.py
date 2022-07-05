# Ejercicio 8-15
# Se importan todas las funciones del módulo printing_functions (2 funciones).
from printing_functions import *
# Se crea una lista con modelos pendientes.
pendientes = ['legacy', 'tucson', 'ranger', 'mustang']
# Se crea una lista vacía para los modelos ya terminados.
terminados = []
# Se imprimen los modelos y se traspasan a la lista de terminados.
# NOTA: función importada desde el módulo.
print_models(pendientes, terminados)
# Se imprimen los elementos terminados.
# NOTA: función importada desde el módulo.
show_completed_models(terminados)
