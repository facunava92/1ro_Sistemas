#!/usr/bin/python

#Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia (cargar por teclado el precio de ese medicamento) sabiendo que todos los medicamentos tienen un descuento del 35%. Mostrar el precio actual, el monto del descuento y el monto final a pagar.

#Entrada
precio= float(input('Ingrese el monto del medicamento: '))

#Procesos
descuento = precio * 0.35
precio_final = precio - descuento

#Salida
print('\n\tPrecio Bruto: ', precio)
print('\n\tDescuento: ', descuento)
print('\n\tPrecio final: ', precio_final)

