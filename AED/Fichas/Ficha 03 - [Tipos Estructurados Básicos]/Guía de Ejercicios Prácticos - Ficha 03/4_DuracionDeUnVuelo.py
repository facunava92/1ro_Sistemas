#!/usr/bin/python

#Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo (hora y minutos), determine cuál es su duración en minutos. Si el viajero necesita luego 45 minutos más para ir del aeropuerto al hotel que ha reservado, ¿a qué hora llegara al mismo?

#Entrada
partida = input('Ingrese el horario de partida en el formato hh:mm 24Hs: ')
llegada = input('Ingrese el horario de llegada en el formato hh:mm 24Hs: ')
delay = 45

#Proceso
minutos_llegada = int(llegada[0]+llegada[1])*60 + int(llegada[3]+llegada[4])
minutos_partida = int(partida[0]+partida[1])*60 + int(partida[3]+partida[4])
minutos_viaje = minutos_llegada - minutos_partida + delay

#Salida
print('\n')
print('\t La duración del viaje fue de {0} minutos '.format(minutos_viaje)
