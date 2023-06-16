# Function untuk menghitung jarak relasi antara dua orang
def check_distance(relations, first_person, second_person):
    # Base case
    if first_person == second_person:
        return 0
    
    elif first_person not in relations:
        raise ValueError(f"Tidak ada hubungan.")
        
    # Recursive case
    return 10 * relations[first_person][1] + check_distance(relations, relations[first_person][0], second_person)

# Relasi:
# A B 10
# B C 10 
# C D 10
# D E 10

# Inisialisasi dictionary untuk relasi dan input data relasi
dict_of_relations = {}
data_relasi = input("Masukkan data hubungan:\n")

while data_relasi != "SELESAI":
    first_person, second_person, distance_raw = data_relasi.strip().split(" ")
    distance = float(distance_raw)
    dict_of_relations[first_person] = (second_person, distance)
    data_relasi = input()

# Meminta input nama awal dan tujuan
first_person = input("Masukkan nama awal: ").strip()
second_person = input("Masukkan nama tujuan: ").strip()

# Mencetak jarak total dan relasi antara dua orang
try:
    total_distance = check_distance(dict_of_relations, first_person, second_person)
    print(f"Jarak total: {int(total_distance)}")
    
    if total_distance <= 100:
        print(f"{first_person} dan {second_person} kenal dekat.")
    elif total_distance <= 1000:
        print(f"{first_person} dan {second_person} mungkin saling kenal.")
    else:
        print(f"{first_person} dan {second_person} tidak saling kenal.")
except ValueError:
    print(f"Tidak ada hubungan antara {first_person} dan {second_person}.")
