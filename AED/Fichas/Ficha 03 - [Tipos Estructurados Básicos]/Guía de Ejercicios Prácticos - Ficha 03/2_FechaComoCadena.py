#!/usr/bin/python

#Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa una fecha en formato 'dd/mm/aaaa', y muestre por separado el día, el mes y el año. Ejemplo: si la cadena ingresada es '16/03/2016' el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'.

#Entrada
cadena = input("Ingrese una fecha con el siguiente formato 'dd/mm/aaaa': ")

#Proceso
dia = cadena[0] + cadena[1]
#cadena[2] = '/'
mes = cadena[3] + cadena[4]
#cadena[5] = '/'
ano = cadena[6] + cadena[7] + cadena[8] + cadena[9]

#Salida
print('\n')
print('\t Dia = ', dia)
print('\t Mes = ', mes)
print('\t Año = ', ano)
