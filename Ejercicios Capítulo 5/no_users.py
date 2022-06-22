# Ejercicio 5-9
usernames = ["admin", "Carlos", "Juan", "Tamara", "Gabriel"]
usernames.clear()
if usernames:
    for username in usernames:
        if username == "admin":
            print("Saludos administrador, ¿desea ver un reporte?")
        else:
            print(f"Saludos, {username}.")
else:
    print("No hay usuarios registrados!")
