print("""
Selamat mencoba Program Pemeriksa Nilai Dek Depe!
=================================================
""")

kunci_jawaban = []
print("Masukkan kunci jawaban:")

# Meminta input jawaban, jika STOP maka program akan berhenti meminta input
while True:
    command = input()
    if command == "STOP":
        break
    kunci_jawaban.append(command)

jawaban_benar = []
print("Masukkan jawaban kamu:")

# Menambahkan jawaban benar ke list dan menghitung nilai
for i, kunci in enumerate(kunci_jawaban):
    jawaban = input()
    if jawaban == kunci:
        jawaban_benar.append(jawaban)

nilai = 100 * len(jawaban_benar) // len(kunci_jawaban)

# Mencetak pesan sesuai dengan interval nilai
if nilai >= 85:
    print("Selamat :D")
elif 55 <= nilai < 85:
    print("Semangat :)")
else:
    print("nt")

# Mencetak total jawaban benar dan nilai yang diperoleh
print(f"Total jawaban benar adalah {len(jawaban_benar)} dari {len(kunci_jawaban)} soal")
print("Nilai yang kamu peroleh adalah", nilai)
