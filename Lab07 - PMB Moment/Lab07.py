print("Selamat datang di program Mengenal Angkatan!")
print("===========================================")

# Inisialisasi dictionary untuk nama dan npm
dict_of_nama = {}
dict_of_npm = {}

# Meminta input identitas mahasiswa, jika STOP program akan berhenti meminta input
print("Masukkan identitas mahasiswa:")
while True:
    query = input()
    if query == "STOP":
        print()
        break
    
    # Mengambil data nama, npm, dan bulan melalui indeks input yang sudah displit
    splitted_query = query.split(" ")
    nama = splitted_query[0]
    npm = splitted_query[1]
    bulan = splitted_query[4]

    # Mengupdate dictionary serta menambahkan nama dan npm yang berkorespondensi dengan bulan lahir
    dict_of_nama.setdefault(bulan, set()).add(nama)
    dict_of_npm.setdefault(bulan, set()).add(npm)

# Meminta input untuk mencari mahasiswa berdasarkan bulan lahir, jika STOP program akan berhenti meminta input
while True:
    bulan_lahir = input("Cari mahasiswa berdasarkan bulan: ")
    if bulan_lahir == "STOP":
        break
    
    # Mencetak hasil data nama dan npm mahasiswa yang dicari berdasarkan bulan lahir
    print("================= Hasil ================")
    if bulan_lahir in dict_of_nama:
        print(f"Terdapat {len(dict_of_nama[bulan_lahir])} nama yang lahir di bulan {bulan_lahir}:")
        for nama in dict_of_nama[bulan_lahir]:
            print(f"- {nama}")

        print()
        print(f"Terdapat {len(dict_of_npm[bulan_lahir])} NPM yang lahir di bulan {bulan_lahir}:")
        for npm in dict_of_npm[bulan_lahir]:
            print(f"- {npm}")

    # Dicetak ketika tidak ada mahasiswa dengan bulan lahir yang dicari pada input
    else:
        print(f"Tidak ditemukan mahasiswa dan NPM yang lahir di bulan {bulan_lahir}.")
    print()

print()
print("Terima kasih telah menggunakan program ini, semangat PMB-nya!")
