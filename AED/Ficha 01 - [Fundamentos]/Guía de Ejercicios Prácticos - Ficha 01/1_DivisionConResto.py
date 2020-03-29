#!/usr/bin/python

# Plantear un script (directamente en el shell de Python) que permita informar, para dos valores a y b el resultado de la división a/b y el resto de esa divisón.

#Entrada
a = int(input('Ingrese el valor de a = '))
b = int(input('Ingrese el valor de b = '))

#Proceso
division = a/b
resto = a%b

#Salida
print("El valor de la división entra a y b es = ", division)
print("El valor del resto entra a y b es = ", resto)

