def anagram(katapertama, katakedua):
    katapertama = katapertama.lower().replace(" ", "")
    katakedua = katakedua.lower().replace(" ", "")
    return sorted(katapertama) == sorted(katakedua)

katapertama = input("Masukkan kata pertama: ")
katakedua = input("Masukkan kata kedua: ")

if anagram(katapertama, katakedua):
    print(f"{katapertama} dan {katakedua} merupakan anagram.")
else:
    print(f"{katapertama} dan {katakedua} bukan anagram.")