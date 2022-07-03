# Ejercicio 8-11
# Lista pequeña con mensajes aleatorios (por enviar)
messages = ['Hola mundo!', 'Esto es Python', 'Que agradable sujeto', 'Number 8']
# Lista con los mensajes que ya han sido enviados
sent_messages = []


def send_messages(lista_mensajes):
    while lista_mensajes:
        mensaje = lista_mensajes.pop()
        print(mensaje)
        sent_messages.append(mensaje)


# Se envían los mensajes usando la función antes definida (se le pasa una
# copia de la lista con los mensajes)
send_messages(messages[:])
# Se imprime la lista de mensajes por enviar (se mantiene inalterada)
print(f'Mensajes por enviar: {messages}')
# Se imprime la lista de mensajes enviados (alterada por la función)
print(f'Mensajes enviados: {sent_messages}')
