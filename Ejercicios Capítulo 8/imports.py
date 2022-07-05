# Ejercicio 8-16

# Importación 1
import imports_functions

imports_functions.crear_sandwich('salame', 'lechuga', 'tomate', 'mayonesa')

# Importación 2
from imports_functions import crear_sandwich
print('')
crear_sandwich('salame', 'lechuga', 'tomate', 'mayonesa')

# Importación 3
from imports_functions import crear_sandwich as fn
print('')
fn('salame', 'lechuga', 'tomate', 'mayonesa')

# Importación 4
import imports_functions as mn
print('')
mn.crear_sandwich('salame', 'lechuga', 'tomate', 'mayonesa')

# Importación 5
from imports_functions import *
print('')
crear_sandwich('salame', 'lechuga', 'tomate', 'mayonesa')
