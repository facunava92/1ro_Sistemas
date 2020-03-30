#!/usr/bin/python

#Un productor agricola desea saber cuantos quintales de trigo puede producir en su parcela. Se pide ingresar el largo y el ancho en metros de la parcela y determinar el rinde sabiendo que en 10 m2 se obtienen 2 quintales.

#Entrada
ancho = float(input('Ingrese el ancho de la parcela: '))
largo = float(input('Ingrese el largo de la parcela: '))
factor_de_rendimiento = 2/10

#Procesos
area = ancho * largo
rendimiento = area * factor_de_rendimiento

#Salida
print('\n')
print('\t La parcela rinde', rendimiento, 'quintales')
