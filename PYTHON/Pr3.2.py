multi = int(input("Per a quin numer vols multiplicar-ho? "))
taula = 1
resultat = 0
Multiple= int(input("Per a quin numero vols saber que sigui multiple? "))

while(taula!=21):
    resultat=taula*multi
    taula+=1
    if((resultat%Multiple)==0):#Multiple
        print(resultat,"*")
    else:
        print(resultat)
