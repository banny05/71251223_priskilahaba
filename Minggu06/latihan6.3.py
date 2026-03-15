def ips():
    print("Program penghitung IPS Mahasiswa")
    jumlah_mata_kuliah = int(input("Berapa jumlah mata kuliah? "))
    sks = 3
    total_bobot = 0
    total_sks = 0

    for i in range (1, jumlah_mata_kuliah +1):
        nilai = input(f"Nilai MK {i} : ")
        if nilai == "A":
            bobot = 4
        elif nilai == "B":
            bobot = 3
        elif nilai == "C":
            bobot = 2
        elif nilai == "D":
            bobot = 1
        else:
            bobot = 0

        total_bobot += bobot * sks
        total_sks += sks

    ips = total_bobot / total_sks
    print(f"Nilai IPS anda semester ini {ips:.2f}")
ips()


