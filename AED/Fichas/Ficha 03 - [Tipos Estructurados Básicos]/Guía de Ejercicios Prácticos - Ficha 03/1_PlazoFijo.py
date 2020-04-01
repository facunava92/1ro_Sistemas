#!/usr/bin/python

#Desarrollar un programa que cargue por teclado la cantidad de dinero depositada en plazo fijo por un cliente de un banco y calcular el saldo que tendrá esa cuenta al vencer el plazo fijo, sabiendo que el interés pactado era de 2.3% y que el banco cobra una tasa fija de gastos por servicios financieros igual $20 por cuenta.

#Entrada
bruto = float(input('Ingrese la cantidad de dinero depositada: '))
comision = 20
interes = 0.023 #2.3/100

#Procesos
neto = bruto*(1+interes) - comision
neto = round(neto,2)

#Salida
print('\n')
print('\tEl monto a cobrar sera de: ', neto)


