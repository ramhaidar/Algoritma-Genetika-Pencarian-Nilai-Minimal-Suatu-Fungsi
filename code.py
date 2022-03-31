#inisiasi batas interval x dan y
interval_x = [-5, 5]
interval_y = [-5, 5]

#ukuran populasi
n_kromosom = 10
n_gen = 10
generasi = 10

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
#pemilihan orangtua
#crossover
#mutasi
#pergantian generas
