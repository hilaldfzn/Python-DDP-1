print("Selamat datang di Pacil Mart!\n")
file_input = input("Masukkan nama file input: ")

try:
    with open(file_input, 'r') as file:
        lines = file.readlines()

    # Cek apakah file kosong atau tidak
    if not lines:
        print("File input ada tapi kosong")
    else:
        print("Berikut adalah daftar belanjaanmu:")
        print()
        print("{:<12s} | {:>8s} | {:>10s}".format("Nama Barang", "Jumlah", "Kembalian"))
        print("-----------------------------------")

        with open(file_input, 'r') as file:
            for line in file:
                nama_barang, uang_bayar, harga = line.split()
                uang_bayar = int(uang_bayar)
                harga = int(harga)

                # Menghitung jumlah barang yang dibeli dan kembalian uangnya
                jumlah = uang_bayar // harga
                kembalian = uang_bayar % harga

                print("{:<12s} | {:>8d} | {:>10d}".format(nama_barang, jumlah, kembalian))
        print()
        print("Terima kasih sudah belanja di Pacil Mart!")

# Exception ketika file tidak ditemukan
except FileNotFoundError:
    print("File tidak tersedia")
