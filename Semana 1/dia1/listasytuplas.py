#declaro una lista
lista = ["cadena", 1, False, "nombre", 20, [1, 3, 2 , 4]]
listaMultiple = ["cadena", ["cadena dentro", "de otra cadena"]]
listaEnteros = [2, 3, 1]
lista.sort()

miLista = lista[2]
miListaMultiple = lista[:-2]

print (lista)
print(miLista)
print(miListaMultiple)
print(miListaMultiple[1])


nuevaLista = lista[0:2]
print(nuevaLista)
nuevaLista = lista[0:4:2]
print(nuevaLista)
nuevaLista = lista[0::2]
print(nuevaLista)
nuevaLista = lista[2:]
print(nuevaLista)
nuevaLista = lista[:4]
print(nuevaLista)

# #lista modificada
lista[0] = "otra cadena"
lista[5][0] = 0

print(lista)

lista[0:2] = ["modificado", 5]

print(lista)

print(lista[-2])
# #Extend - Append - insert - remov
print(lista)
lista.append(["agregado", "otro mas"])
lista.extend(["CDMX","SONORA"])
lista.insert(1,"me metí")
lista[1] = "ya soy estático"
print (lista)

# #tuplas
tupla = (1, "hola", True)

print(tupla)
print(tupla[1:])

# #diccionarios
dic = {'id': 12,
		'Nombre': 'Paco',
		'Apellido': 'Ocampo'
		}

nombre = dic['Nombre']

print(nombre)

# #set
caja = [1, 2, 3, 4, 1]
print(set(caja))