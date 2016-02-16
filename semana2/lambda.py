g = map(lambda x: x**2, range(5))
print(g)

g = list(map(lambda x: x**2, range(5)))
print(g)

lista = [1, 3, 5, 20, 50, 100]
g = list(filter(lambda x: x < 21 and x > 1, lista))
print(g)