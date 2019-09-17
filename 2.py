import random
from matplotlib import pyplot as plt

def Lanzamiento_de_dados():
	dado_1=random.randint(1,6)
	dado_2=random.randint(1,6)
	Resultado=Suma_de_dados(dado_1,dado_2)
	#print("Suma de dados: ",Resultado)
	return dado_1,dado_2,Resultado

def Suma_de_dados(a,b):
	c=a+b
	return c

def Numero_de_lanzamientos():
	x=input("Ingrese la cantidad de lanzamientos: ")
	print("Cantidad de lanzamientos: ",x)
	return int(x)

def Ciclo(Lanzamientos):
	x=0
	Lista_dados_1=[]
	Lista_dados_2=[]
	Suma_dados=[]
	while x<Lanzamientos:
		D1,D2,RE=Lanzamiento_de_dados()
		Lista_dados_1,Lista_dados_2,Suma_dados = Listas(D1,D2,RE,Lista_dados_1,Lista_dados_2,Suma_dados)
		x=x+1
	print(Lista_dados_1)
	print("--------")
	print(Lista_dados_2)
	print("--------")
	print(Suma_dados)
	return Lista_dados_1,Lista_dados_2,Suma_dados

def Listas(D1,D2,RE,Lista_dados_1,Lista_dados_2,Suma_dados):
	Lista_dados_1.append(D1)
	Lista_dados_2.append(D2)
	Suma_dados.append(RE)
	return Lista_dados_1,Lista_dados_2,Suma_dados

def contar_cada_numero(Suma_dados):
	n_de_numeros = []
	x = 0
	numero = 2
	while x != 11:
		n = Suma_dados.count(numero)
		n_de_numeros.append(n)
		numero = numero + 1
		x = x + 1
	print(n_de_numeros)
	return n_de_numeros

def su_probabilidad(n_de_numeros,Lanzamientos):
	probabilidad = []
	x = 0
	while x != len(n_de_numeros):
		prob = n_de_numeros[x] / Lanzamientos
		probabilidad.append(prob)
		x = x + 1
	print(probabilidad)
	return probabilidad

def el_grafico():
	fig = plt.figure(u'Gráfica de barras') # Figure
	grafico = fig.add_subplot(111)
	numero_string = ["2","3","4","5","6","7","8","9","10","11","12"]
	datos = [2,5,6,8,3,7,3,7,2,6,3]
	xx = range(len(datos))
	grafico.bar(xx, datos, width=0.8, align='center')
	grafico.set_xticks(xx)
	grafico.set_xticklabels(numero_string)
	plt.show()

Lanzamientos=Numero_de_lanzamientos()
Lista_dados_1,Lista_dados_2,Suma_dados =  Ciclo(Lanzamientos)
n_de_numeros = contar_cada_numero(Suma_dados)
probabilidad = su_probabilidad(n_de_numeros,Lanzamientos)
el_grafico()