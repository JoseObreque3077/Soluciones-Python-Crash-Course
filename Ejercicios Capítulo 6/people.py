# Ejercicio 6-7
persona1 = {'nombre': 'José',
            'apellido': 'Obreque',
            'edad': 28,
            'ciudad': 'Villarrica'}

persona2 = {'nombre': 'Carlos',
            'apellido': 'Cifuentes',
            'edad': 31,
            'ciudad': 'Loncoche'}

persona3 = {'nombre': 'Francisco',
            'apellido': 'Figueroa',
            'edad': 22,
            'ciudad': 'Padre Las Casas'}

people = [persona1, persona2, persona3]

for persona in people:
    for llave, valor in persona.items():
        print(f'{llave.title()}: {valor}')
    print('')
