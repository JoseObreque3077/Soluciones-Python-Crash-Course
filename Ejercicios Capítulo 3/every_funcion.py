# Ejercicio 3-10
ciudades = ["villarrica", "pucón", "temuco", "valdivia", "ancud", "castro"]

print(f"lista original: {ciudades}")
# Usando append() se agrega un elemento al final de la lista
ciudades.append("padre las casas")
print(f"append(padre las casas): {ciudades}")
# Usando insert() se agrega un valor en la posición indicada, el resto se desplaza a la derecha
ciudades.insert(2, "curarrehue")
print(f"insert(2,curarrehue): {ciudades}")
# Usando del se elimina un valor de la lista según la posición indicada
del ciudades[5]
print(f"del ciudades[5]: {ciudades}")
# Usando pop() se elimina el último valor de la lista y al mismo tiempo, este valor puede ser usado
print(f"pop(): {ciudades.pop()}")
print(f"lista modificada: {ciudades}")
# También se puede usar pop() para eliminar elementos de cualquier posición
print(f"pop(4): {ciudades.pop(4)}")
print(f"lista modificada: {ciudades}")
# Usando remove() se puede eliminar un elemento de la lista por su valor (se elimina la primera aparición)
ciudades.remove("villarrica")
print(f"remove('villarrica'): {ciudades}")
# Usando sorted() se puede ordenar temporalmente una lista, alfabéticamente
print(f"sorted(ciudades): {sorted(ciudades)}")
print(f"ciudades: {ciudades}")
# También se puede realizar un ordenamiento temporal en orden alfabéticamente inverso
print(f"sorted(ciudades, reverse=True): {sorted(ciudades, reverse=True)}")
print(f"ciudades: {ciudades}")
# Con sort() se realiza lo mismo que con sorted() salvo que los cambios se aplican de forma permanente
ciudades.sort()
print(f"ciudades.sort(): {ciudades}")
print(f"ciudades: {ciudades}")
ciudades.sort(reverse=True)
print(f"ciudades.sort(reverse=True): {ciudades}")
print(f"ciudades: {ciudades}")
# Con len() se puede determinar la longitud de una lista
print(f"El largo de la lista, luego de las modificaciones es de: {len(ciudades)}")
