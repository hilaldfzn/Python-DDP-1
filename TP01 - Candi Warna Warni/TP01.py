import random
from turtle import *

# Mengatur layar dan warna background
Screen().bgcolor("green")

# Input dari user untuk jumlah batu bata pada lapisan bawah
lapisan_bawah = numinput("Lapisan bawah", "Jumlah bata lapisan bawah: ", minval = 1, maxval = 25)
if lapisan_bawah == None:
    exit() # Akan keluar dari program ketika memilih cancel
else:
    while lapisan_bawah != round(lapisan_bawah): # Program akan meminta input ulang saat mendapat input user berupa float
        lapisan_bawah = numinput("Lapisan bawah", "Jumlah bata lapisan bawah: ", minval = 1, maxval = 25)
        if lapisan_bawah == None:
            exit()
    lapisan_bawah = int(lapisan_bawah)

# Input dari user untuk jumlah batu bata pada lapisan atas
lapisan_atas = numinput("Lapisan atas", "Jumlah bata lapisan atas: ", minval = 1, maxval = lapisan_bawah)
if lapisan_atas == None:
    exit()
else:
    while lapisan_atas != round(lapisan_atas):
        lapisan_atas = numinput("Lapisan atas", "Jumlah bata lapisan atas: ", minval = 1, maxval = lapisan_bawah)
        if lapisan_atas == None:
            exit()
    lapisan_atas = int(lapisan_atas)

# Input dari user untuk panjang batu bata
panjang_bata = numinput("Panjang batu bata", "Panjang satu buah batu bata (piksel): ", minval = 1, maxval = 35)
if panjang_bata == None:
    exit()

# Input dari user untuk lebar batu bata
lebar_bata = numinput("Lebar batu bata", "Lebar satu buah batu bata (piksel): ", minval = 1, maxval = 25)
if lebar_bata == None:
    exit()
        
# Starting value
total_bata = 0
x_position = 0 # Koordinat awal sumbu x
y_position = (lapisan_atas - lapisan_bawah)*lebar_bata // 2 # Koordinat awal sumbu y
y_temporary = y_position - 15
title("Candi Warna-Warni")
colormode(255)
speed(1000) # Mempercepat turtle dalam membentuk candi

# Melakukan looping batu bata dari lapisan paling bawah ke atas
for a in range(lapisan_bawah,lapisan_atas-1,-1): 
    x_position = -a * panjang_bata/2 # Mendefinisikan ulang posisi x
    for b in range(a): 
        if a == lapisan_atas or a == lapisan_bawah or b == 0 or b == a-1: 
            fillcolor("#BC4A3C") # Mengisi warna asli batu bata pada bagian pinggir candi dengan kode heksadesimal
        else:
            fillcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255)) # Mengisi warna-warni (random) pada bagian tengah candi
        begin_fill() # Mengaktifkan mode untuk mengisi interior gambar dengan warna yang dipilih

        penup()
        goto(x_position,y_position + 10) # Memindahkan koordinat turtle ke lapisan baru
        pendown()
        forward(panjang_bata)
        left(90)
        forward(lebar_bata)
        left(90)
        forward(panjang_bata)
        left(90)
        forward(lebar_bata)
        left(90)
        end_fill() 
        total_bata += 1 # Menjumlahkan seluruh batu bata yang membentuk candi
        x_position += panjang_bata 
    y_position += lebar_bata

# Memindahkan koordinat turtle dan mencetak pesan total batu bata
penup()
goto(0,y_temporary) # Memindahkan koordinat turtle tepat di bawah candi
pendown()
write(f"Candi warna-warni dengan {total_bata} batu bata", align="center", font="Verdana") # Mencetak teks total batu bata dalam pembuatan candi
hideturtle()
exitonclick()
