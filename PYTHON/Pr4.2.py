
num_usuari =int(input("Untrodueixi un numero enter siusplau: "))

divisor=2
residu=1000
etapa=0
dividend=num_usuari

while residu >2:#0-1 es el que no pot dividir 2 .Tambe podem cambiarho per la variable divisor
        quocient = dividend/divisor
        residu= quocient
        dividend=quocient
        etapa+=1
        print(f"quocient:{quocient} , residu:{residu},dividend:{dividend},etapa:{etapa}")
print("")
if(residu >0):
    print(f"El numero introduit {num_usuari} es divisible {etapa} vegades per {divisor}, amb un residu de {residu}")
else:
    print(f"El numero introduit {num_usuari} es divisible {etapa} vegades per {divisor}")
    print(f"O dit d'una altre manera {num_usuari} es igual que dir {divisor} a la {etapa}")
