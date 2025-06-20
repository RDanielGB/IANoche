frutas = {"papaya","manzana","pera","durazno","fresa","papaya"} #noson ordenados
frutas2 = {"papaya","manzana","pera","durazno","fresa","papaya","naranja"}
print(frutas)
frutas.add("mandarina")
print(frutas)
#frutas.clear()
#print(frutas)

copia = frutas.copy()
print(copia)

print(frutas.difference(frutas2))
print(frutas.intersection(frutas2))
print(frutas.union(frutas2))
