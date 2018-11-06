import numpy as np
#Pregunta1
x=0
word="hola"
for i in word:
	if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
		x+=1
print(x)

#Pregunta2

def palabra(a):
	m=['Palabra']
	n=['Repetida']
	return a*n, a*m

print palabra(4)
#Respuesta: Copia el elemento de la lista, el numero de veces que le entra por parametro.

#Pregunta3

def multiplica(a, b=5, c=7):
	return a*b*c

print multiplica(2), multiplica(2,3), multiplica(2,3,8)
#Respuesta: Imprime el resultado de la multiplicacion, en caso de no recibir ningun parametro toma el que tiene la funcion por defecto.

#Pregunta4

class rectangulo():
	def __init__(self, a=1.0, b=2.0):
		self.a=a
		self.b=b
		self.__area=a*b
	def set_area(self):
		self.__area=self.a*self.b
	def print_object(self):
		print("a", self.a)
		print("b", self.b)
		print("area", self.__area)

A=rectangulo()
A.print_object()

A.a=5.0
A.print_object()
#Le asigna este nuevo valor a "a"

A._area=18.0
A.print_object()
#No se modifica el valor del area, porque este es privado y depende de los valores de a y b.

A.set_area()
A.print_object()
#Actualiza el valor del area con los nuevos valores asignados para a y b.

#Pregunta5

class Libreta():
	def __init__(self, nombres=[ ], apellidos=[ ], tel=[ ]):
		self.nombres= nombres
		self.apellidos= apellidos
		self.tel= tel
	def nueva_entrada(self, n,a,tel):
		self.nombres.append(n)
		self.apellidos.append(a)
		self.tel.append(tel)
	def busca_apellido(self, a):
		losQueSon = []
		for i in range(len(self.apellidos)):
			if(a in self.apellidos[i]):
				losQueSon.append(i)
		for i in losQueSon:
			print(self.nombres[i],self.apellidos[i],self.tel[i])
	def borra_entrada(self, n,a):
		for i in range(len(self.nombres)):
			if(self.nombres[i] == n and self.apellidos[i] == a):
				del self.nombres[i]
				del self.apellidos[i]
				del self.tel[i]
				break
	def imprime_todo(self):
		for n in range(len(self.nombres)):
			print(self.nombres[n],self.apellidos[n],self.tel[n])

L = Libreta()

L.nueva_entrada("Ana", "Diaz", "4068585")
L.nueva_entrada("Pony", "Malta", "3449040")
L.nueva_entrada("Diana Lucia", "Hernandez Perez", "876626")
L.nueva_entrada("Daniel", "Forero Hernandez", "2471425")
L.busca_apellido("Hernandez")
L.borra_entrada("Diana Lucia", "Hernandez Perez")
L.imprime_todo()
