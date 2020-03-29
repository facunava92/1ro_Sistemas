#!/usr/bin/python

#Un binomio al  cuadrado (suma) es igual al cuadrado del primer término, más el doble producto del primero por el segundo más el cuadrado del segundo.
#Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores a y b, el valor del cuadrado del binomio.

#Entrada
print('El siguiente programa calcula el cuadrado de un binomio.')
a = int(input('Ingreses un número: '))
b = int(input('Ingreses otro número: '))

#Proceso
binomio = a**2 + 2*a*b + b**2

#Salida
print('El resultado es: ', binomio)
