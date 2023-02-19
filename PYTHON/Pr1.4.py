numN = float(input("Siusplau introuigui un numero positiu: "))
if(numN<0):#Atni negativos
    print("El numero no es positiu")
    numN = float(input("Siusplau torni a introdui un numero: "))
divisible = numN%2
if(divisible == 0 ):
    print("El número ",numN," es divisible per 2")
    print("PARELL")
else:
    print("El número ",numN," no es divisible per 2")
    print("IMPAR")
