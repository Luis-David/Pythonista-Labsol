#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""Ejemplo de modulos en el curso de Python"""
#Se importan los archivos y seles pone un nombre para llamar las funciones correpondiente al archivo
import caso_nuevo.altas as altas
import caso_nuevo.archivos as archivos

def principal():
    #Itera infinitamente hasta que haya un break y esto sucede cuando el 
    #usuario ingresa correctamente un numero entero
    while True:
        try:
            #Se pide que el usuario ingrese un numero entero
            alumnos = input("Número de alumnos:")
            #Se hace la conversion de cadena a entero
            alumnos = int(alumnos)
            #Se imprimer una linea vacia
            print()
            #Se cacha una expcion y se imprime
        except (ValueError) as error:
            print(error)
            #Se salta a la siguiente iteracion
            continue
        else:
            #Rompe el bucle infinito
            break

#Itera de 0 a "alumnnos" veces para ingresar nuevos alumnos.
    for contador in range(alumnos):
        print("\nAlumno nuevo", contador + 1)
        #Ejecuta la funcion agrega_uno() que esta en el archivo "archivos"
        archivos.agrega_uno(altas.alta())
    #Muestra todos los alumnos que tiene registrado el sistema.
    archivos.despliega_todos()
    