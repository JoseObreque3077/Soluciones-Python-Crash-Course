# Ejercicio 4-11
pizzas = ["española", "pepperoni", "triple queso"]
friend_pizzas = pizzas[:]  # Se crea una copia de la lista llamada "pizzas"
pizzas.append("bbq")  # Se agrega una pizza a la lista original
friend_pizzas.append("campestre")  # Se agrega una pizza distinta a la segunda lista
print("Mis pizzas favoritas son:")
for pizza in pizzas:
    print(pizza.title())
print("Las pizzas favoritas de mi amigo son:")
for pizza in friend_pizzas:
    print(pizza.title())
