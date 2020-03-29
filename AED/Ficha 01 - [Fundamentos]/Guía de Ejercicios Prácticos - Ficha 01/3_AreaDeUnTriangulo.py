#!/usr/bin/python

#Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la base, pero sabiendo que su altura es igual al cuadrado de la base. (Observar que la altura no es un dato... sólo se indica la forma de calcularla de acuerdo a la base que sí es un dato).

#Entrada
print('El siguiente programa calcula el área de un triángulo a partir de la base.')
base = int(input('Ingrese el valor de la base: '))
altura = base ** 2

#Proceso
area = (base * altura)/2

#Salida
print('El área del triángulo es: ', area)
