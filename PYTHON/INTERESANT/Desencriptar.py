import time
import os
import numpy
import random
import tensorflow as tf
import cv2

# Primero desglosamos los problemas, en primera instancia los sencillos numericos.

# Problemas unicamente numerales
# Succesion de numeros (Patron) [1,3,5,7....][3,6,9,12...]
"""
def det_sucesion_num():
    #Distribueixo 5 arrais dades sucesives
    ejemplo1=[1,3,5,7,9]#num intercalados
    ejemplo2=[0,2,4,6,8]
    ejemplo3=[3,6,9,12,16]
    ejemplo4=[1,1,1,3,3,3,6,6,6]
    ejemplo5=[0,1,1,2,3,5,8,13]


    #Definimos las capas (Densas, no Densas)
    #units = cantidad neuronas
    #input_shape como indica son las entradas que tiene

    oculta1 =tf.keras.layers.Dense(units=3, input_shape=[1])
    oculta2 =tf.keras.layers.Dense(units=3)
    salida =tf.keras.layers.Dense(units=1)
    modelo=tf.keras.Sequential([oculta1,oculta2,salida])

    #Pre-entrenamiento(Optimizador y funcionn de perdidas)
    modelo. compile(
        optimizer=tf.keras.optimizers.Adam(0.1),
        loss='mean_squared_error'
def anagrama(frase_o_palabra):
"""


def cifratInvers(text):
    textCifrat = ''
    llistaLletres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                     'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    paraulaCambiada = ''
    for i in text:
        if (i != ' '):  # Per preservar els espais del text original
            if (str.lower(i) == 'a'):
                paraulaCambiada = 'z'
            elif (str.lower(i) == 'b'):
                paraulaCambiada = 'y'
            elif (str.lower(i) == 'c'):
                paraulaCambiada = 'x'
            elif (str.lower(i) == 'd'):
                paraulaCambiada = 'w'
            elif (str.lower(i) == 'e'):
                paraulaCambiada = 'v'
            elif (str.lower(i) == 'f'):
                paraulaCambiada = 'u'
            elif (str.lower(i) == 'g'):
                paraulaCambiada = 't'
            elif (str.lower(i) == 'h'):
                paraulaCambiada = 's'
            elif (str.lower(i) == 'i'):
                paraulaCambiada = 'r'
            elif (str.lower(i) == 'j'):
                paraulaCambiada = 'q'
            elif (str.lower(i) == 'k'):
                paraulaCambiada = 'p'
            elif (str.lower(i) == 'l'):
                paraulaCambiada = 'o'
            elif (str.lower(i) == 'm'):
                paraulaCambiada = 'n'
            elif (str.lower(i) == 'n'):
                paraulaCambiada = 'm'
            elif (str.lower(i) == 'o'):
                paraulaCambiada = 'l'
            elif (str.lower(i) == 'p'):
                paraulaCambiada = 'k'
            elif (str.lower(i) == 'q'):
                paraulaCambiada = 'j'
            elif (str.lower(i) == 'r'):
                paraulaCambiada = 'i'
            elif (str.lower(i) == 's'):
                paraulaCambiada = 'h'
            elif (str.lower(i) == 't'):
                paraulaCambiada = 'g'
            elif (str.lower(i) == 'u'):
                paraulaCambiada = 'f'
            elif (str.lower(i) == 'v'):
                paraulaCambiada = 'e'
            elif (str.lower(i) == 'w'):
                paraulaCambiada = 'd'
            elif (str.lower(i) == 'x'):
                paraulaCambiada = 'c'
            elif (str.lower(i) == 'y'):
                paraulaCambiada = 'b'
            elif (str.lower(i) == 'z'):
                paraulaCambiada = 'a'
            i = paraulaCambiada
        textCifrat += i
    print(textCifrat)


def cifratEspaiat(text):

    llistaLletres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                     'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    llistaCaracters = ['!', '@', '#', '~', '€',
                       "¿", '¡', '?', '|', 'º', 'ª', '*', '^']
    cantitat = int(input('Cada cuantes paraules vols espaiarlo? '))
    cifrat = ''
    x = 0
    for i in text:
        x += int(1)
        if (int(x % cantitat) == 0):
            eleccioActual = random.choice(llistaLletres)
            cifrat += str.upper(eleccioActual)
        cifrat += i
    print(cifrat)


def detectarPatrons(text):
    tamanyText = len(text)
    if (tamanyText>= 100):
        print("Hola")
    print("Aquest test es...")
