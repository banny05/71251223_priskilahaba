counts = dict()
namafile = input("Masukkan nama file: ")

fhand = open(namafile)

for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

print(counts)