import math

# Meminta input dari user
nama = input("Nama: ")
panjang_persegi = float(input("Panjang persegi nametag (cm): "))
panjang_trapesium = float(input("Panjang trapesium nametag (cm): "))
banyak_nametag = int(input("Banyak nametag: "))

# Data nilai radius serta tinggi segitiga dan trapesium
radius = panjang_persegi / 2
tinggi_segitiga = tinggi_trapesium = panjang_persegi

# Menghitung luas setiap bangun datar
luas_persegi = math.pow(panjang_persegi, 2)
luas_segitiga = panjang_persegi * tinggi_segitiga / 2
luas_setengah_lingkaran = math.pi * math.pow(radius, 2) / 2
luas_trapesium = (panjang_persegi + panjang_trapesium) * tinggi_trapesium / 2

# Menghitung luas nametag
luas_nametag = luas_persegi + luas_segitiga + luas_setengah_lingkaran + luas_trapesium
luas_total_nametag = luas_nametag * banyak_nametag

# Menghitung total biaya
biaya_total = math.ceil(luas_total_nametag * 0.40 / 1000) * 1000

# Mencetak hasil
print("\nHalo, {0}! Berikut informasi terkait nametag kamu:\n".format(nama))
print("Luas 1 nametag: {0:.2f} cm^2".format(luas_nametag))
print("Luas total nametag: {0:.2f} cm^2".format(luas_total_nametag))
print("Uang yang diperlukan: Rp" + str(biaya_total))
