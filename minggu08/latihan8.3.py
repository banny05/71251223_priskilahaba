def hapus_spasi(kalimat):
    return" ".join(kalimat.split())

kalimat = input("masukkan kalimat: ")
hasil = hapus_spasi(kalimat)
print(f"hasil: {hasil}")