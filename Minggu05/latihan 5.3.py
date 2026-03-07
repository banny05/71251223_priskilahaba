c_f = lambda celcius : (9/5)* celcius + 32 
c_r = lambda celcius : 0.8 * celcius

celcius = float(input("masukkan suhu (C): "))

pilih = input("masukkan pilihan konversi: ")
if pilih == "Celcius to Fahrenheit":
    print(f"F: {celcius} = {c_f(celcius)} °F")
elif pilih == "Celcius to Reamur":
    print(f"R: {celcius} = {c_r(celcius)} °R")
else:
    print("tidak dalam pilihan!")
