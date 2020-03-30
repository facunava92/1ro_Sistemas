#!/usr/bin/python

#Conociendo el precio de lista de un artículo, determinar:
#   Precio de venta al contado (10% de descuento) 
#   Precio de venta con tarjeta (5% de recargo)

#Entrada
precio_bruto = float(input('Ingrese el valor del articulo: '))

#Procesos
precio_contado = precio_bruto * 0.9
precio_tarjeta = precio_bruto * 1.05

#Salida
print('\n')
print('\tEl precio en contado es: ', precio_contado)
print('\tEl precio en tarjeta es: ', precio_tarjeta)
