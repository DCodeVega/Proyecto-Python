lista_nombre = ["juan", "pedro", "ramiro"]

print(lista_nombre)
#print(type(lista_nombre))
# print([])

# Ayuda de lo que se puede hacer
# print(dir(lista_nombre))

print(lista_nombre[1])

# Agregando un nuevo elemento
lista_nombre.append("maria")

print(lista_nombre)

# otro forma de eliminar elemento
lista_nombre.remove('ramiro')
print(lista_nombre)


# otro forma de eliminar elemento por un indice
lista_nombre.pop(0)
print(lista_nombre)

# imprimir el indice de un color
print(lista_nombre.index('pedro'))