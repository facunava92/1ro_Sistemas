#!/usr/bin/python

#En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y Traumatología. El presupuesto anual del hospital se reparte de la siguiente manera:
#    Área           Presupuesto
#   Urgencias           37%
#   Pediatría           42%
#   Traumatología       21%
#Cargar por teclado el monto del presupuesto total del hospital, y calcular y mostrar el monto que recibirá cada área.

#Entrada
presupuesto = int(input('Ingrese el monto del presupuesto del hospital: '))
porcentaje_urgencias = 37/100
porcentaje_pediatria = 42/100
porcentaje_traumatologia = 21/100

#Procesos
urgencias = presupuesto * porcentaje_urgencias
pediatria = presupuesto * porcentaje_pediatria
traumatologia = presupuesto * porcentaje_traumatologia

#Salida
print('\n')
print('\t Urgencias = $', urgencias)
print('\t Pediatría= $', pediatria)
print('\t Traumatología = $', traumatologia)
