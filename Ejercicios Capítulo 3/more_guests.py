# Ejercicio 3-6
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
invitados.insert(2, "Lisa")  # Se agrega un invitado en el medio de la lista (posición 2) usando insert
invitados.append("Iván")  # Se agrega un invitado al final de la lista usando append

print(f"Saludos, {invitados[0].title()}, te invito a cenar")
print(f"Saludos, {invitados[1].title()}, te invito a cenar")
print(f"Saludos, {invitados[2].title()}, te invito a cenar")
print(f"Saludos, {invitados[3].title()}, te invito a cenar")
print(f"Saludos, {invitados[4].title()}, te invito a cenar")

