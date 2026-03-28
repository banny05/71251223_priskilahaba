def prima(p):
    if p < 2:
        return False
    for i in range (2, int (p**0.5)+1):
        if p % i == 0:
            return False
    return True
def prima_terdekat(n):
    if n <=2:
        print(f"tidak ada bilangan prima yang lebih kecil dari {n}")
        return
    for i in range (n-1, 1, -1):
        if prima(i):
            return i
n = int(input("Masukkan nilai p: "))
print(prima_terdekat(n))


    