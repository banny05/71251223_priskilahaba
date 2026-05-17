namafile = input("Enter a file name: ")
try:
    fhand = open(namafile)
except:
    print("File tidak bisa dibuka:", namafile)
    quit()

xyz = dict()
for baris in fhand:
    if not baris.startswith("From "):
        continue
    kata = baris.split()
    waktu = kata[5]
    jam = waktu.split(":")[0]

    if jam not in xyz:
        xyz[jam] = 1
    else:
        xyz[jam] += 1

lis = list()
for jam, jumlah in xyz.items():
    lis.append((jam, jumlah))
lis.sort()

for jam, jumlah in lis:
    print(jam, jumlah)