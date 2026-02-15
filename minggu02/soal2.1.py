tinggi = float(input("Tinggi(cm) : "))
bmi = float(input("BMI yang diharapkan : "))
berat = (tinggi/100)**2 * bmi
print (f"Berat yang diperlukan {round(berat,1)} kg")