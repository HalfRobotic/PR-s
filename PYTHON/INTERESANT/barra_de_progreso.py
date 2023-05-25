import time


def barra_de_progreso(fraccion, total, tamano=30):
    fraccion = fraccion/total
    completado = int(fraccion*tamano)
    restante = tamano-completado
    barra = f"[{'|'*completado}{'/'*restante}]{fraccion:.2%}"
    return barra


n = 30

for i in range(n+1):
    time.sleep(0.1)
    print(barra_de_progreso(i, n, 35), end="\r")
print()
