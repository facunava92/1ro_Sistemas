#!/usr/bin/python

#Una pequeña empresa de informática tiene que desarrollar un sistema de información y para ello tiene un presupuesto de x pesos para cubrir los costos de crear el sistema. Sabiendo que tiene pensado ganar al menos 17% por el proyecto, determine cuál es el valor máximo que pueden alcanzar los costos del proyecto.

#Entrada
x = int(input('Ingrese el presupuesto total: '))
costo = 17

#Proceso
costo_proyecto = (17/100) * x

#Salida
print('\n')
print('\t El costo máximo del proyecto es : $', costo_proyecto)

