nota1 = float(input("Quina es la nota suspesa de Matematicas? "))
nota2 = float(input("Quina es la nota suspesa de Catala? "))
nota3 = float(input("Quina es la nota suspesa de Fisica? "))
nota4 = float(input("Quina es la nota suspesa de Quimica? "))
nota5 = float(input("Quina es la nota suspesa de Frances? "))

# numNotas = len(nota1,nota2,nota3,nota4,nota5)
notaSuma = nota1+nota2+nota3+nota4+nota5
notaMitja = notaSuma/5 #Es divideix per la cantitat de notas

print("La suma de totes les notes son: ",notaSuma)
print("La mitja de totes les notes son: ",notaMitja)
