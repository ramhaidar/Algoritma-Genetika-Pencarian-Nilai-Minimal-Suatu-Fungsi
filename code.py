import math
import random

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

#pemilihan orangtua
#crossover
#mutasi
#pergantian generas
