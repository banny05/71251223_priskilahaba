def frekuensi_kata(kalimat, kata):
    kalimatbersih = kalimat.lower().replace(".", "").replace(",", "")
    katabersih = kata.lower()
    return kalimatbersih.split().count(katabersih)

kalimat = input("masukkan kalimat: ")
kata = input("masukkan kata: ")

frekuensi = frekuensi_kata(kalimat,kata)
print(f"{kata} ada {frekuensi} buah")