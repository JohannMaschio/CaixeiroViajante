# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:55:47 2022
@author: Johann
"""
import matplotlib.pyplot as plt
import random
from random import randint
import math 

#Criando os vetores das coordenadas das cidades
def cidades(qnt_citys):
    x = []
    y = []
    #seed = random.seed(26)
    seed = random.seed(1)
    for i in range(qnt_citys):
        x.append(random.randrange(0, qnt_citys))
        y.append(random.randrange(0, qnt_citys))
    return x, y

#Imprime o mapa
def plot_all(seq):
    for indice in range(0, len(seq)):
        x_plot = []
        y_plot = []
        for i in range(0, quantidade_citys):
            x_plot.append(x[seq[indice][i]])
            y_plot.append(y[seq[indice][i]])
        plt.plot(x_plot, y_plot)
        plt.show()

# mandar somente o melhor individou do vetor
def plot_best(individuo):
    x_plot = []
    y_plot = []
    for i in range(0, quantidade_citys):
        x_plot.append(x[individuo[i]])
        y_plot.append(y[individuo[i]])
    plt.plot(x_plot, y_plot)
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
        for i in range(1, quantidade_citys, 2):
            fit += distancia(x[seq[indice][i]], y[seq[indice][i]], x[seq[indice][i-1]], y[seq[indice][i-1]])
        vet_fit.append(fit)
        fit = 0
    return vet_fit

#Cria a população inicial
def populacao_inicial(qtd_pop):
    individuo = []
    populacao = []
    for i in range(qtd_pop):
        while len(individuo) != quantidade_citys:
            random_int = randint(0, quantidade_citys-1)
            if random_int not in individuo:
                individuo.append(random_int)
        populacao.append(individuo)
        individuo = []
    return populacao

#Ordena a população pelo custo total
def ordena(fit, pop):
    aa = list(zip(fit, pop))
    teste_ord = sorted(aa, reverse=False)   
    return teste_ord

class lala():
    def crossover(pop):
        nova_pop = []
        fit_pop = fitness(pop)
        ordenado_by_fit = ordena(fit_pop, pop)
        for i in range(1, len(pop), 2):
            pai1 = []
            pai2 = []
            crom_filho = []
            filho1 = []
            filho2 = []
            pai1 = ordenado_by_fit[i][1]
            if (i < (len(pop)-1)):
                pai2 = ordenado_by_fit[i+1][1]
            else:
                pai2 = ordenado_by_fit[i-1][1]
            for x in range(quantidade_citys):
                 if random.random() < 0.7:
                     crom_filho.append("0")
                 else:
                     crom_filho.append("1")
            # primeiro filho
            for j in range(quantidade_citys):
                if crom_filho[j] == "0":
                    filho1.append(pai1[j])
                else:
                    filho1.append(0)
            for j in range(quantidade_citys):
                e = 0
                if filho1[j] == 0:
                    while (e != quantidade_citys):
                        if pai2[e] not in filho1:
                            filho1[j] = pai2[e]
                            e = quantidade_citys
                        else:
                            e += 1
            filho1 = lala.mutacao(filho1)
            
            # segundo filho
            for j in range(quantidade_citys):
                if crom_filho[j] == "1":
                    filho2.append(pai2[j])
                else:
                    filho2.append(0)
            for j in range(quantidade_citys):
                e = 0
                if filho2[j] == 0:
                    while (e != quantidade_citys):
                        if pai1[e] not in filho2:
                            filho2[j] = pai1[e]
                            e = quantidade_citys
                        else:
                            e += 1
            filho2 = lala.mutacao(filho2)

            nova_pop.append(filho1)
            nova_pop.append(filho2)
            
            fit_novo = fitness(nova_pop)
            nova_ord = ordena(fit_novo, nova_pop)
        return nova_ord
    
    def mutacao(filho):
        taxa_mutacao = random.random()
        quant = quantidade_citys
        filho_novo = filho
        if taxa_mutacao < 0.3:
            indice1 = randint(0, (quant-1))
            indice2 = randint(0, (quant-1))
            filho_novo[indice1], filho_novo[indice2] = filho_novo[indice2], filho_novo[indice1]
        return filho_novo

melhores = []
def resolver(pop):
    geracoes = 200
    melhor = [0][0]
    pop_cross = lala.crossover(pop)
    for i in range(geracoes):
        #print(f'gerações {i}')
        populacao = []
        for j in range(tamanho_pop):
            populacao.append(pop_cross[j][1])
        resultado = lala.crossover(populacao)
        if melhor < 1000000000:
            melhor = resultado[0][0]
            melhores.append(melhor)
        pop_cross = resultado
    return resultado

#inicia as cidades
quantidade_citys = 100
x, y = cidades(quantidade_citys)
print("\n Grafico inicial das cidades: ")
plt.plot(x,y)
plt.show()

tamanho_pop = 20
teste_pop = populacao_inicial(tamanho_pop)
teste_fit = fitness(teste_pop)

ordenado_by_fit = ordena(teste_fit, teste_pop)
teste_cross = lala.crossover(teste_pop)

finalmente = resolver(teste_pop)
plot_best(finalmente[0][1])
