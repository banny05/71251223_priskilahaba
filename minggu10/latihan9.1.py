file1 = input("File pertama: ")
file2 = input("File kedua: ")

try:
    handle1 = open(file1)
    handle2 = open(file2)

    a = handle1.readlines()
    b = handle2.readlines()

    handle2.close()
    handle1.close()
    
    bnyk_baris = max(len(a), len(b))

    for i in range(bnyk_baris):
        baris1 = a[i].rstrip()
        baris2 = b[i].rstrip()
        if baris1 != baris2:
            print("baris", i+1, "berbeda")
            print("file 1:", baris1)
            print("file 2:", baris2)
except:
    print("file tidak ada!")