#!/usr/bin/python

#¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero? ¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número entero por teclado, y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado) [Ayuda: ¿cuáles son los posibles restos que se obtienen de dividir un número cualquiera por 10?]

#Entrada
num = int(input('Ingrese un numero entero: '))

#Proceso
UnDig  = num % 10
DosDig = num % 100

#Salida
print('El último dígito es : ', UnDig)
print('Los últimos dos dígitos son : ', DosDig)

