gaji_perjam = int(input("gaji per jam yang diinginkan : Rp."))
jam_kerja_perminggu = int(input("jumlah jam kerja 1 minggu : "))

total_gaji_awal = gaji_perjam * jam_kerja_perminggu * 5
pajak = total_gaji_awal * 0.14
gaji_setelah_pajak = total_gaji_awal - pajak
pengeluaran_aksesoris = (gaji_setelah_pajak) * 0.10
pengeluaran_alat_tulis = (gaji_setelah_pajak) * 0.01
pengeluaran_tersier = pengeluaran_aksesoris + pengeluaran_alat_tulis
sedekah = (gaji_setelah_pajak - pengeluaran_tersier) * 0.25
untuk_anak_yatim = sedekah * 0.30
untuk_kaum_dhuafa = sedekah - untuk_anak_yatim


print("1. gaji sebelum pajak: Rp.",total_gaji_awal)
print("2. gaji setelah pajak: Rp.",gaji_setelah_pajak)
print("3. jumlah uang untuk membeli pakaian dan aksesoris: Rp.",pengeluaran_aksesoris)
print("4. jumlah uang untuk membeli alat tulis: Rp.",pengeluaran_alat_tulis)
print("5. jumlah uang sedekah: Rp.",sedekah)
print("6. jumlah uang  yang akan diterima anak yatim: Rp.",untuk_anak_yatim)
print("7. Jumlah uang yang akan diterima kaum dhuafa: Rp.",untuk_kaum_dhuafa)