def cek_digit_belakang(a1, a2, a3):
    if a1%10 == a2%10 or a2%10 == a3%10 or a1%10 == a3%10:
        return True
    else:
        return False

angka1 = int(input())
angka2 = int(input())
angka3 = int(input())
cek = cek_digit_belakang(angka1, angka2, angka3)
print (cek)

