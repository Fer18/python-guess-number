# -*- coding: utf-8 -*-
"""El juego consiste en adivinar un número aleatorio"""
import random
import time

ALEATORIO = random.randint(1, 20)
EXIT = 0
print u"                              ***** Cognits *****"
print U"\n                       **** Adivinado Full Pro 2.0 © ****"
NOMBRE = raw_input("Ingresa tu Nombre:\n")
print u"""\n¡BIENVENIDO!"""+ NOMBRE +u"""\nINSTRUCCIONES:
El reto del juego es adivinar un número comprendido entre 
un rango de (1-20).\n¡OJO!: Recuerda que solo tienes 5 oportunidades.\n¡Suerte!"""
INTENTOS = 0
TURNO2 = 5
#print aleatorio
while INTENTOS < 5:
    NUMERO = (raw_input("Ingresa un número:"))
    try:
        NUMERO = int(NUMERO)
        EXIT = 1
    except(RuntimeError, TypeError, NameError, ValueError):
        print u"Tiene que indicar un valor numérico entero"
# si no introduce un valor numerico, volvemos al inicio del bucle continue
        print
    if EXIT == 1:

        INTENTOS += 1
        TURNO2 -= 1


        if NUMERO < ALEATORIO and NUMERO > 0:
            print u"El número es Mayor"# verifica si el numero es muy alto
            EXIT = 0
            TURNO2 = str(TURNO2)
            print u"Te quedan "+ TURNO2 +" intentos\n"
            TURNO2 = int(TURNO2)
            print

        if NUMERO > ALEATORIO and NUMERO < 20:
            print u"El numero es Menor"#verifica si el numero es muy bajo
            EXIT = 0
            TURNO2 = str(TURNO2)
            print u"Te quedan "+ TURNO2 +" intentos\n"
            TURNO2 = int(TURNO2)

            print

        if NUMERO > 20:
            print u"El Número debe ser menor o igual a 20"
            TURNO2 = str(TURNO2)
            print u"Te quedan "+ TURNO2 +" intentos"
            TURNO2 = int(TURNO2)
            EXIT = 0
            print

        if NUMERO <= 0:
            print u"El Número debe ser Mayor a 0"
            TURNO2 = str(TURNO2)
            print u"Te quedan "+ TURNO2 +" intentos\n"
            TURNO2 = int(TURNO2)
            EXIT = 0
            print


        if NUMERO == ALEATORIO:
            break

if NUMERO == ALEATORIO:
    INTENTOS = str(INTENTOS)
    print
    print u"Excelente, " + NOMBRE + u"! has adivinado el número en: " + INTENTOS + u" intentos!"
    print
    print u"                     **** Adivinador Full Pro 2.0 © **** "
    print u"                            ***** Cognits *****"
    print u"                         Third Generation Grupo # 2 :\n"
    print u"                               Annabel Girón"
    print u"                               Fernando López"
    print u"                                Kevin Herrera\n"
    print u"                          KAR_KO,INDUSTRIS Copyright ®"

    time.sleep(5)

if INTENTOS == 5:
    ALEATORIO = str(ALEATORIO)
    print u"Lo sentimos te quedaste sin intentos y no adivinaste el número.\
    El número correcto era:" + ALEATORIO
    print u"                     **** Adivinador Full Pro 2.0 © **** "
    print u"                            ***** Cognits *****"
    print u"                         Third Generation Grupo # 2 :\n "
    print u"                               Annabel Girón"
    print u"                               Fernando López"
    print u"                                Kevin Herrera\n"
    print u"                          KAR_KO,INDUSTRIS Copyright ®"
time.sleep(5)
