import random
import numpy
import os

os.system("color 0a")

def correr_app():

    Imatge = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    paraules=[]
    #Llista de paraules
    """
    paraules.append("Python")
    paraules.append("IBM")
    paraules.append("Variable")
    paraules.append("Base de dades")
    paraules.append("Array")
    paraules.append("Ciberseguretat")
    """
    paraules =[
            "PYTHON",
            "IBM",
            "VARIABLE",
            "LINK",
            "HELLO*WORLD",
            "GAME*OVER",
            "TALLA*FOCS",
            "HACKER",
            "CRACKER",
            "BLACK*HAT",
            "GREY*HAT",
            "WHITE*HAT",
            "JAVA",
            "PROGRAMARI",
            "BASE*DE*DADES",
            "VIRUS",
            "ALGORITME",
            "APP",
            "ARRAY",
            "CIBERSEGURETAT",
            "SYSTEM",
            "SOFTWARE",
            "XARXA",
            "EMPRENTA*DIGITAL",
            "CAFE"
    ]

    paraula_actual = random.choice(paraules)
    espais= ["_"]* len(paraula_actual)
    falls=0
    lletres_falls=[]

    while True:
        os.system("cls")
        print("""
       ___ _               ___      _
      / __(_)_ __ ___     / _ \___ (_)____
     / /  | | '__/ _ \   / /_\/ _ \| |_  /
    / /___| | | |  __/  / /_ \\ (_) | |/ /
    \____/|_|_|  \___|  \____/\___/|_/___|
        """)
        for index, charcater in enumerate(paraula_actual):
            if (charcater=="*"):
                espais[index] = "  "
        for charcater in espais:
            #if (charcater=="*"):
            #    print(" ",end="")
            print(charcater, end=" ")
        print(Imatge[falls])
        if(len(lletres_falls) >=1):
            print(f"Les lletres fallidas son: {lletres_falls}")

        eleccio =input("Escull una lletra: ").upper()


        acertat = False
        for index, charcater in enumerate(paraula_actual):
            if (charcater==eleccio):
                espais[index] = eleccio
                acertat = True
        if not acertat:
            falls+=1
            lletres_falls.append(eleccio)


        if ("_" not in espais): # Amb aixo comprem que ja no hi ha mes paraules per acertar
            os.system("cls")
            print("             Has guanyat")
            print(f"La paraula era {paraula_actual}")
            print("""
                               _      _
                              (_)    | |
                        __   ___  ___| |_ ___  _ __ _   _
                        \ \ / / |/ __| __/ _ \| '__| | | |
                         \ V /| | (__| || (_) | |  | |_| |
                          \_/ |_|\___|\__\___/|_|   \__, |
                                                     __/ |
                                                    |___/
                """)
            break
            input()#Es com un ReadKey()
        if (falls==6): # Amb aixo comprem que ja no hi ha mes paraules per acertar
            os.system("cls")
            print("             Has perdut ")
            print(f"La paraula era {paraula_actual}")
            print("""
                     ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
                     ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
                     ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
                     ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
                     ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
                     ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                     ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
                     ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
                     ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
                     ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
                     ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
                     ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                     ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
                     ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
                     ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
                     ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
                     ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
                     ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
                     ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
                     ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
                     ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
                     ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
                     ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
                                """)

            break
            input()#Es com un ReadKey()

correr_app()

#GoGo
#print("""

#  ______      _____     ______      _____
# /_/\___\    ) ___ (   /_/\___\    ) ___ (
# ) ) ___/   / /\_/\ \  ) ) ___/   / /\_/\ \
#/_/ /  ___ / /_/ (_\ \/_/ /  ___ / /_/ (_\ \
#\ \ \_/\__\\ \ )_/ / /\ \ \_/\__\\ \ )_/ / /
# )_)  \/ _/ \ \/_\/ /  )_)  \/ _/ \ \/_\/ /
# \_\____/    )_____(   \_\____/    )_____(


#""")
