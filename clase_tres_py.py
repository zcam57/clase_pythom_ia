# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:44:51 2021

@author: cammac
"""


# Tipos de Colecciones

# Listas o vectores
# Tipos de datos mutable y ordenado

a = [2, 3, 4]
b = [2, True, 'Hola', 3.4]
c = [2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.5, 2.6]]

for valor in a:
    print(valor)

for valor in b:
    print(valor)

for valor in c:
    print(valor)

a[0] = 7
a = []
print(b[2])
print(c[2][1])
print(c[3][1][1])

a.append(5)  # Agrega el elemento al final de la lista
a.remove(3)  # Elimina el elemento que coincida con el valor
a.pop()  # Elimina el ultimo elemento del vector
a.pop(2)  # Elimina un elemento por posición
a.clear()  # Elimina todos los elementos del vector
# del a
4 in a  # Busca el elemento 4 dentro de a
len(a)  # Cantidad de elementos del vector
a = b  # Asignacion de b en el mismo espacio de memoria de a
id(a)  # Convierte a decimal la dirección en memoria de un objeto
a = b.copy()  # Copia los elementos de b en a
a = b[:]
b = a[0:3]
b = a[:6]
b = a[2:]
print(c[3][1][:2])

# Tuplas
# Tipos de datos INMUTABLE y ordenado

a = (1, 2, 3, 4)
a = ()
print(a[1])
a = (2, 3, 4)
b = (2, True, 'Hola', 3.4)
c = (2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.5, 2.6])
4 in a


# Set
# Mutable pero NO ordenado
a = {1, 2, 3, 4}
a = set()
print(a[1])
a = {2, 3, 4}
b = {2, True, 'Hola', 3.4}
c = {2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.5, 2.6]}  # no permite en su interior arrays


# Diccionario
# Mutable y No  ordenado
a = {}
a = {'nombre': 'Mac', 'apellido': 'Perez'}
a = {1: 'Mac',  2: 'Perez'}

a['nombre']


for valor in a:
    print(valor)

for valor in a.values():
    print(valor)

for valor in a.keys():
    print(valor)

for valor in a.items():
    print(valor)

for llave, valor in a.items():
    print(f'Llave: {llave}, Valor: {valor}')


# Funciones

def nombre_funcion():
    pass


def saludar():
    print('Hola mundo')


def saludar(nombre):
    print(f'Hola {nombre}')


# Pythom no permite la Sobrecarga de métodos

# Parametro Opcionales

def saludar(nombre='Mundo'):
    print(f'Hola {nombre}')


def saludar(nombre, apellido=""):
    print(f'Hola {nombre} {apellido}')


def saludar(nombre="Mundo", apellido=""):
    print(f'Hola {nombre} {apellido}')

# No puedo tener un parametro obligatorio después de un
# parametro opcional
def saludar(nombre, apellido="", segundo_apellido):
    print(f'Hola {nombre} {apellido}')


# Parámetro ilimitados

def saludar(*nombres, apellido=""):
    for nombres in nombres:
        print(f'Hola {nombres}')
    print(f'apellido {apellido}')


def saludar(**nombres):
    print({nombres})


def resta(a, b):
    print(a - b)


def operaciones(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b
    return suma, resta, mult, div


resultados = operaciones(4, 5)

suma, res, mul, div = operaciones(4, 5)

suma, _, _, div = operaciones(4, 5)

# while(condicion):


# Commit Inicial


# . El departamento de Seguridad de Transito de Barranquilla, desea saber de
# los n autos que entrar a la ciudad, cuantos entran con calcomanía de cada
# color. Conociendo el último digito de la placa de cada automóvil se puede
# determinar el color de la calcomanía utilizando la siguiente relación:
# DIGITO COLOR
# 1 o 2 Amarilla
# 3 o 4 Rosa
# 5 o 6 Roja
# 7 u 8 Verde
# 9 o 0 Azul

amarilla = 0
rosa = 0
roja = 0
verde = 0
azul = 0
cantidad = int(input('Cuantos autos ingresaron a la ciudad : '))
for x in range(cantidad):
    placa = int(input('Digite el ultimo numero de su placa: '))
    if(placa == 1 or placa == 2):
        amarilla = amarilla + 1
    elif(placa == 3 or placa == 4):
        rosa = rosa + 1
    elif(placa == 5 or placa == 6):
        roja = roja + 1
    elif(placa == 7 or placa == 8):
        verde = verde + 1
    elif(placa == 9 or placa == 0):
        azul = azul + 1
print(f'Ingresaron: {amarilla} carros con calcomanía amarilla')
print(f'Ingresaron: {rosa} carros con calcomanía rosa')
print(f'Ingresaron: {roja} carros con calcomanía roja')
print(f'Ingresaron: {verde} carros con calcomanía verde')
print(f'Ingresaron: {azul} carros con calcomanía azul')
