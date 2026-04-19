import re
from datetime import datetime

def cari_tanggal(teks):
    pola = r'\d{4}-\d{2}-\d{2}'
    tgl = re.findall(pola, teks)
    sekarang = datetime.now()
    
    for tanggal in tgl:
        date = datetime.strptime(tanggal, "%Y-%m-%d")
        selisih = abs((sekarang- date).days)
        print(f"{date} selisih {selisih} hari")

teks = input("masukkan teks: ")
cari_tanggal(teks)