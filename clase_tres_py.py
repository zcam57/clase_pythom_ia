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
print(a[1])
a = (2, 3, 4)
b = (2, True, 'Hola', 3.4)
c = (2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.5, 2.6])
4 in a


# Set
# Mutable pero NO ordenado
a = {1, 2, 3, 4}
print(a[1])
a = {2, 3, 4}
b = {2, True, 'Hola', 3.4}
c = {2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.5, 2.6]}  # no permite en su interior arrays


# Diccionario
# Mutable y No  ordenado

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
