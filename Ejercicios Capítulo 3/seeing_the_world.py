# Ejercicio 3-8
lugares = ["noruega", "islandia", "italia", "nueva zelanda", "holanda"]
print(f"lista original: {lugares}")
print(f"lista ordenada a-z: {sorted(lugares)}")  # Sorted ordena la lista temporalmente sin cambiar la original
print(f"lista original: {lugares}")
print(f"lista ordenada z-a: {sorted(lugares, reverse=True)}")  # Sorted ordenando inversamente
print(f"lista original: {lugares}")
lugares.reverse()  # reverse() invierte el orden de la lista (por posición), afectando a la lista original
print(f"lista al revés: {lugares}")
print(f"lista original alterada: {lugares}")
lugares.reverse()
print(f"lista al revés: {lugares}")
print(f"lista original nuevamente: {lugares}")
lugares.sort()  # sort() ordena permanentemente la lista, afectando a la lista original
print(f"lista ordenada a-z: {lugares}")
print(f"lista original alterada: {lugares}")
lugares.sort(reverse=True)
print(f"lista ordenada z-a: {lugares}")
print(f"lista original alterada: {lugares}")

