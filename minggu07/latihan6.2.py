import math
a = int(input("masukkan nilai a : "))
for i in range(a, 0, -1):
    faktorial = math.factorial(i)
    print(faktorial, end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()