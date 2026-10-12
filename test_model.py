from models.buku_model import BukuModel

model = BukuModel()

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# 3. Menguji fungsi Update (Ubah ID 6 sesuai ID buku yang ada di DB Anda)
print("\n--- Mengubah Data Buku ID 9 ---")
model.update_buku(9, "Pemrograman Python MVC (Edisi Revisi)", "Guido van Rossum", 2024)
print("Data berhasil diubah!")

print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# 3. Menguji fungsi Delete (Menghapus buku)
print("\n--- Menghapus Buku ID 9 ---")
model.delete_buku(9)
print("Data berhasil dihapus!")

print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")