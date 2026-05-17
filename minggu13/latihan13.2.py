data = ('Banny Priskila Haba', '71251223', 'Sabu Raijua, NTT')
print("Data:", data)
print()

print("NIM:", data[1])
print("NAMA:", data[0])
print("ALAMAT:", data[2])

print("NIM:", tuple(data[1]))
print()

print("NAMA DEPAN:", tuple(data[0].split()[1][1:]))
print()

print("NAMA TERBALIK:", tuple(data[0].split())[::-1])