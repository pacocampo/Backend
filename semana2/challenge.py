
lista = ['A', 'B', 'C']
categoria = ['Alta', 'Media', 'Baja']
resultado = []

for l in lista:
	for c in categoria:
		resultado.append([l,c])
print(resultado)

# resList = []
# g = [[l, c] for l in lista for c in categoria]
# print(g)