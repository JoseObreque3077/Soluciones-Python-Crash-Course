# Ejercicio 5-10
current_users = ["ADMIN", "Juan", "Carlos", "Sofía", "Camila"]
# Se crea una copia de current_users en minúsculas usando comprensión
current_users_copy = [user.lower() for user in current_users]
new_users = ["Sebastián", "SUPER_ADMIN", "Juan", "Sofía", "MANAGER"]
for user in new_users:
    if user.lower() in current_users_copy:
        print(f"El nombre de usuario {user} ya está en uso. Elige otro!")
    else:
        print(f"El nombre de usuario {user} está disponible")
