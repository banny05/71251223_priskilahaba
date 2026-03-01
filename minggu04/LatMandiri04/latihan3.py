try:
    bulan = int(input("masukkan bulan (1-12) : "))
    if bulan < 1 or bulan > 12:
        print("input salah!")
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        print ("hari : 31")
    elif bulan == 2:
        print("hari : 29")
    else:
        print("hari : 30")
except:
    print("masukkan input nomor bulan!")


