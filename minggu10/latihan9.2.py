namafile = input("nama file: ")

try:
    handle = open(namafile)

    for line in handle:
        b = line.strip().split("||")
        soal = b[0].strip()
        jwbn_bnr = b[1].strip()
        print(soal)
        jawab = input("jawab:")

        if jawab.lower()==jwbn_bnr.lower():
            print("Jawaban benar!")
        else:
            print("Jawaban salah!")
        print()

    handle.close()
except:
    print("File tidak ada!")