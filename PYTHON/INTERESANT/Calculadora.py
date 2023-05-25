# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano.
# La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido,
# y el resultado de aplicar la función a esos enteros.

import os  # Amb aixo podem manipular o escriure com si estiguesim al cmd
# from colorama import Fore, init #Amb aixo podem cambiar de color el cmd
# init()#Iniciem
# print(Fore.GREEN+" Recursos Python")


import datetime
import time


os.system("cls")  # Neteja la pantalla
os.system("color 0a")  # Canvi de color 0a=verd fons negre


def sumar(num1, num2):
    return num1+num2


def restar(num1, num2):
    return num1-num2


def multiplicar(num1, num2):
    return num1*num2


def dividir(num1, num2):
    # Amb aixo fent un anti troll amb un except x/0 (Dinant un error[ZeroDivisionError])
    try:
        return num1/num2
    except ZeroDivisionError:  # Em de expecificar el tipus de error que pot succedir o donara error igualment
        print("No es pot dividir per 0")
        return "operacio erronea"


def potencia(num1, num2):
    return num1**num2


def seno():
    # la relación que existe entre el cateto opuesto al ángulo y la hipotenusa.
    # Se obtiene dividiendo los valores de ambos.
    catet = float(input("Quin es el angle del catet?"))
    hipotenusa = float(input("i Quina es la hipotenusa?"))

    print(
        f"El seno de {catet}(catet) i {hipotenusa}(hipotenusa) es de {catet/hipotenusa}")


def coseno():
    # El coseno es igual a la longitud del lado adyacente al ángulo dividido por la longitud de la hipotenusa.
    costat_a = float(input("Quina es la longuitud del primer costat? "))
    # Aquest seria el b
    costat_oposat = float(input("Quina es la longuitud del costat oposat? "))
    costat_c = float(input("i per ultim ? "))
    cos_a = costat_oposat/costat_c
    cos_b = costat_a/costat_c

    print(f"El coseno de {costat_a}(A), es de {cos_a}")
    print(f"El coseno de {costat_oposat}(B), es de {cos_b}")

    # El coseno también es igual al seno del ángulo complementario.


def tangente():
    print("tangente")


def exponencial():
    print("exponencial")


# Amb aixo el usuari seleccionará quina funcio vol utilitzar
funcio = [0, 1, 2, 3, 4, 5]
operatiu = True
while operatiu == True:  # Infinit
    print(f"""
        Benvolgut a la Ment Humana
        UNA "SENCILLA" CALCULADORA

        Tens les següents opcions:
        1) Sumar
        2) Restar
        3) Multiplicar
        4) Dividir
        5) Potencia
        6) Calcular el seno *
        7) Calcular el coseno*
        8) Calcular la tangent*
        9) Cambiar los números elegidos
        10) Apagar calculadora





        """)
    seleccio = int(input("        Introdueixí la opcio desitgada: "))
    os.system("color 0a")

    if (seleccio == 1):  # Suma
        os.system("cls")  # Netejem la pantalla
        print("""SUMA
        """)
        num1 = float(input("Introdueixi el primer número: "))
        num2 = float(input("Introdueixi un segon número: "))
        # os.system("color 04")
        print(f"Resultat=   {sumar(num1,num2)}")
        time.sleep(2/3)

    if (seleccio == 2):  # Resta
        os.system("cls")  # Netejem la pantalla
        print("""RESTA
        """)
        try:
            num1 = float(input("Introdueixi el primer número: "))
            num2 = float(input("Introdueixi un segon número: "))
        except ValueError:
            print(f"Ingrese un valor numerico")
        except NameError:
            print(f"Ingrese un valor numerico")
        # os.system("color 04")
        else:
            print(f"Resultat=   {restar(num1,num2)}")
        time.sleep(3/3)

    if (seleccio == 3):  # Multiplicar
        os.system("cls")  # Netejem la pantalla
        print("""MULTPICACIÓ
        """)
        num1 = float(input("Introdueixi el primer número: "))
        num2 = float(input("Introdueixi un segon número: "))
        # os.system("color 04")
        print(f"Resultat=   {multiplicar(num1,num2)}")
        time.sleep(2/3)

    if (seleccio == 4):  # Dividir
        os.system("cls")  # Netejem la pantalla
        print("""DIVISIO
        """)
        try:
            num1 = float(input("Introdueixi el primer número: "))
            num2 = float(input("Introdueixi un segon número: "))
        # os.system("color 04")
        except ValueError:
            print("Introdueixi un valor numerico")
        else:
            print(f"Resultat=  {dividir(num1,num2)}")
        time.sleep(2/3)

    if (seleccio == 5):  # Potencia
        os.system("cls")  # Netejem la pantalla
        print("""POTENCIA
        """)
        num1 = float(input("Introdueixi el primer número: "))
        num2 = float(input("Introdueixi un segon número: "))
        print(f"Resultat=  {potencia(num1,num2)}")
        time.sleep(2/3)

    if (seleccio == 6):
        os.system("cls")
        print(""" SENO
        """)
        num1 = float(input("Introdueixi el primer número: "))
        num2 = float(input("Introdueixi un segon número: "))

    if (seleccio == 7):
        os.system("cls")
        print(""" SENO
        """)
        num1 = float(input("Introdueixi el primer número: "))
        num2 = float(input("Introdueixi un segon número: "))

    elif seleccio == 10:
        print("Apagando.")
        time.sleep(1/3)
        print("Apagando..")
        time.sleep(1/3)
        print("Apagando...")
        time.sleep(1/3)
        print("Apagando....")
        time.sleep(1/3)
        operatiu = False
        os.system("exit")


time.sleep(1/10)
os.system(" ")
os.system("exit")

# num1 = float(input("Introduce tu primer número: ") )
# num2 = float(input("Introduce tu segundo número: ") )
