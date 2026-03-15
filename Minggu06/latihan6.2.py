def ganjil(atas,bawah):
    if atas<bawah:
        for i in range(bawah, atas - 1, -1):
            if i%2 != 0:
                print(i)
    else:
        for i in range(bawah, atas + 1):
            if i % 2 != 0: 
               print (i)

atas = int(input())
bawah = int(input())
ganjil(atas,bawah)