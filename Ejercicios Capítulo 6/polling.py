# Ejercicio 6-6

# Resultados de la encuesta hasta el momento
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# Lista de personas a encuestar
personas = ['felipe', 'constanza', 'jen', 'phil', 'ruben']

for nombre in favorite_languages.keys():
    if nombre in personas:
        print(f"{nombre.title()}, gracias por responder la encuesta!")
    else:
        print(f"{nombre.title()}, te invitamos a responder nuestra encuesta.")
