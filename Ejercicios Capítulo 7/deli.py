# Ejercicio 7-8
sandwich_orders = ['atún', 'pollo BBQ', 'pollo teriyaki', 'vegetariano',
                   'salame']
finished_sandwich = []

# Ciclo while que se ejecuta mientras existan elementos en la lista
# "sandwich_orders".
while sandwich_orders:
    # Se extrae el sandwich actual de la lista "sandwich_orders" (el primero
    # en la lista)
    actual_sandwich = sandwich_orders.pop(0)
    # Se imprime un mensaje que indica que el sandwich extraído fué preparado
    print(f'Se ha preparado un sandwich de {actual_sandwich}')
    # Se almacena el sandwich extraído de la lista de órdenes en la lista
    # "finished_sandwich".
    finished_sandwich.append(actual_sandwich)
# Se imprime la lista de sandwiches preparados usando un ciclo for
print('\nLista de sandwich preparados:')
for sandwich in finished_sandwich:
    print(sandwich.title())
