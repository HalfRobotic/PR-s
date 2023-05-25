import os#Amb aixo podem manipular o escriure com si estiguesim al cmd
import time

os.system("cls")#Neteja la pantalla
os.system("color 0a")#Canvi de color 0a=verd fons negre

n1 = float(input("Introdueix un primer número: ") )
n2 = float(input("Introdueix un segundo número: ") )
os.system("cls")
opcion = 0
while True:#Bucle infinit
    print(f"""
        Primer Valor: {n1}
        Segon Valor: {n2}
    Tens diferents opcions:

    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5)Potencia
    6) Cambiar els números escollits
    7) Power Off

    """)
    opcion = int(input("Digues, ¿qué vols fer? ") )
    time.sleep(1)
    os.system("cls")
    if opcion == 1:#Sumar
        print(" ")
        print(f"RESULTADO: La suma de {n1}+{n2} es igual a {n1+n2}")
    elif opcion == 2:#Restar
        print(" ")
        print(f"RESULTADO: La suma de {n1}-{n2} es igual a {n1-n2}")
    elif opcion == 3:#Multiplicar
        print(" ")
        print(f"RESULTADO: La multiplicacio de {n1} x {n2} es igual a {n1*n2}")
    elif opcion == 4:#Dividir
        print(" ")
        print(f"RESULTADO: La divisió de {n1} / {n2} es igual a {n1/n2}")
    elif opcion ==5:#Potencia
        # os.system("cls")#Netejem la pantalla
        print(" ")
        print(f"Resultat= La potencia de {n1} a la {n2} es {n1**n2}")
    elif opcion == 6:#Cambiar los numeros
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
    elif opcion == 7:#Apagar
        break#Apaga el programa

    else:
        print("Opción incorrecta")

    time.sleep(1)
