# Ejercicio 6-12
londres = {'pais': 'Inglaterra',
           'población': 9_002_488,
           'fundación': '43 d.C.',
           'superficie': 1572,
           'información': 'Londres es la capital y mayor ciudad de Inglaterra '
                          'y del Reino Unido. Situada a orillas del río '
                          'Támesis, Londres es un importante asentamiento '
                          'humano desde que fue fundada por los romanos con '
                          'el nombre de Londinium hace casi dos milenios.'}

paris = {'pais': 'Francia',
         'población': 2_240_621,
         'fundación': '52 a.C.',
         'superficie': 105.4,
         'información': 'Su nombre proviene del pueblo galo de los parisios ('
                        'en latín, Parisii). La palabra «París» deriva del '
                        'latín Civitas Parisiorium (‘la ciudad de los '
                        'parisi’), designación que predominó sobre Lutecia ('
                        'cuyo nombre completo era Lutetia Parisii). No se '
                        'conoce con certeza el origen del nombre de los '
                        'parisii.'}

tokio = {'país': 'Japón',
         'población': 14_215_906,
         'fundación': '1457 d.C.',
         'superficie': 2187,
         'información': 'Tokio, oficialmente Metrópolis de Tokio, '
                        'es la capital de facto de Japón, ubicada en el '
                        'centro este de la isla de Honshu, concretamente en '
                        'la región de Kantō. En conjunto es una de las 47 '
                        'prefecturas de Japón. Es el centro de la política, '
                        'economía, educación, comunicación y cultura del '
                        'país. Cuenta también con la mayor concentración de '
                        'sedes corporativas, instituciones financieras, '
                        'universidades y colegios, museos, teatros, '
                        'establecimientos comerciales y de entretenimiento de '
                        'todo Japón.'}

cities = {'Londres': londres, 'París': paris, 'Tokio': tokio}

for city, info in cities.items():
    print(f'Ciudad: {city}')
    for dato, valor in info.items():
        print(f'{dato.title()}: {valor}')
    print('')
