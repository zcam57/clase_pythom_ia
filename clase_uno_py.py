# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:02:39 2021

@author: cammac
"""

print("hellor world")

# Variables
a = 3
print(type(a))
a = "hola"
print(type(a))
a = 3.5
print(type(a))
a = True
print(type(a))

# Operaciones

# Suma

a = 5
b = 2
c = a + b
print(c)

#Resta

a = 5
b = 2
c = a - b
print(c)

# Multiplicacion

a = 5
b = 2
c = a * b
print(c)

# Division

a = 5
b = 2
c = a / b
print(c)

a = 5
b = 2
c = a // b
print(c)

# Potencia

a = 5
b = 2
c = a ** b
print(c)

# Raiz

a = 27
c = a ** (1/3)
print(c)

# import math
# raiz = math.sqrt(25)
# print(raiz)

a = "hola mundo"
a = 'Hola mundo'
b = "I can´t do it"
c = 'Alias "mac"'

# Entero int

a = 5

# Decimal float

a = 5.6

# Booleano bool

x = True
y = False

# Conversiones entre tipos de datos

# Convertitr de x a entero

a = '5'
y = float(a)
print(y)
print(type(y))

# Convertir de x a string

a = 5
y = str(a)
print(y)
print(type(y))

# Concatenaciones

a = 'hola'
b = 'mundo'
c = a + ' ' + b
print(c)

# Capturar por pantalla

nombre = input('Digite su nombre:')
print('Hola', nombre)

print('Digite su nombre:')
nombre = input()
print('Hola ', nombre)

# HUA que sume dos numeros e imprima su resultado

numero1 = input('Digite un numero: ')
numero2 = input('Digite un numero: ')
numero3 = int(numero1) + int(numero2)
print('La suma es : ', numero3)

numero_uno = float(input('Digite un numero: '))
numero_dos = float(input('Digite un numero: '))
suma = numero_uno + numero_dos
# print('La suma es : ', suma)
# print('La suma es : ', suma)
print(f'La suma de los numeros {numero_uno} + {numero_dos} es {suma} ', suma)

# HUA que lea un numero y lo eleve al cuadrado

numero_uno = int(input('Digite un numero: '))
elevado = numero_uno ** 2
print(f'El numero {numero_uno} elevado a la 2 es  {elevado} ')

# HUA que tome el valor de un producto , le aplique el 20%
# de descueto , imprima le valor del producto inicial,
# el valor con descuento y el valor ahorrado

precio = float(input('Digite el precio del producto: '))
descuento = precio ** 0.2
total = precio - descuento
print(f'El precio incial es de  ${precio: ,}  ')
print(f'El valor ahorrado es de   ${descuento: ,}  ')
print(f'El total a pagar es de   ${total: ,}  ')


# HUA que calcule la masa de la siguiente fórmula:
# Masa = (presión * volúmen) / (0.37 * (temperatura + 460))
presion = float(input('Digite la presion: '))
volumen = float(input('Digite el volumen: '))
temperatura = float(input('Digite la temperatura: '))
masa = (presion * volumen) / (0.37 * (temperatura + 460))
print(f'La masa es :  {masa}  ')

# HUA Calcular el número de pulsaciones que una persona debe tener por
# cada 10 segundos de ejercicio, si la fórmula es:
# Num. Pulsaciones = (200 – edad) /10.
edad = float(input('Digite su  edad : '))
Pulsaciones = (200 - edad) / 10.
print(f' Su numero de pulsaciones por cada 10 segundos es  :  {Pulsaciones}  ')












