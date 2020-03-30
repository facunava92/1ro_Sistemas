#!/usr/bin/python

#En el Congreso se vota la sanción de una ley muy importante. Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra, e informe el porcentaje obtenido en cada caso.

#Entrada
pos = int(input('Ingrese la cantidad de votos a favor: '))
neg = int(input('Ingrese la cantidad de votos en contra: '))

#Procesos
total = pos + neg
porcentaje_pos = pos / total * 100
porcentaje_neg = neg / total * 100

#Salida
print('\n')
print('\tHay un', porcentaje_pos, '% de votos a favor')
print('\tHay un', porcentaje_neg, '% de votos en contra')

