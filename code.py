import math
import random

#deklarasi global
tabpop = {
    'kromosom' : [],
    'fitness' : []
}

#inisiasi batas interval x dan y
interval_x = [-5, 5]
interval_y = [-5, 5]

#ukuran populasi
n_kromosom = 10
n_gen = 10
generasi = 10

#random kromosom
def randKrom(gen):
    tabkrom = []
    for i in range(gen):
        tabkrom.append(random.randint(0,1))
    return tabkrom

#populasi untuk menampung kromosom
def buat_populasi(n_populasi, n_gen, tabpop):
    for i in range(n_populasi):
        tabpop['kromosom'].append(randKrom(n_gen))

#fungsi
def fungsi(x, y):
    h = (math.cos(x) + math.sin(y))**2 / (x**2 + y**2)
    return h

#metode dekode kromosom
def decodeKrom(kromosom, interval): #binary decoding
    jml_kali = 0
    jml_penyebut = 0
    for i in range(len(kromosom)):
        gen = kromosom[i]
        jml_kali += (gen *(2**-(i+1)))
        jml_penyebut +=(2**-(i+1))

    return interval[0] + (((interval[1] - interval[0]) / jml_penyebut) * jml_kali)

#membagi array menjadi 2 gamet: x dan y
def split(kromosom):
    return (kromosom[ : len(kromosom) // 2], kromosom[len(kromosom) // 2 : ])

#nilai fitness
def fitness(h):
    a = 0.0000000001
    return 1/(h + a) 

#perhitungan fitness
def hitungFitness(tabpop):
    for i in range(len(tabpop['kromosom'])):
        x, y = split(tabpop['kromosom'][i])
        gamet_x = decodeKrom(x, interval_x)
        gamet_y = decodeKrom(y, interval_y)
        f = fungsi(gamet_x, gamet_y)
        tabpop['fitness'].append(fitness(f))    

#pemilihan orang tua menggunakan roulette wheel selection
def RouletteWheelSelection(tabpop):
    total = 0
    for indv in range(len(tabpop['kromosom'])):
        total += tabpop['kromosom'][indv]

    r = random.random()
    indv = 0
    while(r > 0 & indv < len(tabpop['kromosom'])):
        r -= tabpop['fitness'][indv] / total
        indv += 1
    return indv - 1

#crossover single point
def crossover(parent1, parent2, prob):
    child1 = []
    child2 = []

    #mencari nilai random
    nilai = random.random()

    if nilai <= prob:
        p = random.randint(1, len(parent1) - 1) #mencari titik silang

        #offspring 1
        child1[ : p] = parent1[ : p]
        child1[p : ] = parent2[p : ]

        #offspring 2
        child2[ : p] = parent2[ : p]
        child2[p : ] = parent1[p : ]

    else:
        child1 = parent1
        child2 = parent2
    
    return (child1, child2)

#mutasi
def mutasi(krom, prob):

    for i in range (len(krom)):
        #mencari nilai random
        r = random.random()
        if r <= prob:
            if krom[i] == 0:
                krom[i] = 1
            else:
                krom[i] = 0
    return krom

#pergantian generasi
