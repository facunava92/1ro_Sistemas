#!/usr/bin/python

#Se conoce el monto del salario actual de un empleado, el nombre del empleado y el área funcional al cual pertenece. Se pide calcular el nuevo salario del empleado sabiendo que obtuvo un incremento del 8% sobre su salario actual y un descuento de 2.5% por servicios, informando los resultados con el formato que se especifica a continuación:

#Entrada
nombre = input('Ingrese nombre del empleado: ')
area = input('Ingrese área funcional: ')
salario = int(input('Ingrese el salario del empleado: '))
aumento = 8
descuento = 2.5

#Procesos
salario_nuevo = salario * (1 + ((aumento-descuento)/100))

#Salida
print('\n')
print('Nombre Empleado: ', nombre, '\tNuevo Salario: $ ', salario_nuevo)
print('Área Funcional: ', area)
print('Salario Actual: ', salario)

