#!/usr/bin/python

#Desarrollar un programa que cargue por teclado un importe (cantidad de dinero) expresado como número en coma flotante y muestre un mensaje con esa cantidad pero en dos formatos: en uno debe aparecer precedida por el signo '$' y en el otro debe aparecer precedida por la palabra "pesos".

#Entrada
cadena = input('Ingrese un importe: ')

#Proceso
formato1 = '$' + cadena
formato2 = 'pesos ' + cadena

#Salida
print('\n')
print('\t', formato1)
print('\t', formato2)

