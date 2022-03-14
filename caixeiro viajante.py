# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:55:47 2022
@author: Johann
"""

import matplotlib.pyplot as plt
import random
from random import randint
import numpy as np
import pandas as pd
import math 

#Criando os vetores das coordenadas das cidades
def cidades(qnt_citys):
    x = []
    y = []
    seed = random.seed(26)
    for i in range(qnt_citys):
        x.append(random.randrange(0, qnt_citys))
        y.append(random.randrange(0, qnt_citys))
    return x, y

#Imprime o mapa
def plot_all(seq):
    for indice in range(0, len(seq)):
        x_plot = []
        y_plot = []
        for i in range(0, 100):
            x_plot.append(x[seq[indice][i]])
            y_plot.append(y[seq[indice][i]])
        plt.plot(x_plot, y_plot)
        plt.show()

def plot_best(individuo):
    x_plot = []
    y_plot = []
    for i in range(0, 100):
        x_plot.append(x[individuo[i]])
        y_plot.append(y[individuo[i]])
    plt.plot(x_plot, y_plot)
    plt.show()

#inicia as cidades
x, y = cidades(100)
print("\n Grafico inicial das cidades: ")
plt.plot(x,y)
plt.show()

#Calcula a distencia entre uma cidade e outra
def distancia(xa, ya, xb, yb):
    dist = math.sqrt(((xb-xa)**2)+((yb-ya)**2))
    return dist

#Calcula a distancia percorrida por todas as cidades do vetor
def fitness(seq):
    fit = 0
    vet_fit = []
    for indice in range(0, len(seq)):
        for i in range(1, 100, 2):
            fit += distancia(x[seq[indice][i]], y[seq[indice][i]], x[seq[indice][i-1]], y[seq[indice][i-1]])
        vet_fit.append(fit)
        fit = 0
    return vet_fit

#Cria a população inicial
def populacao_inicial(qtd_pop):
    individuo = []
    populacao = []
    for i in range(qtd_pop):
        while len(individuo) != 100:
            random_int = randint(0, 99)
            if random_int not in individuo:
                individuo.append(random_int)
        populacao.append(individuo)
        individuo = []
    return populacao

teste_pop = populacao_inicial(20)
teste_fit = fitness(teste_pop)

#Ordena a população pelo custo total
def ordena(fit, pop):
    teste = list(zip(teste_fit, teste_pop))
    teste_ord = sorted(teste, reverse=False)   
    return teste_ord

ordenado_by_fit = ordena(teste_fit, teste_pop)

def crossover():
    
    return

def mutacao():
    
    return

## Fazer o algoritmo 
