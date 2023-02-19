parametre_usuari = int(input("Introdueixi un parametre:"))

#Imprimir tantes vegades com el usuari demani
contorn="-"
pintat = "#"
# superior = contorn*parametre_usuari
# intermitg = pintat*parametre_usuari
# superior = contorn*parametre_usuari
#Comença la linea
if(parametre_usuari<=0):
    print(f"+{contorn*parametre_usuari}{contorn}+")
    for iteracions in range(parametre_usuari+1):
        print(f"|{pintat*parametre_usuari} |")
    print(f"+{contorn*parametre_usuari}{contorn}+")
else:
    print(f"+{contorn*parametre_usuari}{contorn}+")
    for iteracions in range(parametre_usuari+1):
        print(f"|{pintat*parametre_usuari}{pintat}|")
    print(f"+{contorn*parametre_usuari}{contorn}+")
