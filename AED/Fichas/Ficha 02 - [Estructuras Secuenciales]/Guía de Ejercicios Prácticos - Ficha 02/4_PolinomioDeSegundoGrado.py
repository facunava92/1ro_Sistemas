#!/usr/bin/python

#Desarrollar un programa que cargue por teclado los coeficientes a, b y c de un polinomio de segundo grado, y calcule y muestre el valor del polinomio en el punto x (cargando también x por teclado). Además, para el mismo polinomio, calcule y muestre el valor del discriminante de la fórmula para el cálculo de las raíces de la ecuación.

#Entrada
a = int(input('Ingrese el coeficiente a: '))
b = int(input('Ingrese el coeficiente b: '))
c = int(input('Ingrese el coeficiente c: '))

x = int(input('Ingrese un punto de interés: '))

#Procesos
punto = a*(x**2) + b*x + c
D = b**2 - 4*a*c

#Salida
print('\n\tEl valor de la función en el punto de interes es: ',punto)
print('\n\tEl valor del discriminante es :', D)
