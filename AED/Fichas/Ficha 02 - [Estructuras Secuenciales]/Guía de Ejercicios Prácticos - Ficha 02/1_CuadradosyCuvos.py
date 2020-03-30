#!/usr/bin/python

#Leer dos números y calcular:
#   La suma de sus cuadrados.
#   El promedio de sus cubos.

#Entrada
a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))

#Procesos
suma = a**2 + b**2
prom = (a**3 + b**3) // 2

print('\n\nLa suma de sus cuadrados es: ', suma)
print('\nEl promedio de sus cubos es: ', prom)
