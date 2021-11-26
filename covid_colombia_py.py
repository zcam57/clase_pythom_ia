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
