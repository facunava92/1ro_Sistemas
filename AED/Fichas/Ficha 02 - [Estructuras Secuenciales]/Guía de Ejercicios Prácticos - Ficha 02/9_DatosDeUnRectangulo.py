#!/usr/bin/python

#Hacer un programa que tome como entrada el ancho y el alto de un rectángulo y determine el perímetro y la superficie del mismo.

#Entrada
ancho = float(input('Ingrese el ancho del rectángulo: '))
alto = float(input('Ingrese el alto del rectángulo: '))

#Procesos
perimetro = 2*ancho + 2*alto
area = ancho * alto

#Salida
print('\n')
print('El valor del perímetro es :', perimetro)
print('El valor del área es:', area)
