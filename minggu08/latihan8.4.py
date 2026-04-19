def cari_kata(kalimat):
    kata = kalimat.split()
    terpendek = kata[0]
    terpanjang = kata[0]

    for k in kata:
        if len(k) < len(terpendek):
            terpendek = k
        if len(k) > len(terpanjang):
            terpanjang = k
    return terpendek, terpanjang

kalimat = input("masukkan kalimat: ")
terpendek, terpanjang = cari_kata(kalimat)
print(f"terpendek: {terpendek}")
print(f"terpanjang: {terpanjang}")