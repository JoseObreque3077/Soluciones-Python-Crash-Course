# Ejercicio 3-7
invitados = ["helton", "orlan", "alexis"]
print(f"Saludos, {invitados[0].title()}, te invito a cenar")
print(f"Saludos, {invitados[1].title()}, te invito a cenar")
print(f"Saludos, {invitados[2].title()}, te invito a cenar")
print(f"{invitados[1].title()} no podrá asistir!")

invitados[1] = "camila"
print(f"Saludos, {invitados[0].title()}, te invito a cenar")
print(f"Saludos, {invitados[1].title()}, te invito a cenar")
print(f"Saludos, {invitados[2].title()}, te invito a cenar")

print("Se ha encontrado una mesa mas grande para la cena!")

invitados.insert(0, "claudio")  # Se agrega un invitado al inicio de la lista (posición 0) usando insert
invitados.insert(2, "lisa")  # Se agrega un invitado en el medio de la lista (posición 2) usando insert
invitados.append("iván")  # Se agrega un invitado al final de la lista usando append

print(f"Saludos, {invitados[0].title()}, te invito a cenar")
print(f"Saludos, {invitados[1].title()}, te invito a cenar")
print(f"Saludos, {invitados[2].title()}, te invito a cenar")
print(f"Saludos, {invitados[3].title()}, te invito a cenar")
print(f"Saludos, {invitados[4].title()}, te invito a cenar")

print("La nueva mesa no llegará a tiempo")
excluido1 = invitados.pop()
print(f"Lo siento {excluido1.title()}, no podré invitarte a cenar")
excluido2 = invitados.pop()
print(f"Lo siento {excluido2.title()}, no podré invitarte a cenar")
excluido3 = invitados.pop()
print(f"Lo siento {excluido3.title()}, no podré invitarte a cenar")
excluido4 = invitados.pop()
print(f"Lo siento {excluido4.title()}, no podré invitarte a cenar")

print(f"Saludos, {invitados[0].title()}, te invito a cenar")
print(f"Saludos, {invitados[1].title()}, te invito a cenar")

del invitados[1]
del invitados[0]
print(invitados)
