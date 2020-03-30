#!/usr/bin/python

#La famosa ecuación de Einstein para conversión de una masa m en energía viene dada por la fórmula: 
#E = mc^2
#Donde c es la velocidad de la luz cuyo valor es c = 299792.458 km/seg. Desarrolle un programa que lea el valor una masa m en kilogramos y obtenga la cantidad de energía E producida en la conversión.

#Entrada
m = float(input('Ingrese el valor de la masa en Kg: '))
c= 299892.458

#Procesos
E = m*c**2

#Salida
print('\n\t La Energia es: ', E, 'J')

