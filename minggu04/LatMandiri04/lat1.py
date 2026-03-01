
inputuser = input("masukkan suhu: ")
try  :
    suhu = int(inputuser)
    if suhu >= 38:
        print ("anda demam")
    else:
        print("anda tidak demam")
except:
    print("input tidak sesuai")

#positif-negatif
inputuser = input("masukkan bilangan : ")
try :
    bilangan = int(inputuser)
    if bilangan > 0:
        print ("positif")
    elif bilangan < 0:
        print ("negatif")
    elif bilangan == 0:
        print("nol")
except:
    print("inputan tidak sesuai")

#bilangan terbesar
try :
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    c = int(input("Masukkan bilangan ketiga: "))

    # secara berurutan tulis kriteria untuk a, b, dan c
    if a > b and a > c:
        print("Terbesar: ", a)
    elif b > a and b > c:
        print("Terbesar: ", b)
    elif c > a and c > b:
        print("Terbesar: ", c)
except :
    print("inputan tidak sesuai")


