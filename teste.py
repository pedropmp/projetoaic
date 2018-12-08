# encoding:utf_8
#
# https://docs.scipy.org/doc/numpy/user/basics.creation.html
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
# https://docs.scipy.org/doc/scipy/reference/
import csv
from numpy import *
from scipy.interpolate import *
import matplotlib.pyplot as plt



def media(dados):

    print dados
    total = 0
    soma = 0.0
    media = 0
    for i in range(0, len(dados) - 1):
        soma = soma + eval(dados[i])
        total = total + 1
    media = soma / total
    return media


def mediana(dados):
    i = 0
    if (((len(dados) - 1)) % 2 == 1):
        i = (len(dados) - 1) / 2
        print dados[i]
    elif (((len(dados) - 1)) % 2 == 0):
        i = len(dados) / 2
        print dados[i - 1]
        print dados[i]


def moda(dados):
    moda = 0
    count = 0
    for i in range(0, len(dados) - 1):
        auxCount = 0
        for j in range(0, len(dados) - 1):
            if dados[i] == dados[j]:
                auxCount = auxCount + 1
        if auxCount > count:
            moda = i
            count = auxCount

    return dados[moda]


def regressao(dados):
    # === Regressao linear ===
    numeros = []
    contador = []
    c = 0
    for dado in dados[0:-1]:
        dado = float(dado)
        numeros.append(float(dado))
        c += 1
        contador.append(c)

    x = array(numeros)
    print 'x: ', x
    y = array(contador)
    print 'y:', y

    p1 = polyfit(x, y, 4)

    print p1

    plt.plot(x, y, 'o')
    plt.plot(x, polyval(p1, x))

    plt.show()



dt = csv.reader(file('teste2.csv'))
for reg in dt:
    for dado in reg:
        dados.append(dado)

media = media(dados)
mediana(dados)
moda = moda(dados)

print 'média: ', media
print 'moda: ', moda

regressao(dados)
variancia = variancia(dados, media)
desviop = desviop(variacia)