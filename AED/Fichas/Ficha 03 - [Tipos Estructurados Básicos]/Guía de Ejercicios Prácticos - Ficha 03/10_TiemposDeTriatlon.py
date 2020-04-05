#!/usr/bin/python

#Un triatlón es una competición deportiva en que los participantes realizan tres carreras: una de natación, una ciclista y una pedestre.
#Desarrollar un programa que permita ingresar el tiempo (en minutos y segundos) logrados en cada etapa por uno de los deportistas participantes.
#Con esos datos determinar:
#Tiempo total de la prueba (en formato hh:mm:ss)
#Tiempo máximo y mínimo (en segundos)
#Tiempo promedio de la prueba (en segundos, redondeado a 2 decimales)
#Consejo: convertir a segundos los horarios ingresados, para facilitar las operaciones

#Entrada
nadar = input('Ingrese el tiempo que demoró nadando respetando el formato mm:ss: ')
bici = input('Ingrese el tiempo que demoró en bici respentando el formato mm:ss: ')
correr = input('Ingrese el tiempo que demoró corriendo respetando el formato mm:ss: ')

#Procesos
nadar_seg= int(nadar[0]+nadar[1])*60 + int(nadar[3]+nadar[4])
bici_seg = int(bici[0]+bici[1])*60 + int(bici[3]+bici[4])
correr_seg = int(correr[0]+correr[1])*60 + int(correr[3]+correr[4])

tiempo_total_seg = nadar_seg + bici_seg + correr_seg
hs, sr = divmod(tiempo_total_seg, 3600)
mi, sr = divmod(sr, 60)

tiempo_min = min(nadar_seg, bici_seg, correr_seg)
tiempo_max = max(nadar_seg, bici_seg, correr_seg)

tiempo_promedio = tiempo_total_seg / 3.00
tiempo_promedio = round(tiempo_promedio,2) 

#Salida
print('\n')
print('\tLa prueba duro = {}:{}:{} Hs'.format(hs,mi,sr))
print('\tEl tiempo que mas demoró fue de {} seg'.format(tiempo_max))
print('\tEl tiempo que menos demoró fue de {} seg'.format(tiempo_min))
print('\tEl tiempo promedio fue de {} seg'.format(tiempo_promedio))

