num_usuari = int(input("Siuspau interodueixi un numero enter positiu: "))
while(num_usuari <=0):#Anti negatius
    print("el numero insertat {num_usuari} no es positiu")
    num_usuari = int(input("Siuspau interodueixi un numero enter positiu: "))
Prim=True
#For per els divisibles
for iteracio in range(num_usuari):
    if( iteracio >=2 and iteracio!=num_usuari):#El num de iteracio no pot ser 0 o 1 y no pot ser el mateix numero per ell mateix
        divisible = num_usuari %iteracio
        resutlat =num_usuari/iteracio
    else:#Es un control per la primera iteracio (no es pot dividir per cero o donaria error)
        divisible = 1
    if(divisible== 0):
        print(f"""El numero {num_usuari} es divisible per {iteracio}
              (amb el numero {int(resutlat)})
        """)
        Prim = False
if(Prim==True):
    print(f"Cap,El nombre {num_usuari} es un nombre primer! ")
