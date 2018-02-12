#! /usr/bin/python3
# -*- coding: utf-8 -*-
import caso_nuevo.datos as datos

#Muestra la informacion completa de un alumno
def despliega_uno(elemento):
    for campo in datos.orden:
        print(campo + ": " + str(elemento[campo]))

#Muestra todos los alumnos que contiene archivos.py.
def despliega_todos(ruta=datos.ruta):
    #Se abre el archivo en modo lectura
    #Se cerrara el archivo automaticamente cuando se haya leido todo y es posible porque se
    #esta usando with
    with open(ruta, 'r') as archivo:
        contador = 0
        #Por cada alumno del archivo se despliegue su informacion correpondiente
        for alumno in archivo:
            alumno = eval(alumno)
            contador += 1
            print("\nAlumno: ", contador)
            despliega_uno(alumno)
        
        
def agrega_uno(elemento, ruta=datos.ruta):
    #Se abre el archivo para escribir un nuevo elemento hasta el final del archivo.El elemento es
    # un diccionario con la informacion de un alumno por ello se hace la conversion a cadena.
    #Cuando termina de guardar el alumno se cierra el archivo automaticamente esto es posible
    #por el uso de with.
    with open(ruta, 'a') as archivo:
        archivo.write(str(elemento) + '\n')