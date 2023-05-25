import os
import random

datesRelacionades=[
"24", "13", "07", "2002","1969","1950","1234","1789","1978","1987","69"
]
musicaRelacionada=[
"ACDC", "Mozart", "Morat", "Bach", "Chopin", "Nach", "JP", "Fito", "Fiti", "paldis","Sabrina","Carpenter","Dante"
]
paraulesRelacionades = [
"Linus","Benedict","Torvalds","Steven","Gary","Wozniak","Addie","Lamarr","Anime","SAO","Monster","Cafe","Python","Mr.Robot","GPT","Spotify","Prg","Gaming","xxx","Html","Guitarra","Sing"
]
simbols=[
    "Z", "_", "-", ".", "~", "$", "€", "!", "¿", "?", "*", "A", "E", "I", "O", "U","a", "e", "i", "o", "u","@","#"
]
paraulesRelacionades.extend(datesRelacionades)
paraulesRelacionades.extend(musicaRelacionada)
paraulesRelacionades.extend(simbols)
def escullir_contrasenya():
    eleccio=input("""Escull quina contrasenya vols:
                                                    facil(<10caracters )
                                                    intermitga(>10c && <20c)
                                                    llarga(>20c)
                                                    HARDCORE(>40CARACTERS)[psicopata]
    """)
    if(str.lower(eleccio) in ["facil","intermitg","intermitga","llarga","hardcore"]):
        if(str.lower(eleccio)=="facil"):#FACIL
            contra=""
            while len(contra)<10:
                proximaParaula = random.choice(paraulesRelacionades)
                paraulaAnterior = proximaParaula
                if (paraulaAnterior in datesRelacionades and proximaParaula in datesRelacionades):
                    proximaParaula = random.choice(paraulesRelacionades)#Para no repetir numeros muy seguido
                if(len(contra)==0 or len(contra)+len(proximaParaula) <= 10):
                    contra+=proximaParaula
                    print(f"la contra de moment es {contra}")
    elif(str.lower(eleccio)=="intermig"):#INTERMIG
        contra = ""
        while len(contra) <20:
            proximaParaula = random.choice(paraulesRelacionades)
            paraulaAnterior = proximaParaula
            if (paraulaAnterior in datesRelacionades and proximaParaula in datesRelacionades):
                #No repetir numeros
                proximaParaula = random.choice(paraulesRelacionades)
            if(len(contra) == 0 or len(contra)+len(proximaParaula) <= 20):
                contra += proximaParaula
                print(f"la contra de moment es {contra}")
        print(f"La teva contrasenya es {contra}")
if __name__ == "__main__":
    escullir_contrasenya()

"""
NO SE QUE PENSABA CUANDO PROGRAME ESTO 
contra_info = [
"ElTemorAlNombreSoloAumentaElTemorAlHombre",
"MementoMoriCarpeDiem",
"DynamoLinusDumbeldorePlatzi"
"Python,C#,Html5,Arduino,R2D2,C3PO"]#Crpt

frase_secreta_de_recuperacion=[
"strong census garment crop nice town suspect body sock save question fabric"]

Seguir =True
while( Seguir==True):
    os.system("cls")

    longitud_array = len(contra_info)
    #num_Aleatori=random.randint(1,contra_info)
    #contra_magica=contra_info[num_Aleatori]
    print(contra_info)
    #print(f"La longitud de la contraseña es {longitud_array} caracters")
    Un_altre=input("Vols saber un altre nom:")
    if(Un_altre.upper()=="SI"):
        Seguir=True
    else:
        Seguir=False
"""
