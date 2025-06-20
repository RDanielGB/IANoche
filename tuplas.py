frutas = ("papaya","manzana","pera","durazno","fresa")
print(frutas.count("fresa"))
print(frutas.index("manzana"))
print(len(frutas))

copia = list(frutas)
print(frutas)
print(copia)
copia.pop(2) # sacar el elemto de la lista
print(copia)
frutas = tuple(copia)
print(frutas)