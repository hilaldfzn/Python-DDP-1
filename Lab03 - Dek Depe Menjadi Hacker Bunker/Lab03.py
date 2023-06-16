print("Selamat Datang di Bunker Hacker!")
print()

# Meminta input dari user untuk banyak pengkonversian
banyak_konversi = int(input("Masukkan berapa kali konversi yang ingin dilakukan: "))

# Validasi input yang tidak valid
while banyak_konversi <= 0:
    print("Input tidak valid.")
    banyak_konversi = int(input("Masukkan berapa kali konversi yang ingin dilakukan: "))
print()

# Meminta input untuk bilangan yang ingin dikonversi
for i in range(1, banyak_konversi + 1):
    decimal = int(input(f"Masukkan angka ke-{i} yang ingin dikonversikan (dalam desimal): "))

    # Inisialisasi string kosong octal untuk mengumpulkan sisa pembagian x dengan 8
    octal =" "

    # Melakukan konversi decimal ke octal
    while decimal != 0:
        hasil_bagi = decimal // 8
        sisa = decimal % 8
        decimal = hasil_bagi
        octal += f"{sisa}"
    octal = (octal[::-1])

    # Mencetak hasil konversi decimal ke octal
    print(f"Hasil konversi desimal ke basis 8 : {octal}")
    print()

print("Terima kasih telah menggunakan Bunker Hacker!")
