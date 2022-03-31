import math
import random

#deklarasi global
tabpop = {
    'fenotif' : [],
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
def kromosom(gen):
    tabkrom = []
    for i in range(gen):
        tabkrom.append(random.randint(0,1))
    return tabkrom

#populasi untuk menampung kromosom
def populasi(populasi, gen):
    tabpop = []
    for i in range(populasi):
        tabpop.append(kromosom(gen))
    return tabpop

#fungsi
def fungsi(x, y):
    h = (math.cos(x) + math.sin(y))**2 / (x**2 + y**2)
    return h

#metode dekode kromosom
def decodeKrom(kromosom, interval): #binary decoding
    jml_kali = 0
    jml_penyebut = 0
    for i in range(len(kromosom)):
        genotif = kromosom[i]
        jml_kali += (genotif *(2**-(i+1)))
        jml_penyebut +=(2**-(i+1))

    return interval[0] + (((interval[1] - interval[0]) / jml_penyebut) * jml_kali)

#perhitungan fitness
def fitness(h):
    a = 0.0000000001
    return 1/(h + a) 

#pemilihan orang tua menggunakan roulette wheel selection
def RouletteWheelSelection(tabpop):
    total = 0
    for indv in range(len(tabpop['fenotif'])):
        total += tabpop['fitness'][indv]

    r = random.random()
    indv = 0
    while(r > 0 & indv < len(tabpop['fenotif'])):
        r -= tabpop['fitness'][indv] / total
        indv += 1
    return indv - 1

#crossover
#mutasi
#pergantian generasi
