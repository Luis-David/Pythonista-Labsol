#! /usr/bin/python3
# -*-coding: utf-8 -*-
import caso_nuevo.datos as datos
import caso_nuevo.valida as valida
"""Módulo que contiene la funcion de altas."""

def alta():
    """Realiza las altas."""
    
    #Funcion que le pide al usuario que ingrese la informacion correspondiente al valor del parametro campo.
    def ingresa(campo):
        #Bucle infinito solo termina cuando se hace un return dato.
        while True:
            #Se hace la concatenacion del mensaje que se le va a mostrar al usuario
            mensaje = "Ingrese " + campo.lower() + ": " 
            #Solicita por pantalla al usuario que ingrese lo que se le pide en el mensaje
            dato = input(mensaje)


            if datos.campos[campo] != str:
                #Verifica que el numero ingresado sea del tipo de dato correpondiente al campo
                try:
                                    #se hace un casting de dato con el tipo de dato del campo.
                                    #Si es entero o flotante se podra validar si es dato correspondiente
                    if eval(dato) == datos.campos[campo](dato):
                        dato = datos.campos[campo](dato)
                    else:
                        continue
                except:
                    continue
            #Valida las cadenas del campo solicitado
            if valida.reglas(dato, campo):
                return dato
    #Regresa un diccionario con la informacion del alumno.
    #Se crea un diccionario a partir de la iteracion de los elementos que componen 
    #a la lista datos.orden y por cada elemento de la lista se llama a la funcion ingresa()
    #para llenar el valor correspondiente al campo del diccionario en el que se encuentre. 
    return {campo: ingresa(campo) for campo in datos.orden}
