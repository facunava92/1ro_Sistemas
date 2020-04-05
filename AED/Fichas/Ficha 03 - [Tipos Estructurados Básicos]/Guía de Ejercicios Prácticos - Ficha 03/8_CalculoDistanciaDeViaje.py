#!/usr/bin/python

#Un persona cautivada por los paisajes argentinos se le ocurrió la loca idea de unir los puntos mas extremos (Ushuahia y La Quiaca) en bicicleta, es decir se propuso hacer 3641.3 Km en bicicleta.
#Nuestro aventurero efectivamente inició la travesía pero se accidentó y sólo recorrió x metros según su GPS. 
#Usted debe solicitar ese valor x e informar cuántos kilómetros y metros recorrió nuestro aventurero y qué porcentaje represento lo recorrido del total de kms a recorrer de Ushuahia a La Quiaca (para el porcentaje usted deberá realizar los calculos en metros).

#Entrada
metros = int(input('Ingrese la cantidad de metros que recorrió el viajante: '))
total = 3641.3 * 1000

#Procesos
kilometros = metros/1000
porcentaje = (metros/total)*100
porcentaje = round(porcentaje, 2)

#Salida
print('\n')
print('\t El viajante recorrió {}m ({}Km) los cuales representa {}% del viaje'.format(metros, kilometros, porcentaje))
