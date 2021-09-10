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

# HUA #3 Una compañía de seguros está abriendo un departamento de
# finanzas y estableció un programa para captar clientes, que conssite
# en lo siguiente: Si el monto por el que se efectúa la fianza es menor
# que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
# es mayor que $50.000 la cuota a pagar será el 2% del monto. La
# afianzadora desea determinar cual será la cuota que debe pagar al
# cliente.

monto = float(input('Ingrese el  monto de su pago: '))
if(monto < 50000 and monto > 0):
    cuota = monto * 0.03
    total = monto + cuota
    print(f'Su cuata a pagar es: ${monto: ,} + 3% dando un total a pagar de: ${total: ,}')
elif(monto >= 50000):
    cuota = monto * 0.02
    total = monto + cuota
    print(f'Su cuata a pagar es: ${monto: ,} + 2% dando un total a pagar de: ${total: ,}')


# 4 HUA Una fábrica ha sido sometida a un programa de control de
# contaminación para lo cual se efectúa una revisión de los puntos de
# contaminación generados por la fábrica. El programa de control de
# contaminación consiste en medir los puntos que emite la fábrica en
# cinco días de una semana y si el promedio es superior a los 170
# puntos entonces tendrá la sanción de parar su producción por una
# semana y una multa del 50% de las ganancias diarias cuando no se
# detiene la producción. Si el promedio obtenido de puntos es de 170 o
# menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
# desea saber cuanto dinero perderá después de ser sometido a la
# revisión.

for i in range(5):
    puntos = int(input(f'Ingrese los puntos de contaminación del dia {i+1}:  '))
    valor = valor + puntos
promedio = valor / 5
if(promedio > 170):
    ganancias = float(input('Ingrese cuales son sus ganancias diarias: '))
    ganancidias = ganancias * 5
    multa = ganancidias * 0.5
    perdida = multa + ganancidias
    print('Como multa por exceder los puntos de contaminación permitidos debe detener su producción por 7 días ')
    print(f'La multa a pagar por exceder los puntos permitidos es de: ${multa: ,}')
    print(f'La cantidad de dinero que perderá la empresa es de:  ${perdida: ,}')
elif(promedio <= 170):
    print('Su empresa cumple con el promedio de contaminación permitida ')
valor = 0

# 5 HUA Una persona se encuentra con un problema de comprar un automóvil
# o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
# mientras el automóvil se devalúa, con el terreno sucede lo contrario.
# Esta persona comprará el automóvil si al cabo de tres años la
# devaluación de este no es mayor que la mitad del incremento del
# valor del terreno. Ayúdale a esta pesona a determinar si debe o no
# comprar el automóvil.

valor = float(input('Ingrese el valor  ambos bienes: '))
# devaluacion de un auto Consiste en dividir el valor
# del auto en la vida útil del mismo.
carro = valor / 3
casa = (valor / 3) * 0.5
if(carro <= casa):
    print('Es recomendable comprar el carro  ')
    print(f'ya que el carro en estos  3 años se devaluó menos del 50%  del valor que ganó la casa: ${carro: ,}')
    print(f'El 50% del valor que ganó la casa en estos 3 años es de: ${casa: ,}')
elif(carro > casa):
    print('Es recomendable comprar la casa ')
    print(f'ya que el carro en estos  3 años se devaluó mas del 50%  del valor que ganó la casa: ${carro: ,}')
    print(f'El 50% del valor que ganó la casa en estos 3 años  es de: ${casa: ,}')

# 6 HUA En una fábrica de computadoras se planea ofrecer a los clientes un
# descuento que dependerá del número de computadoreas que
# compre. Si las computadoras son menos de cinco se les dará un 10%
# de descuento sobre el total de la compra; si el número de
# computadoras es mayor o igual a cinco pero menos de diez se le
# otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
# precio de cada computadora es de $11.000.

cantidad = int(input('Ingrese la cantidad de computadores que desea comprar '))
precio = cantidad * 11000
if(cantidad < 5 and cantidad > 0):
    total = precio - (precio * 0.1)
    print(f'El precio a pagar por la compra de; {cantidad} computadores es:${precio: ,}  - 10% de descuento  es de : ${total: ,}')
elif(cantidad >= 5 and cantidad < 10):
    total = precio - (precio * 0.2)
    print(f'El precio a pagar por la compra de; {cantidad} computadores es:${precio: ,}  - 20% de descuento  es de : ${total: ,}')
elif(cantidad >= 10 ):
    total = precio - (precio * 0.4)
    print(f'El precio a pagar por la compra de; {cantidad} computadores es:${precio: ,}  - 40% de descuento  es de : ${total: ,}')
elif(cantidad <= 0):
    print(f'La siguiente cantidad {cantidad} no es valida')
