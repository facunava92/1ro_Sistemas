#!/usr/bin/python

#Desarrollar un programa que permita ingresar una palabra por teclado y la devuelva enmascarada, mostrando la primer letra y la última, pero reemplazando los caracteres intermedios por asteriscos. 

#Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”.

#Entrada
palabra = input('Ingrese una palabra: ')
n = len(palabra)

#Procesos
palabra_aux = '*' * (n-2)
palabra_final = palabra[0] + palabra_aux + palabra[n-1]

#Salida
print('Palabra enmascarada: ', palabra_final)
