#!/usr/bin/python

#Desafío 01: Conversión de Unidades de Tiempo

#Este primer Desafío es sencillo y lo asumimos como una forma de "entrada en calor" para enfrentar este tipo de evaluaciones. El enunciado del problema (o consigna) a resolver es el siguiente:

#Desarrolle un programa o script Python que permita cargar por teclado un número entero que representa la  cantidad de segundos que pasaron desde un evento dado.  El programa debe convertir esa cantidad de segundos  a la cantidad de horas, minutos y segundos que transcurrieron. Por ejemplo, si la cantidad de segundos  ingresada es 4452 deberá mostrar un mensaje que informe que el tiempo transcurrido fue de 1 hora, 14 minutos  y 12 segundos.

#Su tarea: cuando haya desarrollado el programa pedido, ejecútelo cuatro veces, y compruebe los resultados que obtenga al cargar las siguientes cantidades de segundos:

#Primera ejecución - Cantidad de segundos a ingresar:  7832
#Segunda ejecución - Cantidad de segundos a ingresar:  18993
#Tercera ejecución - Cantidad de segundos a ingresar:  2475
#Cuarta ejecución - Cantidad de segundos a ingresar: 25213

#Cuando haya obtenido los resultados, ingrese en este mismo desafío, y allí se le pedirá que registre los resultados en formato "horas:minutos:segundos". Tomando el mismo ejemplo que se indica en el enunciado del problema, si la cantidad de segundos ingresada es 4452, entonces usted deberá subir un resultado de la forma 1:14:12 sin espacios en blanco, sin comillas, y usando estrictamente el carácter : (dos puntos) para separar una parte de la otra. Cualquier error que cometa en el formato de su respuesta, podrá hacer que la solución subida se considere incorrecta, así que hágalo con mucho cuidado. Si la cantidad de horas o de minutos o de segundos final fue igual a cero, registre un cero en esa posición. Por ejemplo, si usted obtuvo una respuesta de 0 horas, 23 minutos y 0 segundos, entonces registre la siguiente respuesta: 0:23:0 cuando le sea requerida.

#Además, el desafío incluye al final una quinta consigna o pregunta adicional, en la cual se le pedirá hacer un programa que haga el proceso inverso: deberá tomar tres datos, que serán el valor en horas, el valor en minutos y el valor en segundos transcurridos desde un evento dado, y su programa deberá calcular la cantidad total de segundos a partir de esos datos. Por ejemplo, si los datos ingresados fuesen: horas = 4, minutos = 36 y segundos = 8 entonces el resultado a obtener es que la cantidad total de segundos es 16568.

print('\t\t\t Desafío 01: Conversión de Unidades de Tiempo')
for i in range(0,4):
    seg = int(input('Ingrese la cantidad de segundos del evento: '))

    hs, sr = divmod(seg, 3600)
    mi, sr = divmod(sr, 60)

    out = str(hs)+':'+str(mi)+':'+str(sr)
    print('\n\n \tSu conversión en formato de horas es: ', out, 'Hs\n\n')
#Segunda Parte: Conversión Inversa
hs = int(input('Ingrese la cantidad de horas: '))
mi = int(input('Ingrese la cantidad de minutos: '))
sg = int(input('Ingrese la cantidad de segundos: '))

sg_total = hs*3600 + mi*60 + sg
print('\n\n \tLa cantidad de segundos fueron: ', sg_total)

