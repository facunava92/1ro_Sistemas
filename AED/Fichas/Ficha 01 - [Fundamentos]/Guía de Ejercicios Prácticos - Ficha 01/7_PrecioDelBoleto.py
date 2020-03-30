#!/usr/bin/python

#Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia. Para el cálculo del mismo se debe considerar el monto base (que se cobra siempre), más un valor extra calculado en base a la cantidad de kilómetros a recorrer:  Por cada kilómetro a recorrer se cobra $0.30 de adicional.

#Entrada
precio_base = int(input('Ingrese el precio base del boleto: '))
kilometros = int(input('Ingrese una cantidad de kilómetros a recorrer: '))

#Proceso
precio_final = precio_base + (kilometros * 0.30)

#Salida
print('El precio final del boleto es $',precio_final)
