Import = 1 #Turns o Euros
valorDolar =0.98

while(Import<=16384):#Es parará cuant hagi fet 16384 Euros
    if(Import ==1):
        print(Import," euro = ",Import*valorDolar," dòlars")#Això es per la primera iteració
    else:
        print(Import," euros = ",Import*valorDolar," dòlars")
    Import*=2
