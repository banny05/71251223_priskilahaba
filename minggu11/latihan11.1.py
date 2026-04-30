def tiga_terbaik(daftar_angka):
    
    daftar_angka.sort(reverse=True)
    print(f"3 angka terbaik adalah {", ".join(map(str, daftar_angka[:3]))}")

p = input()
daftar_angka = list(map(int, p.split()))
tiga_terbaik(daftar_angka)
