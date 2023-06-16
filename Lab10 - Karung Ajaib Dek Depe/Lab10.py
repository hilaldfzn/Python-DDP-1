import tkinter as tk 
import tkinter.messagebox as tkmsg 
 
class MainWindow(tk.Frame): 
    def __init__(self, master): 
        super().__init__(master) 
        self.master.title("Karung Ajaib") 
        self.pack() 
        self.create_widgets() 
 
    # Lengkapi Binding Event Handler dengan buttons yang ada 
    def create_widgets(self): 
        self.label = tk.Label(self, 
                              text = "Selamat datang Dek Depe di Karung Ajaib. Silahkan pilih Menu yang tersedia") 
 
        self.btn_lihat_daftar_karung = tk.Button(self, 
                                                text = "LIHAT DAFTAR KARUNG", 
                                                command = self.popup_lihat_karung) 
        self.btn_masukkan_item = tk.Button(self,  
                                            text = "MASUKKAN ITEM",  
                                            command = self.popup_add_item) 
        self.btn_keluarkan_item = tk.Button(self, 
                                        text = "KELUARKAN ITEM",  
                                        command = self.popup_keluarkan_item) 
        self.btn_exit = tk.Button(self, 
                                  text = "EXIT", 
                                  command = self.master.destroy) 
 
        self.label.pack() 
        self.btn_lihat_daftar_karung.pack() 
        self.btn_masukkan_item.pack() 
        self.btn_keluarkan_item.pack() 
        self.btn_exit.pack() 
 
    # semua item dalam karung 
    def popup_lihat_karung(self): 
        PopupLihatKarung(self.master) 
 
    # menu masukkan item 
    def popup_add_item(self): 
        PopupAddItem(self.master) 
 
    # menu keluarkan item 
    def popup_keluarkan_item(self): 
        PopupKeluarkanItem(self.master) 
 
class PopupLihatKarung(object): 
  def __init__(self, master): 
    self.main_window = tk.Toplevel() 
    self.main_window.geometry("280x100") 
    self.main_window.wm_title("Lihat Karung") 
 
    self.title = tk.Label(self.main_window, text="Daftar Karung Ajaib") 
    self.nama = tk.Label(self.main_window, text="Nama Item") 
    self.title.pack() 
    self.nama.pack() 
 
    # Tampilkan halaman Lihat Karung Ajaib 
    if len(item_set) == 0: 
        pass 
    else: 
        count = 1 
        for i in sorted(item_set): 
            tk.Label(self.main_window, text=str(count) + ". " + i).pack() 
            count += 1 
    self.exit_button = tk.Button(self.main_window, text="EXIT", command = self.main_window.destroy) 
    self.exit_button.pack() 
     
# Class Masukkan Item  
class PopupAddItem(object): 
     
    def __init__(self,master): 
        self.main_window = tk.Toplevel() 
        self.main_window.wm_title("Masukkan item") 
        self.main_window.geometry("280x100") 
 
        # Create Widget untuk tampilan Masukkan Item 
        # Title 
        self.title = tk.Label(self.main_window, text='Input Masukkan Item') 
        self.title.pack() 
 
        # Entry Nama item 
        self.ent_nama_barang= tk.StringVar() 
        self.lbl_nama = tk.Label(self.main_window, text = 'Nama Item') 
        self.lbl_nama.pack() 
        self.entry_nama = tk.Entry(self.main_window, textvariable=self.ent_nama_barang) 
        self.entry_nama.pack() 
 
        self.submit_button = tk.Button(self.main_window, text = 'Masukkan', command = self.masukkan_item) 
        self.submit_button.pack() 
 
    def masukkan_item(self): 
        # Create Method untuk Masukkan Item 
        nama_item = self.ent_nama_barang.get() 
        if nama_item in item_set: 
            tkmsg.showwarning(title='ItemHasFound', message='Item dengan nama ' + nama_item + ' sudah ada di dalam KarungAjaib. Item ' + nama_item + ' tidak bisa dimasukkan lagi.') 
        else: 
            item_set.add(nama_item) 
            tkmsg.showinfo("Berhasil!", f"Berhasil memasukkan item " + nama_item) 
        return 
     
# Class Keluarkan Item 
class PopupKeluarkanItem(object): 
     
  def __init__(self, master): 
    self.main_window = tk.Toplevel() 
    self.main_window.wm_title("Keluarkan item") 
    self.main_window.geometry("280x100") 
 
    # Create Widget untuk tampilan Keluarkan Item 
    # Title 
    self.title = tk.Label(self.main_window, text='Input Keluarkan Item') 
    self.title.pack() 
 
    # Entry Nama item 
    self.ent_nama_barang= tk.StringVar() 
    self.lbl_nama = tk.Label(self.main_window, text = 'Nama Item') 
    self.lbl_nama.pack() 
    self.entry_nama = tk.Entry(self.main_window, textvariable=self.ent_nama_barang) 
    self.entry_nama.pack() 
 
    self.submit_button = tk.Button(self.main_window, text = "Ambil" , command = self.keluarkan_item) 
    self.submit_button.pack() 
 
  def keluarkan_item(self): 
    # Create Method untuk Keluarkan Item 
    nama_item = self.ent_nama_barang.get() 
 
    if nama_item in item_set: 
        tkmsg.showinfo("Berhasil!", f"Berhasil mengeluarkan item " + nama_item) 
        item_set.remove(nama_item) 
    else: 
        tkmsg.showwarning(title='ItemHasNotFound', message='Item dengan nama ' + nama_item + ' tidak ditemukan di dalam KarungAjaib') 
    return 
                   
item_set = set() 
if __name__ == "__main__": 
    root = tk.Tk() 
    m=MainWindow(root) 
    root.mainloop()
