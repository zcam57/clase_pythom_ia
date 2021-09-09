# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:04:06 2021

@author: cammac
"""

# Condicionales

# Tabla de verdad

# Tabla de and
# v and v = v
# v and f = f
# f and v = f
# f and f = f

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# Tabla del or
# v or v = v
# v or f = v
# f or v = v
# f or f = f

print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# Negacion

print(not True)  # False
print(not False)  # True

# Mas de dos condiciones al mismo tiempo

print(True and False and True or False or True or True)  # True
print(True and (False and True) or False or (True or True))  # True

# Jerarquia de operaciones
# 1. parentesis y llaves
# 2. Potencia y Raices
# 3. Multiplicacion y Division
# 4. Sunas y Restas

# Jerarquia de operaciones booleanas
# 1. Parantesis y llaves
# 2. Tabla de verdad

# Estructura if
x = -1
if (x > 0):
    print('1')
else:
    print('2')
    print('3')


# HUA que dada la edad de una persona indique si es mayor
# o menor de edad

edad = int(input("Ingrese su edad :"))
if (edad >= 18):
    print('Usted es mayor de edad ')
else:
    print('Usted es menor  de edad ')

# HUA que indique si un estudiante aprobo o reprobo una
# asignatura teniendo en cuenta que se aprueba con minimo
# una calificacion de 3.0 hasta 5.0. El rang o valido de una nota es
# entre 0 y 5.

nota = float(input("Ingrese su nota:"))
if (nota >= 3.0 and nota <= 5.0):
    print("usted aprobó la  materia")
elif(nota < 3.0 and nota >= 0):
    print("usted no reprobó la materia")
else:
    print("La nota ingresada no es válida")

# HUA que dado un número n diga si es negativo, positivo o
# cero.

numero = float(input("Digite un número: "))
if(numero >= 1):
    print(f"El número {numero }es positivo")
elif(numero <= -1):
    print(f"El número {numero}es negativo")
else:
    print(f"EL numero {numero} es cero ")

# Ciclos

# Ciclo for

for valor in range(11):
    print(valor)

for valor in range(1, 11):
    print(valor)

for valor in range(2, 11, 2):
    print(valor)

for valor in range(11):
    print(valor)
    print(valor + 1)


# HUA que de las n notas de un estudiante y calcule el promedio
# académico

numero = int(input('Ingrese el número de notas: '))
if(numero >= 0):
    acumulador = 0
    for x in range(numero):
        notas = float(input(f"Ingrese su nota {x + 1}: "))
        acumulador = acumulador + notas
    promedio = acumulador / numero
    promedio = round(promedio, 2)
    print(f"la nota definitiva es: {promedio}")
else:
    print('EL número de notas no puede ser igual a cero')

# Inicio del Taller

# HUA que calcule el total a pagar por la compra de
# camisas. Si se compran tres camisas o mas se aplica un descuento
# del 30% sobre el total de la compra y si son menos de tres camisas
# un descuento del 10%.

precio = float(input('Digite el precio de la camisa: '))
cantidad = int(input('Digite la cantidad de camisas que va a comprar: '))
total = precio * cantidad
if(cantidad >= 3):
    valor = total * 0.3
    precio = total - valor
    print(f'El descuento es de: ${valor: ,} ')
    print(f'El total a pagar es : ${precio: ,} ')
elif(cantidad == 1 and cantidad <= 3):
    valor = total * 0.1
    precio = total - valor
    print(f'El descuento es de: ${valor: ,} ')
    print(f'El total a pagar es : ${precio: ,} ')
else:
    print('Ingrese un cantidad válida de camisas ')

# HUA En un supermercado se hace una promoción, mediante la cual el
# cliente obtiene un descuento dependiendo de un número que se
# escoge al azar. Si el número escogido es menor que 74 el descuento
# es del 15% sobre el total de la compra, si es mayor o igual a 74 el
# descuento es del 20%. Obtener cuanto dinero se le descuenta.
# selecionar desdes el import IMPORTANE IMPORTANTE

import random

for i in range(1):
    print(random.randrange(0, 100))

numero = int(input('Ingrese el número que se le dio anteriormente : '))
precio = float(input('Ingrese el total a pagar de su compra : '))
if(numero <= 73 and numero >= 0):
    descuento = precio * 0.15
    total = precio - descuento
    print(f'Su descuento es del 15% lo cual equivales: ${descuento: ,}')
    print(f'Su total a pagar con descuento es de: ${total: ,}')
elif(numero >= 74 and numero <= 100):
    descuento = precio * 0.2
    total = precio - descuento
    print(f'Su descuento es del 20% lo cual equivales: ${descuento: ,}')
    print(f'Su total a pagar con descuento es de: ${total: ,}')
else:
    print('Digite un número Válido igual o mayor a cero y igual o menor a 100')
