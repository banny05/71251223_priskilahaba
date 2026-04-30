def kata_unnik(k):
    kata = []
    for i in k:
        if i not in kata and i.isalpha():
            kata.append(i)
    print(f"kata unik: {kata}")
    print(f"banyak kata unnik: {len(kata)}")

with open("artikel.txt", "r") as f:
    isi = f.read().lower().split()

kata_unnik(isi)
