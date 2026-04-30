def ratarata(data):
    isilist = []
    for i in data:
        isilist.append(int(i))
    hasil = sum(isilist) / len(isilist)
    print(hasil)

isi = input().split()
isi.remove("done")
ratarata(isi)
