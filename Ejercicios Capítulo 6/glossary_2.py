# Ejercicio 6-4
# Conceptos: constante, variable, lista, ciclo, diccionario
glosario = {'constante': 'Una constante es un tipo de variable la cual no '
                         'puede ser cambiada.',
            'variable': 'Es un nombre que se refiere a un objeto que reside '
                        'en la memoria. Su valor puede cambiar durante la '
                        'ejecución del código.',
            'lista': 'Una lista es una estructura de datos y un tipo de dato '
                     'en python con características especiales. Lo especial '
                     'de las listas en Python es que nos permiten almacenar '
                     'cualquier tipo de valor como enteros, cadenas y hasta '
                     'otras funciones.',
            'ciclo': 'Un ciclo en Python o bucle en Python (como prefieras '
                     'llamarlos) te permite repetir una o varias '
                     'instrucciones cuantas veces lo necesitemos.',
            'diccionario': 'Un Diccionario es una estructura de datos y un '
                           'tipo de dato en Python con características '
                           'especiales que nos permite almacenar cualquier '
                           'tipo de valor como enteros, cadenas, listas e '
                           'incluso otras funciones. Estos diccionarios nos '
                           'permiten además identificar cada elemento por una '
                           'clave.',
            'vista de diccionario': 'Los objetos retornados por los métodos '
                                    'dict.keys(), dict.values(), '
                                    'y dict.items() son llamados vistas de '
                                    'diccionarios. Proveen una vista dinámica '
                                    'de las entradas de un diccionario, '
                                    'lo que significa que cuando el '
                                    'diccionario cambia, la vista refleja '
                                    'éstos cambios.',
            'IDLE': 'El entorno integrado de desarrollo de Python, '
                    'o Integrated Development Environment for Python. IDLE es '
                    'un editor básico y un entorno de intérprete que se '
                    'incluye con la distribución estándar de Python.',
            'iterable': 'Un objeto capaz de retornar sus miembros uno por '
                        'vez. Ejemplos de iterables son todos los tipos de '
                        'secuencias (como list, str, y tuple) y algunos de '
                        'tipos no secuenciales, como dict, objeto archivo, '
                        'y objetos de cualquier clase que defina con los '
                        'métodos __iter__() o con un método __getitem__() que '
                        'implementen la semántica de Sequence.',
            'PEP': 'Propuesta de mejora de Python, del inglés Python '
                   'Enhancement Proposal. Un PEP es un documento de diseño '
                   'que brinda información a la comunidad Python, o describe '
                   'una nueva capacidad para Python, sus procesos o entorno. '
                   'Los PEPs deberían dar una especificación técnica concisa '
                   'y una fundamentación para las capacidades propuestas.',
            'rebanada': 'Un objeto que contiene una porción de una sequence. '
                        'Una rebanada es creada usando la notación de '
                        'suscripto, [] con dos puntos entre los números '
                        'cuando se ponen varios, como en nombre_variable['
                        '1:3:5]. La notación con corchete (suscrito) usa '
                        'internamente objetos slice.'
            }

# Se recorre el diccionario y se almacena localmente la llave y el valor de
# cada item.
for concepto, definicion in glosario.items():
    print(f"{concepto.title()}:")
    print(f"{definicion.title()}\n")
