# Ejercicio 8-7
# Función que recibe un nombre de artista, el nombre de un álbum y el número de
# canciones de este (opcional) y almacena los datos en un diccionario.
def make_album(nombre_artista, nombre_album, num_canciones=None):
    album = {'Artista': nombre_artista, 'Album': nombre_album}
    if num_canciones:
        album['Número Canciones'] = num_canciones
    return album


# Se imprimen los álbumes generados (diccionarios)
print(make_album('Elvis Presley', 'From Elvis in Memphis', 12))
print(make_album('The Beatles', 'Abbey Road'))
print(make_album('Elton John', 'Madman Across the Water', 9))
