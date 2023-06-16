import math

# Function untuk menghitung volume balok
def hitung_volume_balok():
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))
    volume = panjang * lebar * tinggi
    return volume

# Function untuk menghitung volume kerucut
def hitung_volume_kerucut():
    radius = float(input("Masukkan jari-jari kerucut: "))
    tinggi = float(input("Masukkan tinggi kerucut: "))
    volume = 1/3 * math.pi * math.pow(radius, 2) * tinggi
    return volume

print("Selamat datang di Depot Minuman Dek Depe")
print("==========================================")

total_volume = 0

while True:
    # Meminta input user untuk bentuk galon
    bentuk_galon = input("Masukkan bentuk galon yang diinginkan (STOP untuk berhenti): ")
    
    # Penjumlahan volume berdasarkan bentuk galon, jika STOP maka program akan berhenti meminta input
    if bentuk_galon == "KERUCUT":
        total_volume += hitung_volume_kerucut()
    elif bentuk_galon == "BALOK":
        total_volume += hitung_volume_balok()
    elif bentuk_galon == "STOP":
        break
    else:
        print("Input tidak benar, silakan masukkan kembali")
    print()

# Ringkasan output berdasarkan total volume yang didapat nol atau tidak
if total_volume == 0:
    print("====================================================")
    print("Anda tidak memasukkan input satupun :(")
    print("Terima kasih telah menggunakan Depot Air Minum Dek Depe")
    print("====================================================")
else:
    total_harga = total_volume * 700
    print("====================================================")
    print(f"Total volume air yang dikeluarkan adalah: {total_volume:.2f}")
    print(f"Total harga yang harus dibayar adalah: Rp{total_harga:.2f}")
    print("====================================================")
    print("Terima kasih telah menggunakan Depot Air Minum Dek Depe")
