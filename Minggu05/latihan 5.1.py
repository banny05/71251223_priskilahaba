def cek_angka(a1, a2, a3):
    if a1 != a2 and a1 != a3 and a2 != a3:
     if a1 + a2 == a3 or a2 + a3 == a1 or a1 + a3 == a2:
        return True
     else:
        return False
    else:
       return False
    
angka1 = int(input("angka pertama: "))
angka2 = int(input("angka kedua: "))
angka3 = int(input("angka ketiga: "))
cek = cek_angka(angka1, angka2, angka3)
print(cek)
