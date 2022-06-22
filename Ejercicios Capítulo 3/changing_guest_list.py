# Ejercicio 3-5
invitados = ["helton", "orlan", "alexis"]
print(f"Saludos, {invitados[0].title()}, te invito a cenar")
print(f"Saludos, {invitados[1].title()}, te invito a cenar")
print(f"Saludos, {invitados[2].title()}, te invito a cenar")
print(f"{invitados[1].title()} no podrá asistir!")

invitados[1] = "camila"
print(f"Saludos, {invitados[0].title()}, te invito a cenar")
print(f"Saludos, {invitados[1].title()}, te invito a cenar")
print(f"Saludos, {invitados[2].title()}, te invito a cenar")
