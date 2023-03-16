# listas 
lista = []
print(lista)

lista.append(10)
lista.append(47)
lista.append(-1)
lista.append(54)
lista.append(True)
lista.append("Hola")
print("Longitud o tamaño de la lista",len(lista))
lista[3] = "Pedro"
#lista.pop()
print(lista)
lista.pop()
lista.remove(10)
print(lista)
lista.reverse()
lista.insert(2,"Luis")
print(lista)
print("Elemento en posicion 3 de la lista",lista[3])