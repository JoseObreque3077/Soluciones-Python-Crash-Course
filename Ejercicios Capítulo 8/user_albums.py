# Ejercicio 8-8

# Función del ejercicio 8-7
def make_album(nombre_artista, nombre_album, num_canciones=None):
    album = {'Artista': nombre_artista, 'Album': nombre_album}
    if num_canciones:
        album['Número Canciones'] = num_canciones
    return album


# Se utiliza la función dentro de un bucle infinito para que el usuario ingrese
# la información de uno o más álbumes musicales.
while True:
    print('--------REGISTRO DE ALBUM MUSICAL--------')
    input_artista = input('Ingrese nombre del artista: ').title()
    input_album = input('Ingrese nombre del album: ').title()
    album_creado = make_album(input_artista, input_album)
    print('\n--------REGISTRO EXITOSO--------')
    print(album_creado)
    print('-----------------------------------\n')
    continuar = input('PRESIONE Q PARA SALIR O CUALQUIER TECLA PARA '
                      'CONTINUAR ').title()
    if continuar == 'Q':
        break
