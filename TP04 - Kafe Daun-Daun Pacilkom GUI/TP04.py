import random
import copy 
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

class Menu:
    def __init__(self, kode_menu, nama_menu, harga):
        self.kode = kode_menu
        self.menu = nama_menu
        self.harga = int(harga)
        self.list_menu = [self.kode, self.menu, self.harga]

    def getTuple(self):
        return tuple(self.list_menu)

class Meals(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kegurihan):
        super().__init__(kode_menu, nama_menu, harga)
        self.kegurihan = tingkat_kegurihan
        self.list_menu.append(self.kegurihan)
        self.list_menu.append(0)

    def getTuple(self):
        return tuple(self.list_menu)

class Drinks(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kemanisan):
        super().__init__(kode_menu, nama_menu, harga)
        self.kemanisan = tingkat_kemanisan
        self.list_menu.append(self.kemanisan)
        self.list_menu.append(0)

    def getTuple(self):
        return tuple(self.list_menu)

class Sides(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_keviralan):
        super().__init__(kode_menu, nama_menu, harga)
        self.keviralan = tingkat_keviralan
        self.list_menu.append(self.keviralan)
        self.list_menu.append(0)

    def getTuple(self):
        return tuple(self.list_menu)

class Main(tk.Frame): 
    def __init__(self, master = None):
        super().__init__(master)

        self.master.geometry("400x200")
        self.pack()
        master.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        self.btn_pesan = tk.Button(self, text="Buat Pesanan", width=30, command=self.buat_pesanan, bg="#4472C4", fg="white")
        self.btn_selesai = tk.Button(self, text="Selesai Gunakan Meja", width=30, command=self.selesai_gunakan_meja, bg="#4472C4", fg="white")
        self.btn_pesan.grid(row=0, column=0, padx=10, pady=40)
        self.btn_selesai.grid(row=1, column=0)
        
    def buat_pesanan(self):
        BuatPesanan(self.master)

    def selesai_gunakan_meja(self):
        SelesaiGunakanMeja(self.master)

class BuatPesanan(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)

        self.nama = tk.StringVar()
        self.master.geometry("400x200")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        self.lbl_nama = tk.Label(self, text="Siapa nama Anda?")
        self.ent_nama = tk.Entry(self,width=15, textvariable=self.nama)
        self.btn_back = tk.Button(self, text="Kembali", width=18, command=self.destroy, bg="#4472C4", fg="white")
        self.btn_next = tk.Button(self, text="Lanjut", width=18, command=self.validasi, bg="#4472C4", fg="white")

        self.lbl_nama.grid(row = 0, column = 0, padx = 20, pady = (50,0))
        self.ent_nama.grid(row = 0, column = 1, padx = 20, pady = (50,0))
        self.btn_back.grid(row = 1, column = 0, padx = 10, pady = (50,10))
        self.btn_next.grid(row = 1, column = 1, padx = 10, pady = (50,10)) 

        self.mainloop()

    def validasi(self): 
        find = False
        self.nama_pemesan = self.ent_nama.get()
        for nomor in daftar_pesanan.keys():
            if daftar_pesanan[nomor] == "":
                if self.nama_pemesan == "":
                    messagebox.showerror("Kafe Daun-Daun Pacilkom v2.0 🌿","Mohon maaf, Harap masukkan nama Anda"), self.destroy()
                    break

                else:
                    self.nomor_meja = random.randint(1,10)
                    find = True
                    MembuatTabel(daftar_menu, self.nama_pemesan, self.nomor_meja, self, self.master)
                    self.destroy()
                    
            elif nomor == 10 and daftar_pesanan[nomor] != "":
                messagebox.showerror("Kafe Daun-Daun Pacilkom v2.0 🌿","Mohon maaf Semua meja telah terisi penuh,\
                    silahkan datang kembali nanti"), self.destroy()
                
class MembuatTabel(tk.Toplevel):
    def __init__(self, data, nama, nomor_meja, data_nama, master = None):
        super().__init__(master)
        self.nama = nama
        self.data_nama = data_nama 
        self.nomor_user = nomor_meja
        
        self.master.geometry("400x200")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        self.lbl_nama = tk.Label(self, text = f"Nama Pemesan: {self.nama}")
        self.lbl_nomor = tk.Label(self,text = f"No Meja: {self.nomor_user}")
        self.lbl_total = tk.Label(self,text = f"Total harga: 0")
        self.btn_back = tk.Button(self, text="Kembali", command=self.destroy, bg="#4472C4", fg="white")
        self.btn_next = tk.Button(self, text="Ok", command=self.selesai_memesan, bg="#4472C4", fg="white")
        self.btn_ubah = tk.Button(self, text="Ubah", command= self.tampilkan_ubah_meja, bg="#4472C4", fg="white")

        self.lbl_nama.grid(row = 1, column = 1, padx = 0 , pady= 20)
        self.lbl_nomor.grid(row = 1, column = 4, padx = 0, pady = 20, sticky = "E")
        self.btn_ubah.grid(row = 1, column = 5, padx = 0, pady = 20, sticky = "W")

        self.list_combobox = []
        for key in daftar_menu.keys():
            if key == "MEALS":
                self.tambahan_row = 2
                self.info_tambahan = "Kegurihan"
            elif key == "DRINKS":
                self.tambahan_row = len(data["MEALS"]) + 4
                self.info_tambahan = "Kemanisan"
            elif key == "SIDES":
                self.tambahan_row = len(data["MEALS"]) + len(data["DRINKS"]) + 8
                self.info_tambahan = "Keviralan"

            self.key = key 
            self.data = data[key] 
            self.total_rows = len(self.data) 
            self.total_columns = len(self.data[0]) 
            self.generate_table()

        self.tambahan_row_bawah = len(data["MEALS"]) + len(data["DRINKS"]) + len(data["SIDES"]) + 16
        self.lbl_total.grid(row = self.tambahan_row_bawah-4, column = 5, padx = 0 , pady= 20)
        self.btn_back.grid(row=self.tambahan_row_bawah , column=2, padx = 5, pady = 20, sticky="N"+"E"+"S"+"W")
        self.btn_next.grid(row=self.tambahan_row_bawah , column=4, padx = 5, pady = 20, sticky="N"+"E"+"S"+"W")
        
        self.mainloop()

    def generate_table(self):
        self.lbl_submenu = tk.Label(self, text=self.key) 
        self.lbl_submenu.grid(row = self.tambahan_row, column = 1)

        header = ["Kode","Nama","Harga", self.info_tambahan,"Jumlah"] 
        kolom = 0
        for atribut in header:
            entry = tk.Entry(self, width = 20, fg = 'black')
            entry.grid(row = self.tambahan_row + 1, column = kolom + 1, sticky="N"+"S"+"E"+"W") 
            entry.insert(tk.END, atribut)
            entry['state'] = 'readonly'
            kolom += 1 
        
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                entry = tk.Entry(self, width = 20, fg = 'black')
                entry.grid(row = i + 2 + self.tambahan_row, column = j + 1,sticky="N"+"S"+"E"+"W")
                entry.insert(tk.END, self.data[i][j])
                entry['state'] = 'readonly'

            values = tuple([k for k in range(10)])
            self.opsi_jumlah = ttk.Combobox(self, values = values, state = "readonly")
            self.list_combobox.append(self.opsi_jumlah)
            self.opsi_jumlah.current(0)
            self.opsi_jumlah.bind("<<ComboboxSelected>>",self.get_Combobox_value_pesanan)
            self.opsi_jumlah.grid(row = i + 2 + self.tambahan_row, column = self.total_columns)

    def get_Combobox_value_pesanan(self, event):
        self.list_jumlah_pesanan = []

        for combobox in self.list_combobox:  
            jumlah_menu = combobox.get() 
            self.list_jumlah_pesanan.append(jumlah_menu)
        
        self.list_kode, self.list_nama, self.list_harga, self.list_info = [], [], [], []

        for jenis_menu in daftar_menu.keys(): 
            for tuple_menu_makanan in daftar_menu[jenis_menu]: 
                kode_menu, nama_menu, harga_menu, info_menu = tuple_menu_makanan[0], tuple_menu_makanan[1],\
                                                              tuple_menu_makanan[2], tuple_menu_makanan[3] 
                self.list_kode.append(kode_menu)
                self.list_nama.append(nama_menu)
                self.list_harga.append(harga_menu)
                self.list_info.append(info_menu)

        total = 0
        self.list_pesanan = []

        for i in range(len(self.list_harga)):
            total += int(self.list_harga[i]) * int(self.list_jumlah_pesanan[i]) 
            tuple_menu = (self.list_kode[i], self.list_nama[i], int(self.list_harga[i]), int(self.list_info[i]), int(self.list_jumlah_pesanan[i]))

            if int(self.list_jumlah_pesanan[i]) != 0: 
                self.list_pesanan.append(tuple_menu)

        self.lbl_total.config(text=f"Total harga: {total}")
        
    def selesai_memesan(self):
        if (self.list_pesanan) == []:
            messagebox.showerror("Kafe Daun-Daun Pacilkom v2.0 🌿","Mohon maaf, Harap masukkan angka pesanan")
            self.destroy()
            self.data_nama.destroy()

        elif (self.list_pesanan) != []: 
            nama_pemesan.append(self.nama)
            daftar_pesanan[self.nomor_user] = {self.nama: self.list_pesanan} 
            CloseWindow(self.data_nama, self, self.master)

    def tampilkan_ubah_meja(self):
        self.destroy()      
        UbahMeja(self.nomor_user, self, self.nama, self.data_nama, self.master) 
       
class UbahMeja(tk.Toplevel):
    def __init__(self, nomor_meja, tabel, nama, data_nama, master = None):
        super().__init__(master)
        list_nomor_meja = [[1,2,3,4,5], [6,7,8,9,10]]
        self.btn_meja = []
        self.nomor_user = nomor_meja
        self.tabel = tabel
        self.nama = nama
        self.data_nama = data_nama
        
        self.master.geometry("400x200")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        self.lbl_judul = tk.Label(self, text = "Silakan klik meja kosong yang diinginkan:")
        self.lbl_info = tk.Label(self, text = "Info")
        self.lbl_terisi = tk.Label(self, text = "Merah: Terisi")
        self.lbl_tersedia = tk.Label(self, text = "Abu - abu: Kosong")
        self.lbl_meja_user = tk.Label(self, text = "Biru: Meja Anda")

        self.btn_back = tk.Button(self, text="kembali", command= self.destroy, bg="#4472C4", fg="white")
        self.btn_ok = tk.Button(self, text="Ok", command= self.confirm_ubah_meja, bg="#4472C4", fg="white")

        self.lbl_judul.grid(row = 1, column = 1, columnspan=2, padx = 0 , pady= 0)
        self.lbl_info.grid(row = 7, column = 1, columnspan=2, padx = 0 , pady= 0)
        self.lbl_terisi.grid(row = 8, column = 1, columnspan=2, padx = 0 , pady= 0)
        self.lbl_tersedia.grid(row = 9, column = 1, columnspan=2, padx = 0 , pady= 0)
        self.lbl_meja_user.grid(row = 10, column = 1, columnspan=2, padx = 0 , pady= 0)

        self.btn_back.grid(row = 12, column=1, sticky="N"+"S"+"E"+"W", padx=2)
        self.btn_ok.grid(row = 12,column=2, sticky="N"+"S"+"E"+"W",padx=2)

        for i in range(2):
            for j in range(5):
                self.btn_angka = tk.Button(self, text = str(list_nomor_meja[i][j]), command =lambda x =list_nomor_meja[i][j]: 
                                           self.ubah_nomor_meja(x), bg="grey", fg="white", width=7,height=2)
                self.btn_angka.grid(row = 2 + j, column = 1 + i, padx = 5 , pady= 5)
                self.btn_meja.append(self.btn_angka)

                if list_nomor_meja[i][j] == self.nomor_user: 
                    self.btn_angka.config(bg = "#4472C4")
                    self.btn_angka.config(state = "disabled", disabledforeground = "white") 

                elif daftar_pesanan[list_nomor_meja[i][j]] != "":
                    self.btn_angka.config(bg = "red") 
                    self.btn_angka.config(state = "disabled", disabledforeground = "white")
        self.mainloop()

    def ubah_nomor_meja(self, nomor_meja):
        self.btn_meja[self.nomor_user-1].config(bg = "grey", state = "normal", disabledforeground = "white")
        self.nomor_user = nomor_meja 
        self.btn_meja[self.nomor_user-1].config(bg = "#4472C4", state = "disabled", disabledforeground = "white") 

    def confirm_ubah_meja(self):
        self.destroy()
        MembuatTabel(daftar_menu, self.nama, self.nomor_user, self.data_nama , self.master)

class CloseWindow(tk.Toplevel):
    def __init__(self, data_nama, self_window_membuat_tabel, master = None):
        super().__init__(master)
        self.data_nama = data_nama
        self.self_window_membuat_tabel = self_window_membuat_tabel

        self.data_nama.destroy()
        self.self_window_membuat_tabel.destroy()
        self.destroy()    

class SelesaiGunakanMeja(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.lbl_judul = tk.Label(self, text = "Silakan klik meja yang selesai digunakan:")
        self.lbl_info = tk.Label(self, text = "Info")
        self.lbl_terisi = tk.Label(self, text = "Merah: Terisi")
        self.lbl_tersedia = tk.Label(self, text = "Abu - abu: Kosong")
        self.btn_back = tk.Button(self, text = "kembali", command = self.destroy, bg = "#4472C4", fg = "white")

        self.lbl_judul.grid(row = 1, column = 1, columnspan=2, padx = 0 , pady= 0)
        self.lbl_info.grid(row = 7, column = 1, columnspan=2, padx = 0 , pady= 0)
        self.lbl_terisi.grid(row = 8, column = 1, columnspan=2, padx = 0 , pady= 0)
        self.lbl_tersedia.grid(row = 9, column = 1, columnspan=2, padx = 0 , pady= 0)
        self.btn_back.grid(row = 12, column=1,columnspan=2, sticky="N"+"S"+"E"+"W", padx=2)

        list_nomor_meja = [[1,2,3,4,5], [6,7,8,9,10]]
        self.btn_meja = []

        for i in range(2):
            for j in range(5):
                self.btn_angka = tk.Button(self, text = str(list_nomor_meja[i][j]), command = lambda x = list_nomor_meja[i][j]: self.tabel_pesanan_user(x), 
                                           bg="grey", fg="white", width=7,height=2, disabledforeground="white", state= "disabled")

                self.btn_angka.grid(row = 2 + j, column = 1 + i, padx = 5 , pady= 5)
                self.btn_meja.append(self.btn_angka)

                if daftar_pesanan[list_nomor_meja[i][j]] != "":
                    self.btn_angka.config(bg="red", state="normal")

        self.mainloop()

    def tabel_pesanan_user(self, nomor_meja_user):
        self.nomor_user = nomor_meja_user

        self.nama_user = list(daftar_pesanan[self.nomor_user].keys())
        self.nama_user = self.nama_user[0] 
        self.pesanan_user = daftar_pesanan[self.nomor_user][self.nama_user] 
        self.data_pesanan = copy.deepcopy(daftar_menu)
        
        for jenis_menu in self.data_pesanan.keys():
            for i in range(len(self.data_pesanan[jenis_menu])): 
                tuple_menu = self.data_pesanan[jenis_menu][i] 
                data_menu = tuple_menu[1] 

                for tuple_menu_user in self.pesanan_user: 
                    nama_makanan_yg_dipesan_user = tuple_menu_user[1]

                    if data_menu == nama_makanan_yg_dipesan_user: 
                        self.data_pesanan[jenis_menu][i] = list(self.data_pesanan[jenis_menu][i]) 
                        self.data_pesanan[jenis_menu][i][4] = tuple_menu_user[4]
                        self.data_pesanan[jenis_menu][i] = tuple(self.data_pesanan[jenis_menu][i])

        SelesaiGunakanMejaTabel(self.data_pesanan, self.nama_user, self.nomor_user, self, self.master)

class SelesaiGunakanMejaTabel(tk.Toplevel):
    def __init__(self, data, nama, nomor_meja, self_window_selesaigunakannomeja, master = None):
        super().__init__(master)
        self.self_window_selesaigunakannomeja = self_window_selesaigunakannomeja
        self.nomor_user = nomor_meja
        self.nama = nama
        self.total_user = 0

        self.master.geometry("400x200")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        self.lbl_nama = tk.Label(self, text = f"Nama Pemesan: {nama}")
        self.lbl_nomor = tk.Label(self,text = f"No Meja: {self.nomor_user}")
        self.lbl_total = tk.Label(self,text = f"Total harga: 0")
        self.btn_back = tk.Button(self, text="Kembali", command=self.destroy, bg="#4472C4", fg="white")
        self.btn_next = tk.Button(self, text="Ok", command=self.checkout_pesanan, bg="#4472C4", fg="white")
        self.lbl_nama.grid(row = 1, column = 1, padx = 0 , pady= 20)
        self.lbl_nomor.grid(row = 1, column = 4, padx = 0, pady = 20)

    
        for key in data.keys():
            if key == "MEALS":
                self.tambahan_row = 2
                self.info_tambahan = "Kegurihan"
            elif key == "DRINKS":
                self.tambahan_row = len(data["MEALS"]) + 4
                self.info_tambahan = "Kemanisan"
            elif key == "SIDES":
                self.tambahan_row = len(data["MEALS"]) + len(data["DRINKS"]) + 8
                self.info_tambahan = "Keviralan"
  
            self.key = key
            self.data = data[key]
            self.total_rows, self.total_columns = len(self.data), len(self.data[0])
            self.generate_table()

        self.tambahan_row_bawah = len(data["MEALS"]) + len(data["DRINKS"]) + len(data["SIDES"])+ 16
        self.lbl_total.grid(row = self.tambahan_row_bawah-4, column = 5, padx = 0 , pady= 20)
        self.btn_back.grid(row=self.tambahan_row_bawah , column=2, padx = 5, pady = 20, sticky="N"+"S"+"E"+"W")
        self.btn_next.grid(row=self.tambahan_row_bawah , column=4,padx=5, pady = 20, sticky="N"+"S"+"E"+"W")

        self.mainloop()

    def generate_table(self):
        self.lbl_submenu = tk.Label(self, text=self.key)
        self.lbl_submenu.grid(row=self.tambahan_row, column=1)

        header = ["Kode", "Nama", "Harga", self.info_tambahan, "Jumlah"]
        kolom = 0
        for atribut in header:
            self.atribut = tk.Entry(self, width = 20, fg = 'black')
            self.atribut.grid(row = self.tambahan_row + 1, column = kolom + 1, sticky="N"+"S"+"E"+"W")
            self.atribut.insert(tk.END, atribut)
            self.atribut['state'] = 'readonly'
            kolom += 1

        for i in range(self.total_rows):
            for j in range(self.total_columns):
                self.entry = tk.Entry(self, width = 20, fg = 'black')
                self.entry.grid(row = i + 2 + self.tambahan_row, column = j + 1,sticky="N"+"S"+"E"+"W")
                self.entry.insert(tk.END, self.data[i][j])
                self.entry['state'] = 'readonly'

            harga, jumlah = self.data[i][2], self.data[i][4]
            self.total_user += harga * jumlah

        self.lbl_total.config(text=f'Total harga: {self.total_user}')
        
    def checkout_pesanan(self):
        daftar_pesanan[self.nomor_user] = ""
        CloseWindowTelahBerkunjung(self.self_window_selesaigunakannomeja, self, self.master)

class CloseWindowTelahBerkunjung(tk.Toplevel):
    def __init__(self, self_window_selesaigunakannomeja, self_window_selesaitabelnomeja, master = None):
        super().__init__(master)
        self.self_window_selesaigunakannomeja = self_window_selesaigunakannomeja
        self.self_window_selesaitabelnomeja = self_window_selesaitabelnomeja
        
        self.self_window_selesaigunakannomeja.destroy()
        self.self_window_selesaitabelnomeja.destroy()

        self.destroy()

def main():
    global daftar_menu, daftar_pesanan, nama_pemesan
  
    daftar_menu = {} 
    daftar_pesanan = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: ''}
    nama_pemesan = []

    with open("menu.txt", "r") as file:
        for lines in file:
            if lines.startswith("==="):
                submenu = lines.replace("===", "").strip()
                daftar_menu[submenu] = []

            elif ";" in lines:
                data = lines.strip().split(";")
                kode, nama, harga, info = data[0], data[1], data[2], data[3]
                
                if submenu == "MEALS":
                    daftar_menu[submenu].append(Meals(kode, nama, harga, info).getTuple()) 
                elif submenu == "DRINKS":
                    daftar_menu[submenu].append(Drinks(kode, nama, harga, info).getTuple()) 
                elif submenu == "SIDES":
                    daftar_menu[submenu].append(Sides(kode, nama, harga, info).getTuple()) 
    
    window = tk.Tk()
    cafe = Main(window)
    window.mainloop()

if __name__ == '__main__':
    main()
