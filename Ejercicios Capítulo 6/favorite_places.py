# Ejercicio 6-9
favorite_places = {'Carlos': ['Londres', 'Portugal'],
                   'Carolina': ['Santiago', 'Roma', 'Seúl'],
                   'Pedro': ['Lisboa', 'Madrid', 'La Habana']}
for persona, lugares in favorite_places.items():
    print(f'Nombre: {persona}')
    print('Sus lugares favoritos son:')
    for lugar in lugares:
        print(lugar)
    print('')
