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

# Resta

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
descuento = precio * 0.2
total = precio - descuento
print(f'El precio incial es de  ${precio: ,}  ')
print(f'El valor ahorrado es de   ${descuento: ,}  ')
print(f'El total a pagar es de   ${total: ,}  ')


# 1 HUA que calcule la masa de la siguiente fórmula:
# Masa = (presión * volúmen) / (0.37 * (temperatura + 460))
presion = float(input('Digite la presion: '))
volumen = float(input('Digite el volumen: '))
temperatura = float(input('Digite la temperatura: '))
masa = (presion * volumen) / (0.37 * (temperatura + 460))
print(f'La masa es :  {masa}  ')

# 2 HUA Calcular el número de pulsaciones que una persona debe tener por
# cada 10 segundos de ejercicio, si la fórmula es:
# Num. Pulsaciones = (200 – edad) /10.
edad = float(input('Digite su  edad : '))
Pulsaciones = (200 - edad) / 10.
print(f' Su numero de pulsaciones por cada 10 segundos es  :  {Pulsaciones}  ')

# 3 HUA Tres personas deciden invertir su dinero para fundar una empresa.
# Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
# que cada quien invierte con respecto a la cantidad total invertida.

invercion1 = float(input('Digite la cantidad de dinero que desea invertir: '))
invercion2 = float(input('Digite la cantidad de dinero que desea invertir: '))
invercion3 = float(input('Digite la cantidad de dinero que desea invertir: '))
total = invercion1 + invercion2 + invercion3
porcentaje1 = (invercion1 * 100) / total
porcentaje2 = (invercion2 * 100) / total
porcentaje3 = (invercion3 * 100) / total
print(f'el total dinero invertido es de   :  {total} ')
print(f'el porsentaje de inversion de la primera persona es de: {porcentaje1}')
print(f'el porsentaje de inversion de la segunda persona es de: {porcentaje2}')
print(f'el porsentaje de inversion de la tercera persona es de: {porcentaje3}')

# 4 HUA Un banco da a sus ahorradores un interes de 1.5% sobre el monto
# ahorrado. Teniendo como dato de entrada el saldo inicial del
# ahorrador determine el saldo final.

dinero = float(input('Digite la cantidad de dinero Inicial: '))
ganancia = (dinero * 0.015)
total = ganancia + dinero
print(f' El interes generado es de:  ${ganancia: ,}  ')
print(f' El total en su cuenta es  de:  ${total: ,}  ')

# 5 HUA Una empresa le hace los siguientes descuentos sobre el sueldo base
# a sus trabajadores: 1% por ley de politica pública, 4% por seguro
# social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
# algoritmo que determine el monto de cada descuento y el monto total
# a pagar al trabajador.

sueldo = float(input('Digite el total de su sueldo: '))
Ppublica = sueldo * 0.01
Ssocial = sueldo * 0.04
Sforzoso = sueldo * 0.005
Cahorro = sueldo * 0.05
total = sueldo - (sueldo * 0.105)
print(f' Descuento por politica publica:  ${Ppublica: ,}  ')
print(f' Descuento por seguro social:  ${Ssocial: ,}  ')
print(f' Descuento por seguro forzoso:  ${Sforzoso: ,}  ')
print(f' Descuento por caja de ahorro:  ${Cahorro: ,}  ')
print(f' Su sueldo con descuentos obligatorios es de :  ${total: ,}  ')

# 6 HUA El periódico el Informador cobra por un aviso clasificado un monto
# que depende del número de palabras, tamaño en cetímetros y
# número de colores. Cada palabra tiene un costo de $20.000, cada
# centímetro tiene un costo de $15.000 y cada color tiene un costo de
# $25.000. Realice un algoritmo que determine el monto a pagar por un
# aviso clasificado.

palabras = float(input('Numero de palabras que contiene el clasificado: '))
tamaño = float(input('Inregres cuantos centimetro ocupara su clasificado:'))
colores = float(input('Cuantos colores contiene su anuncio: '))
costopalabras = palabras * 20000
costotamaño = tamaño * 15000
costocolores = colores * 25000
total = costopalabras + costotamaño + costocolores
print(f' Costo por todas las palabras :  ${costopalabras: ,}  ')
print(f' Costo por tamaño de clasificado:  ${costotamaño: ,}  ')
print(f' Costo por colores que contiene el clasificado:   ${costocolores: ,}')
print(f' El total a pagar por el clasificado es de :  ${total: ,}  ')

# 7 HUA Una empresa paga a sus empleados un bono por antigüedad que
# consiste en $100.000 por el primer año laboral y $120.000 por cada
# año siguiente. Realice un algoritmo que determine el monto del bono
# a pagar a un trabajador que tiene varios años en la empresa.

antiguedad = float(input('Cuantos años lleva trabajando en la empresa : '))
bono = antiguedad * 120000
print(f' Su bono de antiguedad  es de:  ${bono: ,}  ')

# 8 HUA Una Universidad le paga a sus profesores $20.000 la hora y le hace
# un descuento del 5% por concepto de caja de ahorro. Determine el
# monto del descuento y el monto total a pagar al profesor.

horas = float(input('Cuantas hora trabajo : '))
total = horas * 20000
descuento = total * 0.05
print(f' Su total a pagar es de :  ${total: ,}  ')
print(f' Su Descuento por caja de ahorro es de :  ${descuento: ,}  ')

# 9 HUA Un centro de comunicaciones alquilan tarjetas para realizar llamadas
# y cobran el monto consumido de la tarjeta mas un recargo del 20%.
# Teniendo como dato de entrada el monto inicial y el monto final de la
# tarjeta, determine el costo de la llamada.

inicial = float(input('Digite el monto inicial de la tarjeta  : '))
final = float(input('Digite el monto final de la tarjeta  : '))
total = inicial - final
recargo = total * 0.2
pagar = total + recargo
print(f' Usted gasto  :  ${total: ,}  ')
print(f' Cobro de  recargo por uso de la tarjeta  :  ${recargo: ,}  ')
print(f' El total a pagar seria de :  ${pagar: ,}  ')

# 10 HUA En una fototienda cobran por el revelado de un rollo $1.500 por cada
# foto. Realice un algoritmo que determine el monto a pagar por un
# revelado completo sabiendo que adiconalmente le cobran el IVA
# (16%).

cantidad = float(input('Cuantas fotos contiene su rollo  : '))
pagar = cantidad * 1500
iva = pagar * 0.16
total = pagar + iva
print(f' La cantidad a pagar por todas sus fotos es de   :  ${pagar: ,}  ')
print(f' El iva a pagar es de 16% lo que equivale a  :  ${iva: ,}  ')
print(f' El total a pagar incluido iva es de  :  ${total: ,}  ')

# 11 HUA En un hospital existen tres áreas: Ginecología, Pediatría y
# Traumatología. El presupuesto anual del hospital se reparte
# conforme a la siguiente tabla: ginecologia  40% , traumatologia 30%,
# pediatria 30% , Obtener la cantidad de dinero que recibirá cada área,
# para cualquier monto presupuestal.


presupuesto = float(input('Ingrese el presupuesto total del hospital : '))
ginecologia = presupuesto * 0.40
traumatologia = presupuesto * 0.30
pediatria = presupuesto * 0.30
presupuesto = float(input('Ingrese el presupuesto total del hospital : '))
print(f' El presupuesto de Traumatologia es de  :  ${traumatologia: ,}  ')
print(f' El presupuesto de Pediatria es de   :  ${pediatria: ,}  ')

# 12 HUA Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
# que consiste en dejar gratis el alquiler de una película. Realice un
# algoritmo que teniendo como dato de entrada el total de películas
# alquiladas, y el número de días de alquiler, determine el monto a
# pagar

cantidad = float(input('Ingrese la cantidad de peliculas que alquirara: '))
tiempo = float(input('Ingrese la cantidad de dias que alquirara las peliculas:'))
total = (tiempo * 1500) * (cantidad - 1)
print(f'El total a pagar por el alquiler de las peliculas es de  : ${total : ,} ')

# 13 HUA Una Agencia de viajes cobra por un Tour a Cartagena $25.000
# diarios por persona. Realice un algoritmo que determine el monto a
# pagar por una familia que desee realizar dicho Tour sabiendo que
# también cobran el 12% de IVA.

familia = float(input('Ingrese la cantidad de integrantes de su familia: '))
dias = float(input('Ingrese la cantidad de dias que piensa hacer el tour: '))
total = (familia * 25000) * dias
iva = total * 0.12
suma = total + iva
print(f'El total a pagar por el tour es de  : ${total : ,} ')
print(f'El total a pagar por el tour mas iva es de  : ${total : ,} + ${iva: ,}  =  ${suma: ,}')
















