#Fibonnacci
#Nombres enters cada proxim terme es la suma de dos termes

num_Fb = int(input("Quin numero de Fibonnacci vols veure? "))
Fn_1=0;Fn_2=1
iteracio= 0
Fb=Fn_1+Fn_2

for iteracio in range(num_Fb):#
    Fb=Fn_1+Fn_2
    #print(Fb)
    if(iteracio%2==0):
        Fn_2+=Fn_1
    else:
        Fn_1+=Fn_2
    iteracio+=1
print(Fb)








"""
for iteracio in range(num_Fb ):#El +1 per igualar el numero que vol el usuari
    numFibonnacci=num1
    num1+=num2
    num2+=num1
    iteracio+=1
    print(f"{iteracio}: {numFibonnacci},{num1},{num2}")
print(f"El numero {num_Fb} de Fibonnacci es {numFibonnacci}")


num_voltes = int(input("Cuants numeros de Fibonnacci vols veure? "))
num1=0
num2=1

for a in range (num_voltes+1):
    print(num1)
    print(num2)
    num1+=num2
    num2+=num1
"""
