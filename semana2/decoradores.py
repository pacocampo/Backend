
def dec(funcion):
	#a = funcion
	def wrapper(*segun, **options):
		x = funcion(*segun, **options)
		print(x)
		print("Yo le agrego 1")
		y = x ** 2
		print(y)
	return wrapper


@dec
def sumar(a, x):
	f = a + x
	return f


sumar(2,2)