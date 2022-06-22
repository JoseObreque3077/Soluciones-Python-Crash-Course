# Ejercicio 7-9
# Paso 1: Creación de lista con órdenes de sandwiches
sandwich_orders = ['pastrami',
                   'atún',
                   'pollo BBQ',
                   'pastrami',
                   'pollo teriyaki',
                   'vegetariano',
                   'salame',
                   'pastrami']
# Paso 2: Creación de lista vacía para almacenar sandwiches preparados
finished_sandwich = []

# Paso 3: Mostrar mensaje indicando que se agotó el pastrami
print('Se ha agotado el pastrami!')

# Paso 4: Eliminación de ocurrencias de 'pastrami' en la lista sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Paso 5: Transferencia de elementos de la lista de órdenes a la lista de
# sandwiches preparados
while sandwich_orders:
    actual_sandwich = sandwich_orders.pop(0)
    print(f'Se ha preparado un sandwich de {actual_sandwich}')
    finished_sandwich.append(actual_sandwich)

# Paso 6: Mostrar en pantalla la lista de sandwiches preparados
print('\nLista de sandwich preparados:')
for sandwich in finished_sandwich:
    print(sandwich.title())
