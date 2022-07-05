# Ejercicio 8-13
# Esta función (extraída de un ejemplo del libro) permite crear un perfil de
# una persona usando como valores básicos el nombre y el apellido, permitiendo
# además ingresar una cantidad aleatoria de información en pares llave-valor
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


mi_perfil = build_profile('José',
                          'Obreque',
                          direccion='Av. Costanera 0001',
                          telefono=973829966,
                          email='stark3077@gmail.com')
print(mi_perfil)
