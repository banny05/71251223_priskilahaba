try:
    sisi1 = int(input("panjang sisi pertama: "))
    sisi2 = int(input("panjang sisi kedua: "))
    sisi3 = int(input("panjnag sisi ketiga: "))

    if sisi1 == sisi2 == sisi3 :
        print("3 sisi  sama")
    elif  (sisi1 == sisi2) or (sisi2 == sisi3) or (sisi1 == sisi3):
        print ("2 sisi sama")
    else:
        print("tidak ada sisi yang sama")
except:
    print("input salah!")


