import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:

  def __init__(self):
    # Inisialisasi Model dan View Anggota
    self.model = AnggotaModel()
    self.view = AnggotaView()

    # Binding (mengikat) tombol di View dengan fungsi di Controller
    self.view.btn_simpan.configure(command=self.simpan_data)
    
    # Tambahan binding untuk tombol Update dan Hapus
    self.view.btn_update.configure(command=self.update_data)
    self.view.btn_delete.configure(command=self.hapus_data)

    # Memuat data ke tabel saat aplikasi pertama kali dibuka
    self.muat_data_tabel()

  def muat_data_tabel(self):
    # Mengosongkan isi tabel di View terlebih dahulu
    for item in self.view.tabel.get_children():
      self.view.tabel.delete(item)

    # Mengambil data dari Model (database) Anggota
    data_anggota = self.model.get_all_anggota()

    # Memasukkan data baru ke dalam tabel View (hanya ID, Nama, Alamat)
    for anggota in data_anggota:
      self.view.tabel.insert(
          "", "end", values=(anggota["id_anggota"], anggota["nama"], anggota["alamat"])
      )

  def get_selected_id(self):
    """Helper untuk mengambil id_anggota dari baris tabel yang dipilih pengguna"""
    selected_item = self.view.tabel.selection()
    if not selected_item:
      return None
    item_data = self.view.tabel.item(selected_item)
    return item_data["values"][0]

  def simpan_data(self):
    # Mengambil teks dari kotak input di View Anggota (hanya nama dan alamat)
    nama = self.view.entry_nama.get()
    alamat = self.view.entry_alamat.get()

    # Validasi Form Kosong
    if not nama or not alamat:
      messagebox.showwarning("Peringatan", "Semua kolom form (Nama dan Alamat) harus diisi!")
      return

    # Mengirim data ke Model untuk disimpan
    berhasil = self.model.create_anggota(nama, alamat)

    if berhasil:
      messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
      # Bersihkan form input
      self.view.entry_nama.delete(0, "end")
      self.view.entry_alamat.delete(0, "end")
      # Muat ulang tabel agar data terbaru muncul
      self.muat_data_tabel()
    else:
      messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data anggota.")

  def update_data(self):
    """Logika untuk memperbarui data anggota yang dipilih"""
    id_anggota = self.get_selected_id()
    if not id_anggota:
      messagebox.showwarning("Peringatan", "Pilih baris anggota yang ingin diperbarui di tabel!")
      return

    nama = self.view.entry_nama.get()
    alamat = self.view.entry_alamat.get()

    if not nama or not alamat:
      messagebox.showwarning("Peringatan", "Semua kolom form harus diisi untuk update!")
      return

    berhasil = self.model.update_anggota(id_anggota, nama, alamat)
    if berhasil:
      messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
      self.view.entry_nama.delete(0, "end")
      self.view.entry_alamat.delete(0, "end")
      self.muat_data_tabel()
    else:
      messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data anggota.")

  def hapus_data(self):
    """Logika untuk menghapus data anggota yang dipilih"""
    id_anggota = self.get_selected_id()
    if not id_anggota:
      messagebox.showwarning("Peringatan", "Pilih baris anggota yang ingin dihapus di tabel!")
      return

    konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data anggota ini?")
    if konfirmasi:
      berhasil = self.model.delete_anggota(id_anggota)
      if berhasil:
        messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
        self.muat_data_tabel()
      else:
        messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data anggota.")

  # Fungsi untuk menyalakan aplikasi
  def run(self):
    self.view.mainloop()