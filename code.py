import math
import random

#DEKLARASI GLOBAL
tabpop = { #populasi random
    'kromosom' : [],
    'fitness' : []
}
    
newPop = { #populasi hasil rekayasa
    'kromosom' : [],
    'fitness'  : []
}

bestKrom = {
    'generasi' : [],
    'kromosom' : [],
    'fenotif x' : [],
    'fenotif y' : [],
    'fitness' : [],
}

#inisiasi batas interval x dan y
interval_x = [-5, 5]
interval_y = [-5, 5]

#ukuran populasi
n_kromosom = 10
n_gen = 10
generasi = 10

#probabilitas operasi genetik (pc dan pm)
prob_crossover = 0.8
prob_mutasi    = 0.01

#random kromosom
def randKrom(n_gen):
    tabkrom = []
    for i in range(n_gen):
        tabkrom.append(random.randint(0,1))
    return tabkrom


#populasi untuk menampung kromosom
def buat_populasi(n_krom, n_gen, tabpop):
    for i in range(n_krom):
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
        genotif = kromosom[i]
        jml_kali += (genotif *(2**-(i+1)))
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
        total += tabpop['fitness'][indv]

    r = random.random()
    indv = 0
    while(r > 0 & indv < len(tabpop['kromosom'])):
        r -= tabpop['fitness'][indv] / total
        indv += 1
    return tabpop['kromosom'][indv - 1]

#crossover single point
def crossover(parent1, parent2, prob):
    child1 = []
    child2 = []

    #mencari nilai random
    nilai = random.random()

    if nilai < prob:
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

#seleksi survivor
def elitism(tabpop, newpop):

    #mencari 2 bibit unggul
    for i in range(2):
        best = max(tabpop['fitness'])
        idx_best = tabpop['fitness'].index(best)

        newpop['kromosom'].append(tabpop['kromosom'][idx_best])
        newpop['fitness'].append(tabpop['fitness'][idx_best])
    
    return newpop



#PROGRAM UTAMA
#Pergantian Generasi dengan Generational Model

buat_populasi(n_kromosom, n_gen , tabpop) #membuat populasi random
hitungFitness(tabpop) #menghitung fitness setiap kromosom pada populasi

g = 1
while (g <= generasi): #kondisi penghentian

    #menyeleksi 2 bibit dengan fitness tertinggi
    newPop = elitism(tabpop, newPop)

    #menyimpan data bibit terunggul
    bestKrom['generasi'].append(g)
    bestKrom['kromosom'].append(newPop['kromosom'][0])
    bestKrom['fitness'].append(newPop['fitness'][0])

    x, y = split(newPop['kromosom'][0])
    bestKrom['fenotif x'].append(decodeKrom(x, interval_x))
    bestKrom['fenotif y'].append(decodeKrom(y, interval_y))

    while len(newPop['kromosom']) < n_kromosom:
        #menyeleksi parent
        parent1 = RouletteWheelSelection(tabpop)
        parent2 = RouletteWheelSelection(tabpop)

        #crossover
        ofs1, ofs2 = crossover(parent1, parent2, prob_crossover)

        #mutasi
        ofs1 = mutasi(ofs1, prob_mutasi)
        ofs2 = mutasi(ofs2, prob_mutasi)

        newPop['kromosom'].append(ofs1)
        newPop['kromosom'].append(ofs2)

    hitungFitness(newPop)
    tabpop = newPop
    g += 1

#Tampilan piranti
print("KROMOSOM TERBAIK DENGAN NILAI FUNGSI MINIMUM PADA TIAP GENERASI")
print("")
print('-' * 115)
print('{:<16}{:<3}{:<31}{:<3}{:<20}{:<3}{:<18}{:<3}{:<20}'.format('Generasi ke-','|','Kromosom','|','Fenotif x','|', 'Fenotif y','|', 'Nilai Fitness'))
print('-' * 115)
for i in range (len(bestKrom['generasi'])):
    print(bestKrom['generasi'][i], '\t\t| ', bestKrom['kromosom'][i], '| ', bestKrom['fenotif x'][i], '| ', bestKrom['fenotif y'][i], '| ', bestKrom['fitness'][i])


