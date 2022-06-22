# Ejercicio 6-8
pet1 = {'especie': 'perro', 'dueño': 'Fabián'}
pet2 = {'especie': 'gato', 'dueño': 'Tamara'}
pet3 = {'especie': 'hurón', 'dueño': 'Cristian'}
pet4 = {'especie': 'canario', 'dueño': 'Sebastián'}
pet5 = {'especie': 'perro', 'dueño': 'Christine'}

pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    for llave, valor in pet.items():
        print(f'{llave.title()}: {valor.title()}')
    print('')
