#!/usr/bin/python

#Desarrollar un programa de control electoral en un centro vecinal, en el que se ingresen, para cierto candidato: apellido, nombre y cantidad de votos. Luego presentar en pantalla un resumen que muestre: iniciales del candidato, cantidad de votos entre paréntesis, y debajo una línea con tantas  "x" como votos obtenidos (por ejemplo, el candidato obtuvo 4 votos, deberá aparecer una línea como esta:  "xxxx"  con cuatro letras "x") (Asumimos que en el centro vecinal no hay demasiados electores, de forma que podamos estar seguros que no habrá miles o millones de votos... sólo unos pocos para darle sentido al enunciado).

#Entrada
nombre = input('Ingrese el nombre del candidato: ')
apellido = input('Ingrese el apellido del candidato: ')
votos = int(input('Ingrese la cantidad de votos del candidato: '))

#Procesos
inicial_nombre = nombre[0]
inicial_apellido = apellido[0]
votos_string = votos * '*'

#Salida
print('\n')
print('\t{}{}({})'.format(inicial_nombre, inicial_apellido, votos))
print('\t{}'.format(votos_string))
