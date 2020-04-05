#!/usr/bin/python

#En la disciplina olímpica una de las pruebas mas esperadas en la natacion es la posta 4x100. En esta disciplina el equipo ganador registró los siguientes tiempos en cada estilo:
#   Espalda: 52 segundos 15 centésimas.
#   Pecho: 1 minuto 2 segundos 75 centésimas.
#   Mariposa: 59 segundos 80 centésimas.
#   Libre: 48 segundos 15 centésimas.
#Usted debe averiguar el tiempo total de la carrera del equipo ganador y representarlo en minutos, segundos y centésimas.
#Para recordar:
#   1 minutos son 60 segundos.
#   1 segundo son 100 centesimas.

#Entrada
espalda = input('Tiempo en espalda en el formato mm:ss:cc = ')
pecho = input('Tiempo en pecho en el formato mm:ss:cc = ')
mariposa = input('Tiempo en mariposa en el formato mm:ss:cc = ')
libre = input('Tiempo en libre en el formato mm:ss:cc = ')
#espalda = '00:52:15'
#pecho = '01:02:75'
#mariposa = '00:59:80'
#libre = '00:48:15'

#Proceso
espalda_cent = int(espalda[0]+espalda[1])*60*100 + int(espalda[3]+espalda[4])*100 + int(espalda[6]+espalda[7])
pecho_cent = int(pecho[0]+pecho[1])*60*100 + int(pecho[3]+pecho[4])*100 + int(pecho[6]+pecho[7])
mariposa_cent = int(mariposa[0]+mariposa[1])*60*100 + int(mariposa[3]+mariposa[4])*100 + int(mariposa[6]+mariposa[7])
libre_cent = int(libre[0]+libre[1])*60*100 + int(libre[3]+libre[4])*100 + int(libre[6]+libre[7])

tiempo_total_cent = espalda_cent + pecho_cent + mariposa_cent + libre_cent

ss, cc  = divmod(tiempo_total_cent, 100)
mm, ss  = divmod(ss, 60)

#Salida
print('\n')
print('\t Tiempo total = {}:{}:{}' .format(mm, ss, cc))
