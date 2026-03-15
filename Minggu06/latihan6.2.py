def ganjil(atas,bawah):
    if atas<bawah:
        for i in range(bawah, atas - 1, -1):
            if i%2 != 0:
                print(i, end = " ")
    else:
        for i in range(bawah, atas + 1):
            if i % 2 != 0: 
               print (i, end = " ")

atas = int(input("Batas Atas: "))
bawah = int(input("Batas Bawah: "))
ganjil(atas,bawah)

