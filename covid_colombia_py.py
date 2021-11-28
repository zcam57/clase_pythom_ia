# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 09:19:16 2021

@author: cammac
"""


import pandas as pd


url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

# tamaño del dataset
data.shape

# columnas del dataset

data.columns

# acceder a una columna

data.Sexo

data['Sexo']

# agrupar por columnas

data.groupby('Sexo').size()

#  Reemplazar

data.Sexo.replace('f', 'F', inplace = True)
data.Sexo.replace('m', 'M', inplace = True)

# agrupar por valor 

data.Estado.value_counts()

# normalizar el estado

data.Estado.replace('leve', 'Leve', inplace = True)
data.Estado.replace('LEVE', 'Leve', inplace = True)

# diga cuantas mujeres han fallecido en colombia por covid 19

data[(data.Sexo == 'F') & (data.Estado == 'Fallecido')].shape[0]

# diga cuantas mujeres han fallecido en colombia por covid 19

data[(data.Sexo == 'M') & (data.Estado == 'Fallecido')].shape[0]

# cantidad de hombres y mujeres fallecidas
data[(data.Estado == 'Fallecido')].groupby('Sexo').size()

# cuantos fallecidos hay en colombia

data[(data.Estado == 'Fallecido')].shape[0]


data.groupby(['Estado', 'Sexo']).size()

data.groupby(['Sexo', 'Estado']).size()


data.Estado.value_counts().plot.bar()

data.Sexo.value_counts().plot.bar()

data['Nombre municipio'].value_counts().head(5)


# Cuantas mujeres fallecieron en barranquilla
data[(data.Sexo == 'F') & (data.Estado == 'Fallecido') & (data['Nombre municipio'] == 'BARRANQUILLA')].shape[0]


barranquilla = data[data['Nombre municipio'] == 'BARRANQUILLA']

barranquilla.groupby(['Sexo', 'Estado']).size()

barranquilla[barranquilla.Sexo == 'F'].Estado.value_counts().plot.bar()

barranquilla.Estado.value_counts().sort_values(ascending = False)

barranquilla.groupby(['Estado', 'Sexo']).size().plot.bar()


data['fecha reporte web'] = pd.to_datetime(data['fecha reporte web'])
barranquilla['fecha reporte web'] = pd.to_datetime(barranquilla['fecha reporte web'])

data.groupby('fecha reporte web').size().cumsum().plot()
barranquilla.groupby('fecha reporte web').size().cumsum().plot()


data['Nombre municipio'].value_counts()

# Taller INTELIGENCIA ARTIFICIAL TALLER DE MATRICES

# 1. Número de casos de Contagiados en el País
data.Estado.shape[0]

# 2.Número de Municipios Afectados
data['Nombre municipio'].value_counts().shape[0]

# 3.Liste los municipios afectados (sin repetirlos)


# 4.Número de personas que se encuentran en atención en casa
data['Ubicación del caso'].replace('CASA', 'Casa', inplace = True)
data['Ubicación del caso'].replace('casa', 'Casa', inplace = True)
data[(data['Ubicación del caso'] == 'Casa')].shape[0]

# 5.Número de personas que se encuentran recuperados
data[(data.Recuperado == 'Recuperado')].shape[0]

# 6. Número de personas que ha fallecido
data.Recuperado.replace('fallecido', 'Fallecido', inplace = True)
data[(data.Recuperado == 'Fallecido')].shape[0]

# 7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,
#  Relacionado)
data['Tipo de contagio'].value_counts().sort_values(ascending = False)

# 8. Número de departamentos afectados
data['Nombre departamento'].value_counts().shape[0]

# 9.Liste los departamentos afectados(sin repetirlos)
data['Nombre departamento'].value_counts()

# 10. Ordene de mayor a menor por tipo de atención
data['Ubicación del caso'].replace('CASA', 'Casa', inplace = True)
data['Ubicación del caso'].replace('casa', 'Casa', inplace = True)
data['Ubicación del caso'].value_counts(ascending = False)

# 11. Liste de mayor a menor los 10 departamentos con mas casos de
# contagiados
data['Nombre departamento'].value_counts(ascending = False).head(10)

# 12. Liste de mayor a menor los 10 departamentos con mas casos de
data[(data.Estado == 'Fallecido')].groupby('Nombre departamento').size().sort_values(ascending = False).head(10)

# 13. Liste de mayor a menor los 10 departamentos con mas casos de
# recuperados
data[(data.Recuperado == 'Recuperado')].groupby('Nombre departamento').size().sort_values(ascending = False).head(10)

# 14. Liste de mayor a menor los 10 municipios con mas casos de
# contagiados
data['Nombre municipio'].value_counts(ascending = False).head(10)

# 15. Liste de mayor a menor los 10 municipios con mas casos de
# fallecidos
data[(data.Recuperado == 'Fallecido')].groupby('Nombre municipio').size().sort_values(ascending = False).head(10)

# 16. Liste de mayor a menor los 10 municipios con mas casos de
# recuperados
data[(data.Recuperado == 'Recuperado')].groupby('Nombre municipio').size().sort_values(ascending = False).head(10)

# 17. Liste agrupado por departamento y en orden de Mayor a menor las
# ciudades con mas casos de contagiados /comit 17
data.groupby(['Nombre departamento', 'Nombre municipio']).size().sort_values(ascending = False).head(10)

# 18. Número de Mujeres y hombres contagiados por ciudad por
# departamento
data.groupby(['Sexo', 'Nombre departamento']).size().sort_values(ascending = False)

# 19. Liste el promedio de edad de contagiados por hombre y mujeres por
# ciudad por departamento 
data.groupby(['Sexo', 'Nombre departamento', 'Edad']).size().sort_values(ascending = False).head(10)

# 20. Liste de mayor a menor el número de contagiados por país de
# procedencia
data['Nombre del país'].value_counts(ascending = False)

# 21. Liste de mayor a menor las fechas donde se presentaron mas
# contagios
data['Fecha de diagnóstico'].value_counts(ascending = False)

# 22. Diga cual es la tasa de mortalidad y recuperación que tiene toda 
# Colombmia 
data[(data.Estado == 'Fallecido')].shape[0]
data[(data.Recuperado == 'Recuperado')].shape[0]

# 23. Liste la tasa de mortalidad y recuperación que tiene cada
# departamento
data[(data.Recuperado == 'Fallecido')].groupby('Nombre departamento').size().sort_values(ascending = False)
data[(data.Recuperado == 'Recuperado')].groupby('Nombre departamento').size().sort_values(ascending = False)

# 24. Liste la tasa de mortalidad y recuperación que tiene cada ciudad
data[(data.Recuperado == 'Fallecido')].groupby('Nombre municipio').size().sort_values(ascending = False)
data[(data.Recuperado == 'Recuperado')].groupby('Nombre municipio').size().sort_values(ascending = False)

# 25. Liste por cada ciudad la cantidad de personas por atención
data.groupby(['Nombre municipio', 'Estado']).size().sort_values(ascending = False)

# 26. Liste el promedio de edad por sexo por cada ciudad de contagiados
data.groupby(['Nombre municipio', 'Sexo', 'Edad']).size().sort_values(ascending = False)

# 27. Grafique las curvas de contagio, muerte y recuperación de toda
# Colombia acumulados
data.Recuperado.value_counts().plot.bar()

# 28. Grafique las curvas de contagio, muerte y recuperación de los 10
# departamentos con mas casos de contagiados acumulados
data['Nombre departamento'].value_counts(ascending = False).head(10).plot.bar()

# 29. Grafique las curvas de contagio, muerte y recuperación de las 10
# ciudades con mas casos de contagiados acumulados
data['Nombre municipio'].value_counts(ascending = False).head(10).plot.bar()

