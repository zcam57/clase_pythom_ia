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

#  Un Zoólogo pretende determinar el porcentaje de animales que hay en las
# siguiente categorias de edades: 0 a 1 año, de mas de 1 año y menos de 3 y
# de 3 o mas años. El zoológico todavía no está seguro del animal que va
# estudiar. Si se decide por elefantes solo tomará una muestra de 20 de ellos;
# si se decide por jirafas, tomara 15 de muestras y si son chompancés tomará
# 40.
rango = 0  # rango de edad de 0 -1
rango2 = 0  # rango de edad  >1 y <3
rango3 = 0  # rango de edad >3
porcentaje = 0
porcentaje2 = 0
porcentaje3 = 0
animal = input('Que animal va estudiar: elefante, jirafas, chimpancés:  ')
if(animal == 'elefante'):
    for x in range(2):
        edad = int(input(f'Ingrese la edad del elefante #{x+1}: '))
        if(edad >= 0 and edad <= 1):
            rango = rango + 1
        elif(edad > 1 and edad < 3):
            rango2 = rango2 + 1
        elif(edad >= 3):
            rango3 = rango3 + 1
    porcentaje = rango / 2
    porcentaje2 = rango2 / 2
    porcentaje3 = rango3 / 2
    print(f'EL promedio de elefantes con una edad de  0 a 1 año es {porcentaje}')
    print(f'EL promedio de elefantes con una edad de de mas de 1 año y menos de 3 {porcentaje2}')
    print(f'EL promedio de elefantes con una edad de de 3 o mas años {porcentaje3}')
elif(animal == 'jirafas'):
    for x in range(5):
        edad = int(input(f'Ingrese la edad de las jirafa  #{x+1}: '))
        if(edad >= 0 and edad <= 1):
            rango = rango + 1
        elif(edad > 1 and edad < 3):
            rango2 = rango2 + 1
        elif(edad >= 3):
            rango3 = rango3 + 1
    porcentaje = rango / 5
    porcentaje2 = rango2 / 5
    porcentaje3 = rango3 / 5
    print(f'EL promedio de Jirafas con una edad de  0 a 1 año es {porcentaje: ,}')
    print(f'EL promedio de Jirafas con una edad de de mas de 1 año y menos de 3 {porcentaje2: ,}')
    print(f'EL promedio de Jirafas con una edad de de 3 o mas años {porcentaje3: ,}')
elif(animal == 'chimpances'):
    for x in range(4):
        edad = int(input(f'Ingrese la edad del Chimpancé #{x+1}: '))
        if(edad >= 0 and edad <= 1):
            rango = rango + 1
        elif(edad > 1 and edad < 3):
            rango2 = rango2 + 1
        elif(edad >= 3):
            rango3 = rango3 + 1
    porcentaje = rango / 4
    porcentaje2 = rango2 / 4
    porcentaje3 = rango3 / 4
    print(f'EL promedio de chimpancés con una edad de  0 a 1 año es {porcentaje}')
    print(f'EL promedio de Chimpancés con una edad de de mas de 1 año y menos de 3 {porcentaje2}')
    print(f'EL promedio de Chimpanc´s con una edad de de 3 o mas años {porcentaje3}')
else:
    print('El animal ingresado no es valido')

# Una empresa se requiere calcular el salario semanal de cada uno de los n
# obreros que laboran en ella. El salario se obtiene de la siguiente forma:
# a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora
# b. Si trabaja mas de 40 horas se le paga $20 por cada una de
# las primeras 40 horas y $25 por cada hora extra.

cantidad = int(input('Ingrese la cantidad de trabajadores de su empresa: '))
for x in range(cantidad):
    horas = int(input('Ingrese la cantidad de horas trabajadas  esta semana:'))
    if(horas <= 40 and horas > 0):
        salario = 20 * horas
        print(f'el salario del trabajador es de: ${salario: ,}')
    elif(horas > 40):
        extras = horas - 40
        salario = (40 * 20) + (extras * 25)
        print(f'el salario del trabajador es de: ${salario: ,}')
    else:
        print('Las horas de trabajo no pueden ser igual a cero')

# Calcular el promedio de edades de hombres, mujeres y de todo un grupo
# de alumnos.
acumulador = 0  # acumulador de edad hombres
cantidad = 0  # contador de hombre
acumulador2 = 0  # acumulador de edad mujeres
cantidad2 = 0  # contador de mujeres
alumnos = int(input('Ingrese la cantidad de alumnos: '))
for x in range(alumnos):
    genero = input('El estudiante es Hombre o Mujer: ')
    if(genero == 'hombre'):
        edad = int(input('Ingrese su edad: '))
        acumulador = acumulador + edad
        cantidad = cantidad + 1
    elif(genero == 'mujer'):
        edad = int(input('Ingrese su edad: '))
        acumulador2 = acumulador2 + edad
        cantidad2 = cantidad2 + 1
promedio = acumulador / cantidad
promedio2 = acumulador2 / cantidad2
print(f'El promedio de edad de los alumnos hombres es de  {promedio} ')
print(f'El promedio de edad de los alumnass mujeres es de  {promedio2} ')

# Encontrar el menor valor de un conjunto de n números dados

menor = 999
cantidad = int(input('Ingrese la cantidad de números a ingresar '))
for x in range(cantidad):
    numero = int(input('Ingrese un número '))
    if(numero < menor):
        menor = numero
print(f'El numero menor de todos los ingresados es: {menor}')

# Cinco miembros de un club contra la obesidad desean saber cuanto han
# bajado o subido de peso desde la última vez que se reunieron. Para esto se
# debe realizar un ritual de pesaje en donde cada uno se pesa en diez
# básculas distintas para así tener el pormedio mas exacto de su peso. Si
# existe diferencia positiva entre este promedio de peso y el peso de la última
# vez que se reunieron, significa que subieron de peso. Pero si la diferencia
# es negativa, significa que bajaron. Lo que el problema requere es que por
# cada persona se imprima un letrero que diga: “SUBIÓ” o “BAJÓ” y la
# cantidad de kilos que subió o bajó de peso.

for x in range(5):
    peso = 0
    bascula = 0
    promedio = 0
    kilos = 0
    peso = int(input('Ingrese su ultimo peso: '))
    for y in range(10):
        pesaje = int(input(f'Ingrese su peso en la maquina numero {y+1}: '))
        bascula = bascula + pesaje
    promedio = bascula / 10
    kilos = promedio - peso
    if(peso < promedio):
        print(f' Subió  : {kilos} kilos')
    elif (peso > promedio):
        print(f' Bajó  : {kilos} kilos')

# 7 En un supermercado una ama de casa pone en su carrito los artículos que
# va tomando de los estantes. La señora quiere asegurarse de que el cajero
# le cobre bien lo que ella ha comprado, por lo que cada vez que toma un
# artóculo anota su precio junto con la cantidad de artículos iguales que ha
# tomado y determina cuanto dinero gastará en ese artículo; a esto le suma lo
# que irá gastando en los demás artículos, hasta que decide que ya tomó
# todo lo que necesitaba. Ayúdele a esta señora a obtener el total de su
# compra.

total = 0
cantidad = int(input('Ingrese la cantidad de articulos que va a comprar: '))
for x in range(cantidad):
    precio = float(input('Ingrese el precio del producto: '))
    iguales = int(input('Ingrese la cantidad de articulos iguales: '))
    producto = precio * iguales
    print(f'EL pago por el producto ingresado es de: {producto: ,}')
    total = total + (precio * iguales)
print('Ya tomo todos los articulos que necesitaba')
print(f'EL total a  pagar por sus articulos es de: ${total: ,}')





