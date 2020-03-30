#!/usr/bin/python

#Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en: 
#    yardas 
#    pulgadas 
#    centímetros 
#    metros 
#Sabiendo que: 1 pie = 12 pulgadas, 1 yarda = 3 pies,  1 pulgada = 2.54 centímetros, 1 metro = 100 centímetros.

#Entrada
pies = int(input('Ingrese un valor, el mismo corresponde a unidades en "pies": '))

#Proceso
yardas = pies/3
pulgadas = 12 * pies
centimetros = pulgadas * 2.54
metros = centimetros/100

#Salida
print('La conversión de ', pies,' pies es:')
print('Yardas: ', yardas)
print('Pulgadas: ', pulgadas)
print('Centímetros: ', centimetros)
print('Metros : ',metros)
